import json
import datetime


def JSON2Dict(path: str, debug : bool = False) -> dict:
    #* Transforma um arquivo JSON em um dicionário Python

    with open(path, "r", encoding='utf-8') as calendario_JSON:
        dicionario = json.load(calendario_JSON)
    
    if debug:
        print("__Dicionário__\n")
        PrintarRecursivo(dicionario)

    return dicionario


def Dict2JSON(path: str, dict_cal: dict, debug : bool = False):
    #* Salva um dicionário Python para um arquivo JSON

    with open(path, "w", encoding='utf-8') as calendario_JSON:
        if len(dict_cal) > 0:
            calendario_JSON.truncate()
                
            if debug:
                print(dict_cal)

            json.dump(dict_cal, calendario_JSON, ensure_ascii=False)


def PrintarRecursivo(dict_cal: dict, indent: int = 0):
    #* Recursivamente verifica itens

    lvl = "|----"*indent

    for i in dict_cal:
        try:
            if isinstance(dict_cal[i], dict):
                print(lvl + i)

                PrintarRecursivo(dict_cal[i], indent=indent+1)

            else:
                print(lvl + f"{i} => {dict_cal[i]}")
        except:
            print("except on:", i)


def AtualizarRecursivo(new_entry: dict, dict_cal: dict, indent: int = 0, debug: bool = False) -> dict:
    #* Recursivamente verifica e atualiza itens de um dicionário

    if debug:
        print('__new_entry__')
        PrintarRecursivo(new_entry)
        print('\n__base_dict__')
        PrintarRecursivo(dict_cal)

    for i in new_entry:
        if i not in dict_cal:
            dict_cal[i] = new_entry[i]

        else:
            if new_entry[i] != dict_cal[i]:
                if isinstance(new_entry[i], dict):
                    AtualizarRecursivo(new_entry[i], dict_cal[i], indent=indent+1, debug=debug)

    if debug:
        print('\n\n__Final__')
        PrintarRecursivo(dict_cal)
    
    return dict_cal


def GetDatas(dict_cal : dict, debug : bool = False) -> tuple[dict[str, dict], dict[str, object]]:
    #* Retornar datas cadastradas

    datas = {}
    erros = {}

    for data in dict_cal:
        if isinstance(dict_cal[data], dict):
            try:
                dia : str = data[:2]
                mes : str = data[3:5]
                ano : str = data[6:]

                if 0 < int(dia) <= 31 and data[2] == '/'   \
                and 0 < int(mes) <= 12 and data[5] == '/'  \
                and 2000 < int(ano):
                    datas[data] = dict_cal[data]

                    if debug:
                        print(data)
                
                else:
                    erros[data] = dict_cal[data]

                    if debug:
                        print(f'\nData invalida em: `{data}` -> `{data} : {dict_cal[data]}`')
                    
            except:
                erros[data] = dict_cal[data] #! salva erros em indentação no nível de datas
                
                if debug:                        
                    print(f'\nFormato invalido em: `{data}` -> `{data} : {dict_cal[data]}`\n')

                    if isinstance(dict_cal[data], dict):
                        PrintarRecursivo(dict_cal[data])
        
        else:
            erros[data] = dict_cal[data] #! salva erros em indentação no nível de chaves-primárias

            if debug:
                print(f'\n{data} => não é Dicionário ({data} : {dict_cal[data]} -> {type(dict_cal[data])})')
    
    if debug:
        print("\n__Erros__")
        data = 0

        for indent in erros:
            print(f"{indent} : {erros[indent]}")

    listas = (datas, erros)
    
    return listas


def Add2JSON(pathJSON : str, dict_cal : dict, data : str, instancia : str = "Default", notas : str = "Default", debug : bool = False):
    dia : str = data[:2]
    mes : str = data[3:5]
    ano : str = data[6:]

    try:
        if not (                                   \
            0 < int(dia) <= 31 and data[2] == '/'  \
        and 0 < int(mes) <= 12 and data[5] == '/'  \
        and 2000 < int(ano)
        ):
            if debug:
                print(f"Data inválida: {dia}{data[2]}{mes}{data[5]}{ano}")

            return 3
        
    except:
        if debug:
            print("Erro no formato da data")

        return 2
    
    for chave in dict_cal:
        if debug:
            print("Chave:", chave)

        if isinstance(dict_cal[chave], dict):
            if data in dict_cal[chave]:
                if debug:
                    print("Chave já existe")
                    
                return 4


    dict_cal[data] = {"instância" : instancia, "notas" : notas}

    if debug:
        print(f'adicionado -> dict_cal["{data}"] : {{"instância" : {instancia}, "notas" : {notas}}}')
    
    Dict2JSON(pathJSON, dict_cal, debug=debug)

    return True


def RemoveFromJSON(pathJSON : str, dict_cal : dict, data : str, debug : bool = False):
    dia : str = data[:2]
    mes : str = data[3:5]
    ano : str = data[6:]

    try:
        if not (                                   \
            0 < int(dia) <= 31 and data[2] == '/'  \
        and 0 < int(mes) <= 12 and data[5] == '/'  \
        and 2000 < int(ano)
        ):
            if debug:
                print(f"Data inválida: {dia}{data[2]}{mes}{data[5]}{ano}")

            return 3
        
    except:
        if debug:
            print("Erro no formato da data")

        return 2
            
    for chave in dict_cal:
        if debug:
            print("Chave:", chave)
        
        if isinstance(dict_cal[chave], dict):
            if data in dict_cal:
                dados = dict_cal[data]

                if dados == dict_cal.pop(data, "data não existente"):
                    if debug:
                        print(f"Removido: {data}:{'{'}{dados}{'}'}")
        
                    Dict2JSON(pathJSON, dict_cal, debug=debug)

                    return True
        
    else:
        if debug:
            print("Data não cadastrada")
        
        return 5


def CalcularDiaOpt(dict_cal : dict, debug : bool = False) -> tuple[datetime.datetime, int]:
    #* Retorna o dia com mais espaço entre datas programadas para paradas

    atualidade_data = datetime.datetime.now()
    atualidade_str = atualidade_data.strftime("%d/%m/%Y")  #! convertendo para string no formato dia/mês/ano

    atualidade_e_datas = {**{atualidade_str : "Valor somente para para comparação"}, **GetDatas(dict_cal, debug=debug)[0]}

    sorted_datas = sorted(atualidade_e_datas, key=lambda data: Str2Data(data))

    datas_programadas = [Str2Data(data) for data in sorted_datas if Str2Data(data) > Str2Data(atualidade_str)]

    if debug:
        print('__Datas Programadas__')

        for data in datas_programadas:
            print(data)

    optimo = (0, 1)
    
    for index, data in enumerate(datas_programadas):
        if index + 1 < len(datas_programadas):
            diferenca = datas_programadas[index + 1] - data

            if diferenca.days > optimo[1]:
                optimo = (data + datetime.timedelta(days=diferenca.days/2), diferenca.days)

                if debug:
                    print("novo melhor->", Data2Str(optimo[0]), f": {optimo[1]} days between {Data2Str(data)} e {Data2Str(datas_programadas[index + 1])}")

    return optimo


def Data2Str(data : datetime.datetime) -> str:
    return datetime.datetime.strftime(data, "%d/%m/%Y")


def Str2Data(data : str) -> datetime.datetime:
    return datetime.datetime.strptime(data, "%d/%m/%Y")
