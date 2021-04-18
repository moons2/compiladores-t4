from .Analyser import SemanticoAnalyser
import os


class BlogeeSemantico(SemanticoAnalyser):
    variaveis = {}

    ATT = ['blog', 'capa', 'autor', 'titulo', 'data', 'corpo', 'midias']

    OBG = ['blog', 'titulo', 'autor', 'data']

    def __init__(self, modelo):
        self.modelo = modelo
        self.parser = self.modelo._tx_parser

    def verificarTipo(self, atributo, argumento, linha):
        LIST = ['paragrafo', 'midia']
        IMG = ['capa']
        EXT = ['jpg', 'jpeg', 'png', 'bmp', 'svg']

        if not isinstance(argumento, str):
            self.showError(
                f"'{atributo}' deve receber uma cadeia de caracteres.", linha)
            return False
        elif atributo in IMG:

            # a atribuicao da img na gramatica é em relação a origen da gramatica
            # mas a verificação de existencia é em relação ao main
            if not os.path.isfile(argumento.replace('../', '')):
                # print(argumento)
                self.showError(
                    f"'{atributo}' deve receber um caminho valido ate uma imagem. ", linha)
                return False

            arquivo = argumento.split('.')[-1]

            if not arquivo in EXT:
                self.showError(
                    f"'{atributo}' deve ser uma imagem valida com uma das seguintes extensões: {', '.join(EXT)}.", linha)
                return False
        elif atributo in self.OBG:
            if not argumento.strip():
                self.showError(
                    f"'{atributo}' não deve ser vazio.", linha)
                return False

        return True

    def analisar(self):
        self.variaveis = {}

        no_errors = True

        for cmndo in self.modelo.comandos:
            no_errors = self.analisarComando(cmndo) and no_errors

        faltantes = set(self.OBG) - set(self.variaveis.keys())

        if(faltantes):
            for var in faltantes:
                self.showErrorUndeclared(var)

            no_errors = False

        if no_errors:
            opcionais = list((set(self.ATT) - set(self.OBG)) -
                             set(self.variaveis.keys()))

            for var in opcionais:
                self.variaveis[var] = ""

        # print(self.variaveis)

        return no_errors

    def analisarComando(self, Comando):
        nome_classe = type(Comando).__name__
        res = True

        if nome_classe == "ComandoDefina":
            res = self.analisarComandoDefina(Comando)
        elif nome_classe == "ComandoListe":
            res = self.analisarComandoListe(Comando)
        return res

    def analisarComandoDefina(self, Comando):

        linha, coluna = self.parser.pos_to_linecol(Comando._tx_position)

        if Comando.tipo in self.variaveis:
            self.showErrorDeclared(Comando.tipo, linha)
            return False

        tipo_correto = self.verificarTipo(
            Comando.tipo, Comando.argumento, linha)
        if not tipo_correto:
            return False

        self.variaveis[Comando.tipo] = Comando.argumento
        return True

    def analisarComandoListe(self, Comando):
        tipo = Comando.tipo
        res = True
        lista = []
        funcoes = {
            'corpo': self.analisarParagrafo,
            'midias': self.analisarMidia
        }

        linha, coluna = self.parser.pos_to_linecol(Comando._tx_position)

        if tipo in self.variaveis:
            self.showErrorDeclared(tipo, linha)
            res = False

        for elem in Comando.lista:
            aux = funcoes[tipo](elem, lista)
            if not aux:
                res = False
                continue

            lista.append(aux)

        if res:
            self.variaveis[tipo] = lista

        return res

    def analisarParagrafo(self, Paragrafo, lista_atual):
        linha, coluna = self.parser.pos_to_linecol(Paragrafo._tx_position)

        if not type(Paragrafo).__name__ == 'Paragrafo':  # não é paragrafo
            self.showError(
                f"Entrada fornecida estah fora do formato para 'paragrafo'", linha)
            return False

        texto = self.verificarTipo('texto', Paragrafo.texto, linha)

        if not texto:  # se houve algum problema
            return False

        # if '\n' in Paragrafo.texto:
        #    self.showError(
        #        f"Por favor nao pule linha dentro de um paragrafo", linha)
        #    return False

        return {'paragrafo': Paragrafo.texto}

    def analisarMidia(self, Midia, lista_atual):
        linha, coluna = self.parser.pos_to_linecol(Midia._tx_position)

        if not type(Midia).__name__ in ['Email', 'Insta', 'Face']:  # não é midia
            self.showError(
                f"Entrada fornecida estah fora do formato para 'midia'", linha)
            return False

        rede = Midia.rede

        res = False
        if(rede == 'email'):
            res = {'email': Midia.email}  # self.analisarEmail(Midia)
        elif rede == 'instagram':
            res = {'instagram': Midia.insta}  # self.analisarInsta(Midia)
        else:
            res = {'facebook': Midia.face}  # self.analisarFace(Midia)

        return res
