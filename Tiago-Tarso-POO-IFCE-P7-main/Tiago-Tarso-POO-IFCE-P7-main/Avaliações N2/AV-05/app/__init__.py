from flask import Flask, request, url_for, redirect, render_template
from app.models.tables import Cliente
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

idg = 2
codigog = 2
clientes = [Cliente(1, "Tiago de Tarso", 1, '128.831.674-78', 'Pessoa Jurídica')]


@app.route("/")
def index():
    return render_template('index.html')

# função adicionar
@app.route("/inserir", methods=['GET', 'POST'])
def refactor():

    if request.method == 'POST':

        global idg
        global codigog
        idg += 1
        codigog += 100

        newcliente = Cliente(idg,
                             request.form['nome'],
                             codigog,
                             request.form['cpfcnpj'],
                             'Pessoa Jurídica')

        clientes.append(newcliente)

        return redirect(url_for('read'))

    return render_template('inserir.html')


@app.route("/read")
def read():

    return render_template('read.html', clientes=clientes)


@app.route("/atualizar", methods=['GET', 'POST'])
def atualiza():
    if request.method == 'POST':

        clienteId = int(request.form['id'])

        cliente = [c for c in clientes if clienteId == c.get_id()][0]

        cliente.set_nome(request.form['nome'])

        cliente.set_cnpjcpf(request.form['cpfcnpj'])

        return redirect(url_for('read'))

    return render_template('atualiza.html')


@app.route("/remover", methods=['GET', 'POST'])
def remover():
    if request.method == 'POST':

        clienteId = int(request.form['id'])

        cliente = [c for c in clientes if clienteId == c.get_id()][0]

        clientes.remove(cliente)

        return render_template('deletar.html', cliente=cliente)

    else:

        return render_template('deletar.html')
