#
# BLOGEE, Linguagem geradora de páginas de blogs
#
# UNIVERSIDADE FEDERAL DE SÃO CARLOS
#   COMPILADORES 1 - TRABALHO 4
#    prof: DANIEL LUCREDIO
#
# Autores:
#       Luan V. M. Silva - 744342
#       Karolayne Arrais - 726460
#


# TODO LIST:
#   - validar formato do dia, mes e ano da data (possivelmente alterar gramatica)
#   - possibilitar titulo simples no corpo
#   - toc na div direita
#   - centralizar qquer imagem na div capa
#   - tratar erro de arquivo passado via -i nao encontrado
#   - substituir imgs da logo por texto

from textx import metamodel_from_file
from src.BlogeeArgParser import BlogeeArgParser
from textx.exceptions import TextXSyntaxError, TextXSemanticError
from src.Analyser import Analyser
from src.BlogeeSintatico import BlogeeSintatico
from src.BlogeeSemantico import BlogeeSemantico
from src.BlogeeGerador import BlogeeGerador
import os
import sys
import argparse

GRAMMAR = "blogee.tx"

MSG_AJUDA = """
COMANDOS DISPONIVEIS
    [ajuda]
        descricao: imprime esta tela de ajuda
        ex:
            python main.py ajuda

    [analisar [-i | -input]]
        descricao: realiza a analise lexica, sintatica e 
        semantica da linguagem Blogee do arquivo de entrada
        ex:
            python main.py analisar -i meuArquivo.bgee
    
    [gerar [[-i | -input] | [-o | -output]]]
        descricao: dado o caminho ate o arquivo de entrada (flag -i)
        e o caminho destino de saida, realiza analise lexica, sintatica
        e semantica, em caso de sucesso gera-se o blog pessoal em HTML.
        ex:
            python main.py gerar -i inputFile.bgee -o outputFile.html
    
    [testar [--sintatico] [--semantico] [--geracao]]
        descricao: executa os casos de teste presentes em 'casos_de_teste'
        de a flag informada
"""


class Blogee():
    gramatica = GRAMMAR

    def __init__(self, argumentos):
        self.args = argumentos

    def executar(self):
        comando = self.args.comando

        if comando == 'analisar' or comando == 'gerar':
            # print(self.args)

            self.grammar_file = self.args.i[0]

            if not os.path.isfile(self.grammar_file):
                print(
                    f'Arquivo com a linguagem destino nao encontrado, por favor verifique o nome e a extensão!\nNome: {self.grammar_file}')
                return False

            self.meta_modelo = metamodel_from_file(self.gramatica)

            if comando == 'analisar':
                self.analisar()
            else:
                self.output = self.args.o[0]
                self.gerar()
        elif comando == 'testar':
            self.meta_modelo = metamodel_from_file(self.gramatica)

            if self.args.sintatico:
                caminho = 'casos_de_teste/erros_sintaticos/'
                print(f'----------ANALISE SINTATICA----------')
                for arquivo in os.listdir(caminho):
                    print(f'----------{arquivo}----------')
                    self.arquivo = os.path.join(caminho, arquivo)
                    self.analisar()

            if self.args.semantico:
                caminho = 'casos_de_teste/erros_semanticos/'
                print(f'----------ANALISE SEMANTICA----------')
                for arquivo in os.listdir(caminho):
                    print(f'----------{arquivo}----------')
                    self.arquivo = os.path.join(caminho, arquivo)
                    self.analisar()

            if self.args.geracao:
                caminho = 'casos_de_teste/corretos/'
                print(f'----------GERACAO----------')
                for arquivo in os.listdir(caminho):
                    print(f'----------{arquivo}----------')
                    self.arquivo = os.path.join(caminho, arquivo)
                    self.arquivo = os.path.join(
                        'saida/corretos/', f'{arquivo}_blogee.html')
                    self.gerar()

        elif comando == 'ajuda':
            print(MSG_AJUDA)

    def analisar(self):
        # print("Voce invocou o metodo analisador!")

        self.modelo = False

        sintatico = BlogeeSintatico(self.meta_modelo)
        self.modelo = sintatico.analisar(self.grammar_file)

        semantica = False
        if self.modelo:
            semantico = BlogeeSemantico(self.modelo)
            semantica = semantico.analisar()

        if semantica:
            print('Analise realizada com exito!')
            return semantico.variaveis
        else:
            print('Analise finalizada sem exito!')
            return False

    def gerar(self):
        # print("Voce invocou o metodo gerador!")
        variaveis = self.analisar()

        if variaveis:
            gerador = BlogeeGerador(variaveis, self.output)
            gerador.gerar()
            print('Geracao concluida com exito!')
        else:
            print('Falha na Geracao, verifique o que ocorreu errado!')


def main():
    arg_parser = BlogeeArgParser()
    args = arg_parser.parse_args()
    blogee = Blogee(args)
    blogee.executar()

    # print(args.comando)
    # print(MSG_AJUDA)

    # meta_modelo = metamodel_from_file(GRAMMAR)

    # try:
    # Cria o modelo a partir do meta modelo
    # meta_modelo.model_from_file(args[1])
    # except TextXSyntaxError as e:  # Erro léxico/ sintático
    # parser = e.__context__.parser  # Instância do parser do textX
    # parser.position = e.__context__.position  # Posição da ocorrência do erro
    # analisador = Analyser()
    # analisador.showError(
    #    f"sequencia nao reconhecida proximo a '{parser.context()}'", e.line)

    # blogee = Blogee(args)


if __name__ == '__main__':
    main()
