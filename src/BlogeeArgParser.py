import sys
import argparse


class BlogeeArgParser:
    def __init__(self):
        self.arg_parser = argparse.ArgumentParser(
            description='Parser de argumentos do terminal')

        self.subparsers = self.arg_parser.add_subparsers(dest='comando')

        self.ajuda_parser = self.subparsers.add_parser(
            'ajuda', description='Parser para o subcomando de ajuda', help='Exibe as informações de utilização do programa')

        self.analisar_parser = self.subparsers.add_parser(
            'analisar', description='Parser para o subcomando de analise de código',
            help=('A partir do arquivo de entrada na linguagem Blogee, eh executado as analises lexica'
                  ', sintatica e semantica.'))

        self.analisar_parser.add_argument(
            '-i', '-input', type=str, nargs=1, help=('Caminho para o arquivo de entrada'), required=True)

        self.gerar_parser = self.subparsers.add_parser(
            'gerar', description='Parser para o subcomando de geração de código',
            help=('Dado um arquivo de entrada contendo o código na linguagem Blogee'
                  ' gera uma pagina de Blog pessoal em HTML com nome e localização definidos pelo parametro de saida.'))

        self.gerar_parser.add_argument('-i', '-input', type=str, nargs=1,
                                       help=('Caminho para o arquivo de entrada contendo o programa na linguagem Blogee'), required=True)

        self.gerar_parser.add_argument('-o', '-output', type=str, nargs=1,
                                       help=('Caminho para o arquivo de saida que '
                                             'contera o Blog pessoal HTML.'))
        self.testar_parser = self.subparsers.add_parser('testar', description='Parser para o subcomando de teste de casos de teste',
                                                        help=("Dado um um ou mais tipos de testes que se deseja executar "
                                                              "executa a análise ou a geração de código para o tipo desejado. Podem"
                                                              "ser: --sintatico, --semantico ou --geracao"))

        self.testar_parser.add_argument('--sintatico', help=('Executa os casos de teste para erros sintáticos'),
                                        action='store_true', required=False)

        self.testar_parser.add_argument('--semantico', help=('Executa os casos de teste para erros semânticos'),
                                        action='store_true', required=False)

        self.testar_parser.add_argument('--geracao', help=('Executa os casos de teste para geração de código'),
                                        action='store_true', required=False)

    def parse_args(self):
        return self.arg_parser.parse_args()
