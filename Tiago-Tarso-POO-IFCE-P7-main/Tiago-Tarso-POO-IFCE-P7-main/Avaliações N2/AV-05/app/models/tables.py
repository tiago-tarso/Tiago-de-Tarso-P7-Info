# teste
class Cliente:

    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        self._id = id
        self._nome = nome
        self._codigo = codigo
        self._cnpjcpf = cnpjcpf
        self._tipo = tipo

    def str(self):

        string = "\nId={0} Codigo={1} Nome={2} CNPJ/CPF={3} Tipo={4}".format(self._id,
                                                                             self._codigo,
                                                                             self._nome,
                                                                             self._cnpjcpf,
                                                                             self._tipo)
        return string

    def get_id(self):
        return self._id

    def get_tipo(self):
        return self._tipo

    def get_codigo(self):
        return self._codigo

    def get_nome(self):
        return self._nome

    def get_cnpjcpf(self):
        return self._cnpjcpf

    def set_nome(self, nome):
        self._nome = nome

    def set_cnpjcpf(self, cnpjcpf):
        self._cnpjcpf = cnpjcpf
