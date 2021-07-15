from teste.teste import Cliente
from teste import db

def instanciar():
    cl1 = Cliente(1,
                  'Tiago',
                  10,
                  '1472583690',
                  'P. Física')
    db.session.add(cl1)
    db.session.commit()
