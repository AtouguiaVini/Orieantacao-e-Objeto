import os
from modelos.restaurante import Restaurante

'''Código principal, que realiza a criação dos objetos com as notas'''
restaurante_praca = Restaurante('praça', 'gourmet', )
restaurante_mexicano = Restaurante('Mexican Food','Mexicana')
restaurante_japones = Restaurante('Japa', 'japonesa')

restaurante_mexicano.alternar_estado()
restaurante_japones.alternar_estado()

restaurante_praca.receber_avaliacao('Gui', 4)
restaurante_praca.receber_avaliacao('Lais', 3)
restaurante_praca.receber_avaliacao('Emy',5)

restaurante_mexicano.receber_avaliacao('Gusta', 2)
restaurante_mexicano.receber_avaliacao('Mauro', 5)
restaurante_mexicano.receber_avaliacao('Roger', 7)

restaurante_japones.receber_avaliacao('Laura', 8)
restaurante_japones.receber_avaliacao('Dina', 2)
restaurante_japones.receber_avaliacao('Carlos', 4)

def main():
    os.system('cls')
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()