from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_solicitar_valores.db'
db = SQLAlchemy(app)

# requisiçoes de entrada (banco api alyson)
class Usuario(db.Model):
    cpf = db.Column(db.Integer, primary_key=True)
    data_de_nascimento = db.Column(db.Integer, nullable=False)


# tabelas no banco
with app.app_context():
    db.create_all()
    print("é os guri do gremio")
