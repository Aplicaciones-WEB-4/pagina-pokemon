from flask import Flask, redirect, render_template,url_for,request,flash
import requests as api
import json
import os
import json
import time

def clear(): os.system('clear')
clear()

app = Flask(__name__)

@app.route('/')
def redirect_home():
	return redirect(url_for('.index'))

@app.route("/add", methods = ["GET","POST"])
def anadir():
	imagenes = {}
	for x in range(1,50):

		respuesta = api.get(f"https://pokeapi.co/api/v2/pokemon-form/{x}/")

		dato = json.loads(respuesta.content)
		imagenes[x] = dato
		print(x)

	if request.method == "POST":
		try:

			poke_id0 = request.form["poke0"]
			poke_id1 = request.form["poke1"]
			poke_id2 = request.form["poke2"]
			poke_id3 = request.form["poke3"]
			poke_id4 = request.form["poke4"]
			poke_id5 = request.form["poke5"]
			user_name = request.form["user_name"]

			form = {
				"poke_id0" : poke_id0,
				"poke_id1" : poke_id1,
				"poke_id2" : poke_id2,
				"poke_id3" : poke_id3,
				"poke_id4" : poke_id4,
				"poke_id5" : poke_id5,
				"user_name" : request.form["user_name"]
			}

			if '' in form.values():
				return render_template("añadir.html", pokemons = imagenes)

			print("usr name "+user_name)

			variable0 = api.get(f"https://pokeapi.co/api/v2/pokemon-form/"+poke_id0+"/").json()
			variable1 = api.get(f"https://pokeapi.co/api/v2/pokemon-form/"+poke_id1+"/").json()
			variable2 = api.get(f"https://pokeapi.co/api/v2/pokemon-form/"+poke_id2+"/").json()
			variable3 = api.get(f"https://pokeapi.co/api/v2/pokemon-form/"+poke_id3+"/").json()
			variable4 = api.get(f"https://pokeapi.co/api/v2/pokemon-form/"+poke_id4+"/").json()
			variable5 = api.get(f"https://pokeapi.co/api/v2/pokemon-form/"+poke_id5+"/").json()

			print(variable0["pokemon"]["name"])
			print(variable1["pokemon"]["name"])
			print(variable2["pokemon"]["name"])
			print(variable3["pokemon"]["name"])
			print(variable4["pokemon"]["name"])
			print(variable5["pokemon"]["name"])

			return  redirect("/success")
		except:
			return  render_template("añadir.html",pokemons = imagenes)
		
	return render_template("añadir.html", pokemons = imagenes)

@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/delete')
def eliminar():
    return render_template("eliminar.html")

@app.route('/update')
def actualizar():
    return render_template("actualizar.html")

@app.route('/login')
def inicio_sesion():
    return render_template("iniciosesion.html")

@app.route('/signup')
def registro():
    return render_template("registro.html")

@app.route('/settings')
def configurar():
    return render_template("configurar.html")

@app.route('/profile')
def perfil():
    return render_template("perfil.html")

@app.route('/success')
def success():
	return render_template("exito.html")
	
@app.route('/fail')
def fail():
    return cosa()


if __name__ == "__main__":
	app.run(debug=True,port=8080)