class Analyser():
    def showError(self, msg, line):
        print(f'Erro na linha {line}: {msg}')


class SemanticoAnalyser(Analyser):
    def showErrorDeclared(self, att, line):
        self.showError(f"'{att}' já definido anteriormente", linha)

    def showErrorUndeclared(self, att):
        print(f"Erro: atributo obrigatório '{att}' não declarado")
