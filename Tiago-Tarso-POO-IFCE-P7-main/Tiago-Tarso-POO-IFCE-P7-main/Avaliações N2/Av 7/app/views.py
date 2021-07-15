from app.app import Cliente
from app import db

def instanciar():
    cl1 = Cliente(1,
                  'Tiago de Tarso',
                  4,
                  '03924179360',
                  'Pessoa Física')
    db.session.add(cl1)
    db.session.commit()
