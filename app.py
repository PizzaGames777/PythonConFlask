from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'

# 🔗 CONEXIÓN A POSTGRESQL (EDITÁ USUARIO Y CONTRASEÑA)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:gonfire7@localhost/vetcontrol'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Importar rutas al final para evitar import cycle
from routes import *

from models import Usuario

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))