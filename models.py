from app import db
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    usuario = db.Column(db.String(50), unique=True)
    contraseña = db.Column(db.String(100))
    rol = db.Column(db.String(20))  # admin o vendedor

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(200))

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    contacto = db.Column(db.String(100))

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Float)
    stock = db.Column(db.Integer)
    

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'))
    cantidad = db.Column(db.Integer)
    fecha = db.Column(db.Date)

    # Relaciones
    producto = db.relationship("Producto", backref="compras")
    proveedor = db.relationship("Proveedor", backref="compras")


class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    cantidad = db.Column(db.Integer)
    fecha = db.Column(db.Date)

    # Relaciones
    producto = db.relationship("Producto", backref="ventas")
    cliente = db.relationship("Cliente", backref="ventas")