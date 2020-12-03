""" Se importan los módulos, que en caso de requerirse se instalan en el entorno virtual de python """
from flask import Flask, redirect, render_template,url_for,request,flash
import requests as api
import json
import os
import json
import time
from bson.json_util import dumps

""" Esta función esta al inicio del programa para que limpie la consola """
def clear(): os.system('clear')
clear()

app = Flask(__name__)

""" Es una serie de rutas que definen el comportamiento del software, se utiliza la funcion render templates, para no mostrar las rutas de los archivos """
""" dentro del servidor """

""" La primer ruta es root y redirecciona el dominio inicial a la página de inicio que tiene la ruta /home """
@app.route('/')
def redirect_home():
	return redirect(url_for('.index'))


""" Esta función es para añadir pokémones, por medio de una interfáz gráfica se selecciona el pokemón por nombre y se ingresa el nombre de usuario """
""" esto esta dentro de un formulario, y se extraen los datos para enviarlos a la base de datos por medio de la API. """
""" El método GET se utiliza para cargar los pokémones en el menú, el método POST para jalar los datos del formulario y enviarlos. """

@app.route("/add", methods = ["GET","POST"])
def anadir():
	
	""" Puede que sea un número limitado de pokémones por que la API de donde se obtienen los datos pokémones tiene problemas de desempeño, y tarda hasta 1 minuto por pokémon """
	imagenes = {}
	for x in range(1,51):

		""" Se hace la petición y en un json se guardan la dirección de las imágenes para cargarlas en el front end el nombre del pokémon y la imágen, la cual se renderiza cuando se seleccione el nombre de alguno  """
	
		respuesta = api.get(f"https://pokeapi.co/api/v2/pokemon-form/{x}/")

		dato = json.loads(respuesta.content)
		imagenes[x] = dato
	
	""" Esta parte del código se utiliza en caso de que se accione el formulario """
	if request.method == "POST":
		""" Se utiliza try/excetp para el manejo de errores, en caso de tener uno se carga la página de nuevo """
		try:
			
			""" La base de datos da errores da errores si el string tiene espacios asi que se reemplaza por un guión bajo """
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
			
			""" Se valida que el nombre de usuario no esté en la base de datos """
			respuesta = api.get("https://maketeam.herokuapp.com/all_teams")
			dato = json.loads(respuesta.content)
			for x in dato:
				if nombre == x['user_name']:
					return render_template("añadir.html",pokemons = imagenes,texto = "Usuario tomado")

			""" Se valida que el campo nombre no esté vacio """
			if '' in form.values():
				return render_template("añadir.html", pokemons = imagenes,texto = "")		

			url = 'https://maketeam.herokuapp.com/MissingNo151/new_team/'
			api.post(url,json = datos)
						
			""" En caso de que todo se ejecute de manera correctase se manda a una página con un mensaje de éxito """
			return  redirect("/success")
		except:
			""" Si algo falla se vuelve a cargar la plantilla """
			return  render_template("añadir.html",pokemons = imagenes,texto ="")
		
	""" Se carga la plantilla si el método es GET """
	return render_template("añadir.html", pokemons = imagenes,texto = "")

""" Es la plantila inicial,tiene 2 secciones principales una muestra los equipos de pokémones, y otra busca usuarios por medio de una barra de búsqueda """
@app.route('/home',methods = ["GET","POST"])
def index():
	
	""" Si se utiliza el formulario se entra a esta parte de la ruta y se busca el nombre ingresado en la barra """
	if request.method == "POST":
		
		nombre = request.form['nombre']

		respuesta = api.get(f"https://maketeam.herokuapp.com/MakeTeams/{nombre}/")
	
		dato = json.loads(respuesta.content)
		
		if dato == None:
			return render_template("fallo.html")
		return render_template("solo.html", info = dato)	
	else:
		""" Si el método es GET se carga la plantila de manera normal """
		respuesta = api.get("https://maketeam.herokuapp.com/all_teams")
		dato = json.loads(respuesta.content)
		return render_template("index.html", info = dato)
	

""" El método GET es necesario para cargar la página
3 métodos son necesarios para cargar la página si lo codificamos en una sola función """
@app.route('/delete', methods = ['GET','POST','DELETE'])
def eliminar():
	""" el método POST es para obtener los valores del formulario HTML """
	if request.method == "POST":
		""" Se valida por medio de una contraseña """
		if (request.form['token'] != 'MissingNo151'):
			return render_template('fallo.html')
		else:
			try:
				usuario = request.form['nombre']
				""" Se elimina un usuario, de la base de datos propia por medio de la API
				el método DELETE es para hacer una eliminación en la base de datos """

				api.delete(f'https://maketeam.herokuapp.com/MissingNo151/MakeTeams/del/{usuario}')

				""" Se renderiza una plantilla de éxito en caso de que la operación se ejecute """
				return render_template('exito.html')
			except :
				""" Se renderiza una plantilla de fallo en caso de que la operación no se ejecute """
				return render_template('fallo.html')

	""" Si no se acciona el botón del formulario se renderiza la plantilla para ingresar los datos """
	return render_template("eliminar.html")

""" El método GET es necesario para cargar la página
3 métodos son necesarios para cargar la página """
@app.route('/update', methods = ['GET','PUT','POST'])
def actualizar():
	""" Si se jalan datos de formulario se utiliza este método """
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

		""" Se valida con una clave ingresada en el front end """
		if request.form['clave'] != 'MissingNo151':
			return render_template("fallo.html")
		else:
			""" Si todo se ejecuto bien hasta este punto se hace la actualización """
			url = f'https://maketeam.herokuapp.com/MissingNo151/MakeTeams/update/{nombre}'
			api.put(url,json = nuevos_datos)
			return render_template("exito.html")		
	else:
	    return render_template("actualizar.html")

""" Estas rutas muestran una página con un mensaje de éxito o error y se utiliza bastante a lo largo del código 
dentro del mismo HTML tiene un script de JS para que se muestre la página por un segundo y se redirige a index """

@app.route('/success')
def success():
	return render_template("exito.html")
	
@app.route('/fail')
def fail():
    return render_template('fallo.html')


""" Para su implementación en heroku se necesita llamar desede otro archivo en la carpeta raíz per se mantiene comentado 
para su explicación  """

""" if __name__ == "__main__":
	app.run() """
