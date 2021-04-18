import os


class BlogeeGerador():
    def __init__(self, variaveis, saida):
        self.variaveis = variaveis
        self.saida = saida

    # gerar
    # params: nao recebe parametros
    # return: nao possui retorno
    # este metodos percorre o template.html fazendo a substituição apropriada
    # de acordo com a chave contida em variaveis
    def gerar(self):

        parent = os.path.join(os.path.dirname(__file__), '..')

        with open(os.path.join(parent, "template.html"), encoding='utf-8') as html_file:
            html = html_file.read()
            for key in self.variaveis.keys():  # retorna todas as chaves contidas no obj 'variaveis'
                html = html.replace(
                    "{{ " + key + " }}", self.traduzir2HTML(key, self.variaveis[key]))

            final = open(self.saida, "w")
            final.write(html)
            final.close()

    # traduzir2HTML
    # params: a chave (tipo) e valor contidos em variáveis
    # return: retorna o valor devidamente interpretado em HTML
    def traduzir2HTML(self, tipo, valor):

        # por default, o valor atomico eh uma cadeia de caracteres
        ret = str(valor)

        if tipo == 'corpo':
            ret = self.traduzCorpo(valor)
        elif tipo == 'midias':
            ret = self.traduzMidia(valor)

        return ret

    def traduzCorpo(self, paragrafos):

        if paragrafos == "" or not len(paragrafos):
            return "<h3> Redija ao menos um paragrafo !</h3>"

        ret = []

        for paragrafo in paragrafos:
            ret.append(f"<p>{paragrafo['paragrafo']}</p>")

        return ''.join(ret)

    def traduzMidia(self, Midias):

        if Midias == "" or not len(Midias):
            return "<h3> Nenhuma mídia adicionada!</h3>"

        ret = []

        for midia in Midias:
            if 'email' in midia.keys():
                ret.append(
                    f"<li><span class=\"email-icon icon\"></span><span><a href=\"{midia['email']}\">{midia['email']}</a></span></li>")
            elif 'instagram' in midia.keys():
                ret.append(
                    f"<li><span class=\"insta-icon icon\"></span><span><a href=\"https://www.instagram.com/{midia['instagram']}\">{midia['instagram']}</a></span></li>")
            elif 'facebook' in midia.keys():
                ret.append(
                    f"<li><span class=\"face-icon icon\"></span><span><a href=\"https://pt-br.facebook.com/{midia['facebook']}\">{midia['facebook']}</a></span></li>")

        return ''.join(ret)
