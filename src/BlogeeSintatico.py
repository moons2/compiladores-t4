from textx.exceptions import TextXSyntaxError, TextXSemanticError
from .Analyser import Analyser


class BlogeeSintatico(Analyser):
    def __init__(self, meta_modelo):
        self.meta_modelo = meta_modelo

    def analisar(self, arquivo):
        try:
            modelo = self.meta_modelo.model_from_file(arquivo)
        except TextXSyntaxError as err:
            parser = err.__context__.parser
            parser.position = err.__context__.position
            self.showError(
                f'sequencia nao reconhecida proxima a \'{parser.context()}\'', err.line)
            return False
        return modelo
