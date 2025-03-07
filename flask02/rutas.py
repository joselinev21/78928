from flask import Flask, render_template
from modelos import Producto

#la instancia
app = Flask(__name__)

@app.route('/')
def inicio():
    productos = [Producto("Manzanas", 12), Producto("Peras", 13)]
    return render_template('index.html', productos=productos)


#el lanzamiento del servidor
if __name__=='__main__':
    app.run(host='0.0.0.0',
debug=True)