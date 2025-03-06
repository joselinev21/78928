from flask import Flask

#name le indica a python el nombre del 
app = Flask(__name__)

#app es la instancia q tiene de flask
#nos permite exponer una funcion para que se ejecute desde web

@app.route('/')
def hola_mundo():
    return 'Hola mundo!'
if __name__=='__main__':
    app.run(host='0.0.0.0',
debug=True)
