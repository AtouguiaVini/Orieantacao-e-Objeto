from modelos.avaliacao import Avaliacao

class Restaurante:

    '''Class aplicada para a criação de restaurantes '''
    restaurantes = []



    def __init__(self, nome, categoria):
        '''Inicializa a criação de restaurantes
        
        Parâmetros:
        - nome (str): Refere-se ao nome do restaurante
        - categoria (str): Refere-se ao tipo de restaurante criado
        - ativo (bool): Verificação de ativação do restaurante no app / como padrão, inicializa desativado
        - avaliação (list): Lista de avaliações de clientes.
        '''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Retorna uma representação em string para o objeto restaurante'''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Método da classe que retorna lista de restaurantes cadastrados'''
        print(f'{"Restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Avaliação".ljust(20)} | Ativo')
        for restaurante in cls.restaurantes:
            print(f'- {restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        '''Retorna um símbolo indicativo se o restaurante está ativo ou não'''
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        '''Alterna o estado do restaurante entre Ativado e Desativado (True or False)'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Cria a avaliação do restaurante e verifica se recebe notas
        
        Parâmetros:
        - cliente (str): Nome do cliente
        - nota (float): Nota do cliente
        '''
        if 0 < nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Calcula a média da nota do cliente, para exibição quando solicitado lista'''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media



