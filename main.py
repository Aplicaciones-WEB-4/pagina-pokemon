from flask import Flask, redirect, render_template,url_for,request,jsonify
import requests as api
from app import create_app
import json
import db_config as db
from bson.json_util import dumps


app = create_app()
# app = Flask(__name__)


@app.route('/test')
def test():
    return jsonify({
        "message": "API working ok",

    })


@app.route('/crear', methods = ['POST'])
def test2():
    db.db.MakeTeams.insert_one({
    "Miembro1": request.json["Miembro1"],
    "Miembro2": request.json["Miembro2"],
	"Miembro3": request.json["Miembro3"],
	"Miembro4": request.json["Miembro4"],
	"Miembro5": request.json["Miembro5"],
	"Miembro6": request.json["Miembro6"],
	"Nombre_usuario": request.json["Nombre_usuario"]
    })
    return jsonify({
        "message":"A new keyboard was added with success",
        "status": 200,
    })

@app.route("/hacer", methods = ["GET","POST"])
def obtener():
	imagenes = {}
	for x in range(1,11):

		respuesta = api.get(f"https://pokeapi.co/api/v2/Miembro-form/{x}/")



		dato = json.loads(respuesta.content)
		imagenes[x] = dato
		print(x)
	return render_template("makeTeam.html", Miembros = imagenes)


if __name__ == "__main__":
	app.run(debug=True,port=8080)
