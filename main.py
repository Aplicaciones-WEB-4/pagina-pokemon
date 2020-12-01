from flask import Flask, redirect, render_template,url_for,request,flash
import requests as api
import json
import os
import json


def clear(): os.system('clear')
clear()

app = Flask(__name__)

@app.route('/')
def redirect_home():
	return redirect(url_for('.index'))

@app.route("/add", methods = ["GET","POST"])
def anadir():
	imagenes = {}
	for x in range(1,7):

		respuesta = api.get(f"https://pokeapi.co/api/v2/pokemon-form/{x}/")

		dato = json.loads(respuesta.content)
		imagenes[x] = dato
		print(x)

	if request.method == "POST":
		
		poke_id0 = request.form["poke0"]
		poke_id1 = request.form["poke1"]
		poke_id2 = request.form["poke2"]
		poke_id3 = request.form["poke3"]
		poke_id4 = request.form["poke4"]
		poke_id5 = request.form["poke5"]
		
		user_name = request.form["user_name"]
		
	for z in range (0,6):
		print("Poke id "+poke_id)
	
	print("Poke id "+poke_id1)
	print("Poke id "+poke_id2)
	print("Poke id "+poke_id3)
	print("Poke id "+poke_id4)
	print("Poke id "+poke_id5)

	print("usr name "+user_name)

	variable1 = api.get(f"https://pokeapi.co/api/v2/pokemon-form/"+poke_id1+"/").json()
	variable2 = api.get(f"https://pokeapi.co/api/v2/pokemon-form/"+poke_id2+"/").json()
	print(variable1["pokemon"]["name"])
	print(variable2["pokemon"]["name"])
	
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


if __name__ == "__main__":
	app.run(debug=True,port=8080)
