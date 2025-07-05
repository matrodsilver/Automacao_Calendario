import json
import time
import flask
import calendario_funcs as cf


app = flask.Flask(__name__)


caminho_json = "calendario.json"
novas_datas: dict = {"K": "V"}
dict_calendario = cf.json2dict(caminho_json)


@app.route("/")
def historico():
    dias_mes = [n for n in range(1, 31)] #! pegar dias do mês (i.e. datetime)

    paradas = [n for n in range(1, 6)] #! pegar paradas (i.e. puxar das chaves da base de dados)

    # for chave in dict_calendario:
    #     print(chave)

    return flask.render_template("calendario.html", dias_mes=dias_mes, paradas=paradas)


## Add
#• criar front interativo e rotas
#• desenvolver melhor lógica de comparação e optimização
#• verificar viabilidade de IA
#• add layout.html (se necessário)
