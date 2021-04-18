<h1 align="center" color="blue">Blogee - linguagem geradora de páginas de Blog</h1>
<h2 align="center" color="blue">TRABALHO 4 - COMPILADORES 1</h2>
<h3 align="center" color="blue"> Universidade Federal de São Carlos - Prof. Daniel Lucrédio </h2>
<br>
<h3 align="center" color="blue"> Autores:</h2>
<p align="center"> Luan V. Moraes da Silva - 744342 </p>
<p align="center"> Karolayne F. Arrais - 726460 </p>

## SUMÁRIO :pencil:

[O que é](#o-que-é) <br>
[Pré requisitos](#pré-requisitos) <br>
[Como utilizar](#como-utilizar) <br>
[Exemplos de uso](#exemplos-de-uso) <br>
[Gramática](#gramática) <br>
[Vídeo auxiliar](#vídeo-auxiliar)

## O QUE É?

Este projeto consiste na criação de uma linguagem e um compilador para a mesma, onde temos como entrada um arquivo descritivo no formato BGEE (especificado na nossa gramática) resultando como saída em uma página html com template de um blog.

## PRÉ REQUISITOS

Temos as seguintes dependências:

### 1. [python3](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe)

Você pode verificar se a instalação foi realizada com exito digitando no terminal:

```terminal
python3 --version
```

:warning: **ATENÇÃO** :warning: : se o comando `python3` não for reconhecido, substitua as ocorrências de `python3` neste tutorial por `python`, ou verifique se o comando `python3` está incluso nas variáveis de ambiente do seu sistema!

### 2. [textX](https://github.com/textX/textX)

Para instalar, você pode digitar no terminal:

```terminal
pip install textX[cli]
```

## COMO UTILIZAR

Com todos os pré requisitos atendidos, ou seja, todas dependências instaladas, basta clonar o repositório do diretório de sua escolha (caso tenha git instalado) ou então fazer o download do projeto compactado e extrair no diretório escolhido.

Abra o terminal na pasta onde se encontram os arquivos e então execute o comando

```terminal
python main.py ajuda
```

Como resultado você terá listado os possíveis comandos que poderá utilizar para executar o projeto, com seus respectivos exemplos.

### Analise Lexica, Sintatica e Semantica de um arquivo em `.bgee`

Para analisar um arquivo _blogee_, basta inserir no terminal o seguinte comando:

```terminal
python main.py analisar -i path_arquivo_para_analisar.bgee
```

Caso a linguagem esteja de acordo com a gramática será retornado sucesso, em qualquer outro caso será retornado falha e apresentado o erro encontrado.

### Geração de uma página HTML

Para gerar uma página HTML a partir da linguagem _blogee_, basta inserir no terminal:

```terminal
python main.py gerar -i path_arquivo_entrada.bgee -o path_arquivo_destino.html
```

Primeiro a analise da linguagem será feita, caso sucesso a página HTML será gerada no destino passado, caso falha o erro encontrado será apresentado e a geração não acontecerá!

## EXEMPLOS DE USO

O projeto contem pastas com exemplos de arquivos de entrada e saídas esperadas.

:white_check_mark:Em [casosTeste_corretos](https://github.com/moons2/compiladores-t4/tree/main/casosTeste_corretos), você encontrará arquivos BGEE seguindo a gramática estabelicida da linguagem, sem erros; com as saídas geradas após a execução para geração. <br>
:bug: Em [casosTeste_syntaxError](https://github.com/moons2/compiladores-t4/tree/main/casosTeste_syntaxError), você encontrará arquivos BGEE com erros sintátios e o resultado esperado no terminal após tentativa de geração da página html.<br>
:bug: Em [casosTeste_semanticError](https://github.com/moons2/compiladores-t4/tree/main/casosTeste_semanticError), você encontrará arquivos BGEE com erros semãnticos e o resultado esperado no terminal após tentativa de geração da página html. <br>

:warning: **ATENÇÃO** :warning: : ao passar uma imagem como argumento de capa, verifique se está realmente passando o caminho correto. Caso contrário, você terá erros que serão avisados após tentativa de análise ou geração. Nos casos de teste colocados como exemplo, todas as imagens estão presentes da pasta [images](https://github.com/moons2/compiladores-t4/tree/main/images)

## GRAMÁTICA

A gramática da linguagem Blogee desenvolvida, está definida no arquivo [blogee.tx](https://github.com/moons2/compiladores-t4/blob/main/blogee.tx)

## VÍDEO AUXILIAR

Segue o [link](https://youtu.be/ScuOSjoYFUo) de um breve vídeo mostrando a execução do projeto.
