from flask import render_template, request, redirect
from app import app, db
from models import Cliente, Producto, Proveedor, Compra, Venta
from datetime import date

#Se que habia que hacer usuario de vendedor y administrador, pero no llegamos con el tiempo

@app.route("/")
def inicio():
    return render_template("index.html")

# CLIENTES#

@app.route("/clientes", methods=["GET", "POST"])

def clientes():
    if request.method == "POST":
        nuevo = Cliente(
            nombre=request.form["nombre"],
            telefono=request.form["telefono"],
            direccion=request.form["direccion"]
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect("/clientes")

    lista = Cliente.query.all()
    return render_template("clientes.html", clientes=lista)

@app.route("/clientes/eliminar/<int:id>")

def clientes_eliminar(id):
    if current_user.rol != "admin":
        return "No autorizado"
    c = Cliente.query.get(id)
    db.session.delete(c)
    db.session.commit()
    return redirect("/clientes")


#PROVEEDORES#

@app.route("/proveedores", methods=["GET", "POST"])

def proveedores():
    if request.method == "POST":
        nuevo = Proveedor(
            nombre=request.form["nombre"],
            contacto=request.form["contacto"]
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect("/proveedores")

    lista = Proveedor.query.all()
    return render_template("proveedores.html", proveedores=lista)

@app.route("/proveedores/eliminar/<int:id>")

def proveedores_eliminar(id):
    if current_user.rol != "admin":
        return "No autorizado"
    p = Proveedor.query.get(id)
    db.session.delete(p)
    db.session.commit()
    return redirect("/proveedores")


#PRODUCTOS#

@app.route("/productos", methods=["GET", "POST"])

def productos():
    if request.method == "POST":
        nuevo = Producto(
            nombre=request.form["nombre"],
            descripcion=request.form["descripcion"],
            precio=request.form["precio"],
            stock=request.form["stock"]
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect("/productos")

    lista = Producto.query.all()
    return render_template("productos.html", productos=lista)

@app.route("/productos/eliminar/<int:id>")

def productos_eliminar(id):
    if current_user.rol != "admin":
        return "No autorizado"
    p = Producto.query.get(id)
    db.session.delete(p)
    db.session.commit()
    return redirect("/productos")


#COMPRAS#

@app.route("/compras", methods=["GET", "POST"])

def compras():
    if request.method == "POST":
        compra = Compra(
            producto_id=request.form["producto_id"],
            proveedor_id=request.form["proveedor_id"],
            cantidad=int(request.form["cantidad"]),
            fecha=date.today()
        )
        db.session.add(compra)

        prod = Producto.query.get(request.form["producto_id"])
        prod.stock += int(request.form["cantidad"])

        db.session.commit()
        return redirect("/compras")

    compras = Compra.query.all()
    productos = Producto.query.all()
    proveedores = Proveedor.query.all()
    return render_template("compras.html", compras=compras, productos=productos, proveedores=proveedores)


#VENTAS#

@app.route("/ventas", methods=["GET", "POST"])

def ventas():
    if request.method == "POST":
        venta = Venta(
            producto_id=request.form["producto_id"],
            cliente_id=request.form["cliente_id"],
            cantidad=int(request.form["cantidad"]),
            fecha=date.today()
        )
        db.session.add(venta)

        prod = Producto.query.get(request.form["producto_id"])
        prod.stock -= int(request.form["cantidad"])

        db.session.commit()
        return redirect("/ventas")

    ventas = Venta.query.all()
    productos = Producto.query.all()
    clientes = Cliente.query.all()
    return render_template("ventas.html", ventas=ventas, productos=productos, clientes=clientes)
