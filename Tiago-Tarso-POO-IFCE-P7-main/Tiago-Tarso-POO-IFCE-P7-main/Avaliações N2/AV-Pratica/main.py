from folha_pagamento import FolhaPagamento
from colaborador import Colaborador
from movimento_folha import MovimentoFolha
from tipomovimento import TipoMovimento


def main():
    # Objeto FP:
    fp = FolhaPagamento(9, 2019, 0, 0)
    # Objetos CL:
    cl01 = Colaborador("100", "Phelipe Cruz", "Av. Paulista, 9796", "(11)964357824",
                       "Liberdade", "60867-700", "124543556-89", 5000.00)
    cl02 = Colaborador("200", "Samir Duarte", "Av. Bela Cintra, 3146",
                       "(11)", "Aeroporto", "60530-020", "301789435-54",
                       2500.00)
    cl03 = Colaborador("300", "Gurmelina Castro Saraiva", "Av João Pessoa 1020",
                       "3235-1089", "Damas", "60330-090", "350245632-76", 3000.00)
    # Objetos MF:
    mf01 = MovimentoFolha(cl01, "Salario", 4500.00, TipoMovimento.P)
    mf02 = MovimentoFolha(cl01, "Plano Saúde", 1000.00, TipoMovimento.P)
    mf03 = MovimentoFolha(cl01, "Pensão", 600.00, TipoMovimento.D)
    mf04 = MovimentoFolha(cl02, "Salario", 2500.00, TipoMovimento.P)
    mf05 = MovimentoFolha(cl02, "Gratificação", 1000.00, TipoMovimento.P)
    mf06 = MovimentoFolha(cl02, "Faltas", 600.00, TipoMovimento.D)
    mf07 = MovimentoFolha(cl03, "Salario", 4500.00, TipoMovimento.P)
    mf08 = MovimentoFolha(cl03, "Plano Saúde", 1000.00, TipoMovimento.P)
    mf09 = MovimentoFolha(cl03, "Pensão", 600.00, TipoMovimento.D)

    fp.set_colaborador(cl01)
    fp.set_colaborador(cl02)
    fp.set_colaborador(cl03)

    fp.inserir_movimento_fp(mf01)
    fp.inserir_movimento_fp(mf02)
    fp.inserir_movimento_fp(mf03)
    fp.inserir_movimento_fp(mf04)
    fp.inserir_movimento_fp(mf05)
    fp.inserir_movimento_fp(mf06)
    fp.inserir_movimento_fp(mf07)
    fp.inserir_movimento_fp(mf08)
    fp.inserir_movimento_fp(mf09)

    cl01.inserir_movimentos_colab(mf01)
    cl01.inserir_movimentos_colab(mf02)
    cl01.inserir_movimentos_colab(mf03)
    cl02.inserir_movimentos_colab(mf04)
    cl02.inserir_movimentos_colab(mf05)
    cl02.inserir_movimentos_colab(mf06)
    cl03.inserir_movimentos_colab(mf07)
    cl03.inserir_movimentos_colab(mf08)
    cl03.inserir_movimentos_colab(mf09)

    cl01.calcular_salario()
    cl02.calcular_salario()
    cl03.calcular_salario()

    fp.calcular_folha()


if __name__ == '__main__':
    main()
