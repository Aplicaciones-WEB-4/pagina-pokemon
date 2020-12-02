from flask import Flask, redirect, render_template,url_for,request,flash
import requests as api
import json
import os
import json
import time
from bson.json_util import dumps


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
		try:
			
			nombre = request.form["user_name"].replace(' ','_')
			
			datos = {
			"poke_id0" : request.form["poke0"],
			"poke_id1" : request.form["poke1"],
			"poke_id2" : request.form["poke2"],
			"poke_id3" : request.form["poke3"],
			"poke_id4" : request.form["poke4"],
			"poke_id5" : request.form["poke5"],
			"user_name" : nombre
			}
			
			url = 'https://maketeam.herokuapp.com/MissingNo151/new_team/'
			api.post(url,json = datos)

			if '' in form.values():
				return render_template("añadir.html", pokemons = imagenes)

			

			variable0 = api.get(f"https://pokeapi.co/api/v2/pokemon-form/{poke_id0}/").json()
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
			print("usr name "+user_name)
			return  redirect("/success")
		except:
			return  render_template("añadir.html",pokemons = imagenes)
		
	return render_template("añadir.html", pokemons = imagenes)

@app.route('/home',methods = ["GET"])
def index():
	respuesta = api.get("https://maketeam.herokuapp.com/all_teams")
	dato = json.loads(respuesta.content)
	for	x in dato:
		print(x['user_name'])

	return render_template("index.html", info = dato)

@app.route('/delete', methods = ['GET','PUT','DELETE'])
def eliminar():
    return render_template("eliminar.html")

@app.route('/update', methods = ['GET','PUT','POST'])
def actualizar():
	if request.method == "POST":
		nuevos_datos = {
			
			"poke_id0" :  request.form["pokemon1"],
			"poke_id1" :  request.form["pokemon2"],
			"poke_id2" :  request.form["pokemon3"],
			"poke_id3" :  request.form["pokemon4"],
			"poke_id4" :  request.form["pokemon5"],
			"poke_id5" :  request.form["pokemon6"],
			"user_name" :  request.form["nombreN"]
		}
		nombre = request.form["nombre"]
		if request.form['clave'] != 'MissingNo151':
			return render_template("index.html")
		else:
			url = f'https://maketeam.herokuapp.com/MissingNo151/MakeTeams/update/{nombre}'
			api.put(url,json = nuevos_datos)
			return render_template("index.html")

		
	else:
	    return render_template("actualizar.html")

@app.route('/success')
def success():
	return render_template("exito.html")
	
@app.route('/fail')
def fail():
    return render_template('fallo.html')


if __name__ == "__main__":
	app.run(debug=True,port=8080)


