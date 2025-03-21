from flask import Flask

#name le indica a python el nombre del 
app = Flask(__name__)

#app es la instancia q tiene de flask
#nos permite exponer una funcion para que se ejecute desde web

@app.route('/saludar')
def hola_mundo():
    return 'Hola mundo!'

@app.route('/despedir')
def adios_mundo():
    return 'Adiós mundo!'

@app.route('/hablar')
def hola_hola():
    return 'Hola hola!'

@app.route('/hola')
def hola_html():
    return '<h1 style="color:red;">Hola!!</h1>'

@app.route('/json')
def json():
    return Response('{"nombre":"john"}', mimetype='application/json')

@app.route('/xml')
def xml():
    return '<?xml version="1.0"?><nombre>John</nombre>'
    return Response(xml, mimetype='application/xml')

if __name__=='__main__':
    app.run(host='0.0.0.0',
debug=True)
