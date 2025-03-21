from flask import Flask, render_template
from producto import Producto
from flask import request
from flask import Response
from flask import redirect, url_for

#la instancia
app = Flask(__name__)

productos = [Producto("Computadora", 200), Producto("Impresora", 50)]

@app.route('/')
def inicio():
   # productos = [Producto("Computadora", 200), Producto("Impresora", 50)]
    return render_template('productos.html', productos=productos)

@app.route('/editar/<producto>/<precio>')
def editar(producto, precio):
    #recuperar el producto
    print(producto)
    return render_template('editar.html', producto=producto, precio=precio)

@app.route('/guardar', methods=['POST'])
def guardar():
    n = request.form.get('nombre')
    p = request.form.get('precio')

    print(f"Producto actualizado: {n}, Precio: {p}")
    i = 0
    for e in productos:
        if e.nombre == n:
            productos[i] = Producto(n,p)
            print(f"{e.nombre} {e.precio}")
        i+=1
    return Response("guardado", headers={'Location': '/'}, status=302)

@app.route('/eliminar/<nombre>')
def eliminar(nombre):
    i = 0
    for e in productos:
        if e.nombre == nombre:
            productos.pop(i)
            print(f"{e.nombre} {e.precio}")
        i+=1
    return Response("eliminado", headers={'Location': '/'}, status=302)

@app.route('/crear', methods=['POST'])
def crear():
    n = request.form.get('nombre')
    p = request.form.get('precio')

    if n and p:  # Verifica que los valores no estén vacíos
        productos.append(Producto(n, p))
        print(f"Producto agregado: {n}, Precio: {p}")

    return redirect(url_for('inicio'))


#el lanzamiento del servidor
if __name__=='__main__':
    app.run(host='0.0.0.0',
debug=True)