from flask import Flask, request, render_template
import calendario_funcs as cf
import datetime, calendar


app = Flask(__name__)


debug = False

#' Carregar arquivo JSON para manipulação de dicionário
caminho_json = r".\calendario.json"
dict_calendario = cf.JSON2Dict(caminho_json, debug=debug)

#' Vars. Mêses
nome_meses = [
    "Index 0", 'Janeiro', "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
cores = {
    "laranja" : "#A50", "verde" : "#0A0", "azul" : "#00A", "marrom" : "#AA0", "roxo" : "#A0A", "amarelo" : "#0AA"}
atualidade = datetime.datetime.now()

#' List erros
erros = [
    "Nenhum dia disponível", None, "Erro no formato da data", "Data inválida", "Data já conta com parada", "Data sem parada cadastrada"]

#' Lambda Funcs.
paradas_programadas : dict = lambda mes: {d : dict_calendario[d] for d in cf.GetDatas(dict_calendario, debug=debug)[0] if cf.Str2Data(d).month == mes}
dias_de_paradas : list[int] = lambda mes : [int(data[:2]) for data in paradas_programadas(mes)]
instancias_conhecidas : list[str] = lambda mes: {int(chave[:2]) : chave for chave in paradas_programadas(mes) if int(chave[:2]) in dias_de_paradas(mes)}
dias_no_mes : int = lambda mes: calendar.monthrange(atualidade.year, mes)[1]
exibir_opt : str = lambda : cf.Data2Str(cf.CalcularDiaOpt(dict_calendario, debug=debug)[0])


@app.route("/")
def Calendario():
    try:
        exibir_mes = int(request.args.get("mes"))

    except:
        exibir_mes = atualidade.month
    
    if debug:
        print("Mês a exibir:", exibir_mes)
        print("paradas_programadas: ", paradas_programadas(exibir_mes))
    
    return render_template("calendario.html", dias_mes=dias_no_mes(exibir_mes), dias_de_paradas=dias_de_paradas(exibir_mes), paradas=paradas_programadas(exibir_mes), uniao=instancias_conhecidas(exibir_mes), optimo=exibir_opt(), mes_a_exibir=exibir_mes, atualidade=atualidade, meses=nome_meses, cores=cores)


@app.route("/calcular" , methods=["POST"])
def Calcular():
    global dict_calendario
    
    optimo = cf.CalcularDiaOpt(dict_calendario, debug=debug)[0]

    if optimo == 0:
        return render_template("erro.html", erros[0])

    instancia = request.form.get("instancia")
    notas = request.form.get("notas")

    if debug:
        print("Data:", optimo, "| Instancia:", instancia, "| notas:", notas)

    ## Atualizar JSON
    retorno = cf.Add2JSON(caminho_json, dict_calendario, cf.Data2Str(optimo),
                instancia if instancia is not None else 'Adição de instância: Calcular()',
                notas if notas is not None else 'Adição de notas: Calcular()',
                debug=debug)
    
    if retorno > 1:
        return render_template("erro.html", erro=erros[retorno])

    ## Atualizar dados
    exibir_mes = optimo.month
    dict_calendario = cf.JSON2Dict(caminho_json, debug=debug) # atualizar dicionário do calendário

    if debug:
        print("Mês a exibir:", exibir_mes)
        print("paradas_programadas: ", paradas_programadas(exibir_mes))

    return render_template("calendario.html", dias_mes=dias_no_mes(exibir_mes), dias_de_paradas=dias_de_paradas(exibir_mes), paradas=paradas_programadas(exibir_mes), uniao=instancias_conhecidas(exibir_mes), optimo=exibir_opt(), mes_a_exibir=exibir_mes, atualidade=atualidade, meses=nome_meses, cores=cores)


@app.route("/adicionar", methods=["POST"])
def Adicionar():
    global dict_calendario

    data = request.form.get("data")
    instancia = request.form.get("instancia")
    notas = request.form.get("notas")

    if debug:
        print("Data:", data, "| Instancia:", instancia, "| notas:", notas)

    ## Atualizar JSON
    retorno = cf.Add2JSON(caminho_json, dict_calendario, data,
                instancia if instancia is not None else 'Adição de instância: Adicionar()',
                notas if notas is not None else 'Adição de notas : Adicionar()',
                debug=debug)
    
    if retorno > 1:
        return render_template("erro.html", erro=erros[retorno])

    ## Atualizar dados
    dict_calendario = cf.JSON2Dict(caminho_json, debug=debug) # atualizar dicionário do calendário

    exibir_mes = int(data[3:5])

    if debug:
        print("Mês a exibir:", exibir_mes)
        print("paradas_programadas: ", paradas_programadas(exibir_mes))

    return render_template("calendario.html", dias_mes=dias_no_mes(exibir_mes), dias_de_paradas=dias_de_paradas(exibir_mes), paradas=paradas_programadas(exibir_mes), uniao=instancias_conhecidas(exibir_mes), optimo=exibir_opt(), mes_a_exibir=exibir_mes, atualidade=atualidade, meses=nome_meses, cores=cores)


@app.route("/excluir", methods=["POST"])
def Excluir():
    global dict_calendario

    data = request.form.get("data")

    if debug:
        print("\nData a excluir:", data)

    ## Atualizar JSON
    retorno = cf.RemoveFromJSON(caminho_json, dict_calendario, data)

    if retorno > 1:
        return render_template("erro.html", erro=erros[retorno])

    ## Atualizar dados
    dict_calendario = cf.JSON2Dict(caminho_json, debug=debug) # atualizar dicionário do calendário

    exibir_mes = int(data[3:5])

    paradas = paradas_programadas(exibir_mes)

    if debug:
        print("Mês a exibir:", exibir_mes)
        print("paradas_programadas: ", paradas)

    return render_template("calendario.html", dias_mes=dias_no_mes(exibir_mes), dias_de_paradas=dias_de_paradas(exibir_mes), paradas=paradas_programadas(exibir_mes), uniao=instancias_conhecidas(exibir_mes), optimo=exibir_opt(), mes_a_exibir=exibir_mes, atualidade=atualidade, meses=nome_meses, cores=cores)
