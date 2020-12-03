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
	for x in range(1,51):

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
			

			respuesta = api.get("https://maketeam.herokuapp.com/all_teams")
			dato = json.loads(respuesta.content)
			for x in dato:
				if nombre == x['user_name']:
					return render_template("añadir.html",pokemons = imagenes,texto = "Usuario tomado")
				
			url = 'https://maketeam.herokuapp.com/MissingNo151/new_team/'
			api.post(url,json = datos)


			
			if '' in form.values():
				return render_template("añadir.html", pokemons = imagenes,texto = "")		

			return  redirect("/success")
		except:
			return  render_template("añadir.html",pokemons = imagenes,texto ="")
		
	return render_template("añadir.html", pokemons = imagenes,texto = "")

@app.route('/home',methods = ["GET","POST"])
def index():
	
	if request.method == "POST":
		print("Vale")
		nombre = request.form['nombre']

		respuesta = api.get(f"https://maketeam.herokuapp.com/MakeTeams/{nombre}/")
	
		dato = json.loads(respuesta.content)
		print(dato)
		if dato == None:
			return render_template("fallo.html")
		return render_template("solo.html", info = dato)	
	else:
		
		respuesta = api.get("https://maketeam.herokuapp.com/all_teams")
		dato = json.loads(respuesta.content)
		return render_template("index.html", info = dato)
	

@app.route('/delete', methods = ['GET','POST','DELETE'])
def eliminar():
	if request.method == "POST":
		if (request.form['token'] != 'MissingNo151'):
			return render_template('fallo.html')
		else:
			try:
				usuario = request.form['nombre']
				api.delete(f'https://maketeam.herokuapp.com/MissingNo151/MakeTeams/del/{usuario}')
				return render_template('exito.html')
			except :
				return render_template('fallo.html')
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
			return render_template("fallo.html")
		else:
			url = f'https://maketeam.herokuapp.com/MissingNo151/MakeTeams/update/{nombre}'
			api.put(url,json = nuevos_datos)
			return render_template("exito.html")

		
	else:
	    return render_template("actualizar.html")

@app.route('/success')
def success():
	return render_template("exito.html")
	
@app.route('/fail')
def fail():
    return render_template('fallo.html')

	
""" if __name__ == "__main__":
	app.run() """