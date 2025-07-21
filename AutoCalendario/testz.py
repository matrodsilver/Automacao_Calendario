"""Tests File"""



## __Tests Arqvs__ ##

def StrMultiplication(n : int):
    print("/t"*n, "-> indent")

#. StrMultiplication(3)


def Recursividade():
    from calendario_funcs import AtualizarRecursivo

    entradas = {
        "paradas_programadas": {
            "04/08": {
                "instância": "Chiller",
                "notas": "Parada de um Chiller para manutenção, estimativa de 1 horas"},
            "05/08": {
                "instância": "MCAG-B1",
                "notas": "Parada do MCAG-B1 para manutenção, estimativa de 3 horas"
            },
            "key_indent1": {
                "key_indent2": {
                    "key_indent3": "value_indent3",
                    "key_indent3-2": "value_indent3-2",
                    "key_indent3-3": {
                        "key_indent4": "value_indent4"
                    }
                },
                "key_indent2-2": "value_indent2-2"
            },
        }
    }

    print(AtualizarRecursivo(entradas, debug=True))

#. Recursividade()


def AtualizarDados():
    entrada = {
        "paradas_programadas": {
            "04/08": {
                "instância": "Chiller",
                "notas": "Parada de um Chiller para manutenção, estimativa de 1 horas"},
            "05/08": {
                "instância": "MCAG-B1",
                "notas": "Parada do MCAG-B1 para manutenção, estimativa de 3 horas"
            },
            "key_indent1": {
                "key_indent2": {
                    "key_indent3": "value_indent3",
                    "key_indent3-2": "value_indent3-2",
                    "key_indent3-3": {
                        "key_indent4": "value_indent4"
                    }
                },
                "key_indent2-2": "value_indent2-2"
            },
        },

        "paradas_variáveis":
        {
            "key_indent2" : {
                "key_indent3": "value_indent3",

            }
        }
    }

    entrada2 = {
        "paradas_programadas": {
            "nova/data": {
                "instância": "ph i",
                "notas": "ph n"},
        },
        "novas_paradas" : "novos_valores"
    }

    for i in entrada2:
        if i not in entrada: #! se instância não existe na principal
            entrada[i] = entrada2[i]

        else: #! se instância já existe na principal
            ## --checagem de conflito--
            if entrada[i] == entrada2[i]:
                continue

            elif type(entrada2) == dict:
                pass

                #* recursividade *#
                for j in entrada2[i]:
                    if j not in entrada[i]:
                        entrada[i][j] = entrada2[i][j]

                    else:
                        pass

    print(entrada)

#. AtualizarDados()


def AtualizarDados2():
    from calendario_funcs import AtualizarRecursivo
    a = {
        "key_indent1": {
            "key_indent2": {
                "key_indent3": "value_indent3",
                "key_indent3-2": "value_indent3-2",
                "key_indent3-3": {
                    "key_indent4": "value_indent4"
                }}}}
    b = {
        "1": {
            "2": {
                "3": "4",
                "5": "6",
                "7": {
                    "8": "9"
                }}}}

    AtualizarRecursivo(b, a, debug=True)


    # # test Dict 2 JSON

    import calendario_funcs as cf

    dict_calendario = cf.JSON2Dict("./AutoCalendario/calendario.json", True)
    novas_datas = {
        "paradas_programadas": {
            "00/00":
            {
                "instância": "testInstancia",
                "notas": "testNotas"
            },
            "01/00":
            {
                "instância": "testInstancia",
                "notas": "testNotas"
            },
            "02/00":
            {
                "instância": "testInstancia",
                "notas": "testNotas"
            }
        }
    }

    for k in novas_datas:
        dict_calendario[k] = novas_datas[k]

    print(dict_calendario)

    for instancia in dict_calendario:
        instancia = sorted(instancia)

#. AtualizarDados2()


def testGetDatas():
    from calendario_funcs import JSON2Dict #, GetDatas

    dict_calendario = JSON2Dict("./calendario.json", True)

    # dados = GetDatas(dict_calendario)
    
    # datas = dados[0]
    # erros = dados[1]

    # for dia in datas:
    #     print(dia)
    # print("/n__Erros__")
    # print(erros)
    
    # for i in erros:
    #     print(f"CHAVE: {i} => DATA: {erros[i]}")

#. testGetDatas()



## __Tests Time__ ##

def TestGetTime():
    import time, calendar

    tempo = time.localtime()
    print(tempo)

    year = 2025
    month = 7
    
    days_in_month = calendar.monthrange(year, month)[1]
    days_in_year = 366 if calendar.isleap(year) else 365

    print(f"Number of days in `{calendar.month_name[month]}` `{year}` (day `{tempo.tm_yday}` of `{days_in_year}` days): `{days_in_month}`")

#. TestGetTime()


def DiasDiferenca():
    import datetime

    date_time = datetime.datetime.strptime("15/07/2025", "%d/%m/%Y") #! parsing string to time
    print(date_time.strftime("%d/%m/%Y")) #! parsing string to time

    specific_date = datetime.datetime.strptime("28/07/2025", "%d/%m/%Y")
    print(specific_date.strftime("%d/%m/%Y"))

    diferenca = specific_date - date_time

    print(diferenca.days)

#. DiasDiferenca()


def ChecarDataFutura():
    import datetime

    atualidade = datetime.datetime.now()
    comparar = datetime.datetime.strptime("15/07/2025", "%d/%m/%Y")

    print(comparar > atualidade)

#. ChecarDataFutura()


def CheckData():
    import datetime

    atualidade = datetime.datetime.now()

    print(atualidade)

#. CheckData()



## __Tests Fluxo__ ##
def testCalcularDiaOpt(debug : bool = True):
    from calendario_funcs import CalcularDiaOpt, JSON2Dict

    dict_calendario = JSON2Dict("./AutoCalendario/calendario.json", True)

    print(CalcularDiaOpt(dict_calendario, debug=True))

#. testCalcularDiaOpt()


def testAdd2JSON():
    from calendario_funcs import Add2JSON, JSON2Dict, Str2Data

    dict_calendario = JSON2Dict("./AutoCalendario/calendario.json", True)

    # dict_calendario = sorted(dict_calendario, key=lambda data: Str2Data(dict_calendario['paradas'][data]))

    # print(dict_calendario)

    Add2JSON(dict_calendario, "21/04/2025", debug=True)
#. testAdd2JSON()

a = {i:'1' for i in range(10)}

print(a)