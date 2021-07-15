from teste import create_teste
from teste.views import instanciar

teste = create_teste()

if __name__ == '__main__':
    teste.run(debug=True)
    instanciar()
