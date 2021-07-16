import datetime
from . import db


class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    codigo = db.Column(db.Integer)
    cnpjcpf = db.Column(db.String(150))
    tipo = db.Column(db.String(150))

    notas = db.relationship("NotaFiscal")

    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        self.id = id
        self.nome = nome
        self.codigo = codigo
        self.cnpjcpf = cnpjcpf
        self.tipo = tipo

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "codigo": self.codigo, "cnpjcpf": self.cnpjcpf, "tipo": self.tipo}

    def str(self):
        string = "\nId={4} Codigo={2} Nome={3} CNPJ/CPF={1} Tipo={0}".format(self.tipo, self.cnpjcpf, self.codigo,
                                                                             self.nome, self.id)
        return string


class ItemNotaFiscal(db.Model):
    __tablename__ = 'itens'

    id = db.Column(db.Integer, primary_key=True)
    sequencial = db.Column(db.Integer)
    quantidade = db.Column(db.Integer)

    produtos = db.relationship("Produto")
    nota_id = db.Column(db.Integer, db.ForeignKey('notas.id'))

    def __init__(self, id, sequencial, quantidade, produto):
        self.id = id
        self.sequencial = sequencial
        self.quantidade = quantidade
        self.produto = produto
        self.descricao = self.produto['descricao']
        self.valorUnitario = self.produto['valorUnitario']
        self.valorItem = float(self.quantidade * self.valorUnitario)

    def to_json(self):
        return {"id": self.id, "sequencial": self.sequencial, "quantidade": self.quantidade,
                "produto": self.produto, "descricao": self.descricao, "valorUnitario": self.valorUnitario,
                "valorItem": self.valorItem}

    def str(self):
        string = "\nId={5} Sequencial={4} Quantidade={3} Produto={2} Valor Unitario={1} Valor Item={0}".format(
            self.valorItem,
            self.valorUnitario,
            self.descricao,
            self.quantidade,
            self.sequencial,
            self.id)
        return string

    def get_sequencial(self):
        seq = str(self.sequencial)
        if len(seq) > 2:
            return seq

        elif len(seq) > 1:
            return f'0{seq}'

        return f'00{seq}'


class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)
    descricao = db.Column(db.String(150))
    valorUnitario = db.Column(db.Float)

    item_id = db.Column(db.Integer, db.ForeignKey('itens.id'))

    def __init__(self, id, codigo, descricao, valorUnitario):
        self.id = id
        self.codigo = codigo
        self.descricao = descricao
        self.valorUnitario = valorUnitario

    def to_json(self):
        return {"id": self.id, "codigo": self.codigo, "descricao": self.descricao, "valorUnitario": self.valorUnitario}

    def str(self):
        string = "\nId={3} Codigo={2} Descricao={1} Valor Unitario={0}".format(self.valorUnitario, self.descricao,
                                                                               self.codigo, self.id)
        return string


class NotaFiscal(db.Model):
    __tablename__ = 'notas'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(150))

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    itens = db.relationship("ItemNotaFiscal")

    def __init__(self, id, codigo, cliente, lista_itens=None):
        self.id = id
        self.codigo = codigo
        self.cliente = cliente
        self.lista_itens = lista_itens
        self.data = datetime.datetime.now()
        self.itens = []
        self.valorNota = 0.0

    def str_itens(self):
        if self.lista_itens is None:
            itens_json = [item for item in self.itens]
            return itens_json
        else:
            return self.lista_itens

    def to_json(self):
        return {"id": self.id, "codigo": self.codigo, "cliente": self.cliente, "itens": self.str_itens(),
                "data": self.data_nota(), "valorNota": self.valorNota}

    def set_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.cliente = cliente

    def data_nota(self):
        lista_data_e_hora = str(self.data).split()  # Separa o resultado de "datetime.datetime.now()" numa lista
        # com 2 elementos, a data e a hora
        data_lista = lista_data_e_hora[0].split('-')  # Divide em strings apenas a data, primeiro elemento da lista
        # acima
        data_final_nota = f'{data_lista[2]}/{data_lista[1]}/{data_lista[0]}'  # Ordena a data na nossa ordem padrão
        return data_final_nota  # Retorna a data formatada

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total_nota(self, controle=False):
        valor = 0.0
        for item in self.itens:
            valor = valor + item["valorItem"]
        self.valorNota = valor
        if controle == True:
            return valor

    def get_sequencial(self, item):
        seq = str(item['sequencial'])
        if len(seq) > 2:
            return seq

        elif len(seq) > 1:
            return f'0{seq}'

        return f'00{seq}'

    def imprimir_nota_fiscal(self):
        """
        Formatação final da nota fiscal, a string completa de saída. Método principal do programa.
        """
        linhas = '-' * 111

        formatacao_nota = '{}\n' \
                          'NOTA FISCAL{:>100}\n' \
                          'Cliente:{:>6}{:>4}Nome: {}\n' \
                          'CPF/CNPJ: {}\n' \
                          '{}\n' \
                          'ITENS\n' \
                          '{}\n' \
                          'Seq{:>3}Descricao{:>52}QTD{:>7}Valor Unit{:19}Preço\n' \
                          '{}  {}    {}     {}     {}'.format(linhas,
                                                              self.data_nota(),
                                                              self.cliente['codigo'], ' ', self.cliente['nome'],
                                                              self.cliente['cnpjcpf'],
                                                              linhas,
                                                              linhas,
                                                              ' ', ' ', ' ', ' ',
                                                              '-' * 4, '-' * 56, '-' * 5, '-' * 12, '-' * 18)

        if len(self.itens) > 0:  # Adicionando e formatando os itens, elementos finais da nota
            for item_nota in self.itens:
                formatacao_nota += '\n\n{}{:>3}{}'.format(self.get_sequencial(item_nota), ' ', item_nota['descricao'])
                formatacao_nota += ' ' * (60 - len(item_nota['descricao']))  # Controlando de acordo com a descrição
                formatacao_nota += '{:.2f}             {:.2f}                  {:.2f}'.format(
                    item_nota['quantidade'], item_nota['valorUnitario'],
                    item_nota['valorItem'])

        formatacao_nota += '\n{}\nValor Total: {:.2f}'.format(linhas, self.valorNota)
        return formatacao_nota

