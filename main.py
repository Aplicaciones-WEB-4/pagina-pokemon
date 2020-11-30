from flask import Flask, redirect, render_template,url_for,request
import requests as api
import json
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def obtener():
	imagenes = {}
	for x in range(1,4):

		respuesta = api.get(f"https://pokeapi.co/api/v2/pokemon-form/{x}/")



		dato = json.loads(respuesta.content)
		imagenes[x] = dato
		print(x)
	return render_template("makeTeam.html", pokemons = imagenes)


if __name__ == "__main__":
	app.run(debug=True,port=8080)
