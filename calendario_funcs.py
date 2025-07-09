import json


def JSON2Dict(path: str) -> dict:
    #* Transforma um arquivo JSON em um dicionário Python

    with open(path, "r", encoding='utf-8') as calendario_JSON:
        dicionario = json.load(calendario_JSON)

    return dicionario


def Dict2JSON(path: str, dict_cal: dict):
    #* Salva um dicionário Python para um arquivo JSON

    with open(path, "w", encoding='utf-8') as calendario_JSON:
        if len(dict_cal) > 0:
            print(dict_cal)
            calendario_JSON.truncate()
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


def AtualizarRecursivo(new_entry: dict, dict_cal: dict, indent: int = 0, debug: bool = True) -> dict:
    #* Recursivamente verifica e atualiza itens

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


def GetDatas(dict_cal : dict, debug : bool = True) -> tuple[list[int], tuple[list, list]]:
    #* Retornar datas cadastradas

    datas = []
    erros = ([], [])

    for i in dict_cal:
        if isinstance(dict_cal[i], dict):
            for dia in dict_cal[i]:
                try:
                    if isinstance(int(dia[:2]), int) and dia[2] == '/'    \
                    and isinstance(int(dia[3:5]), int) and dia[5] == '/'  \
                    and isinstance(int(dia[6:]), int):
                        datas.append(dia)

                        if debug:
                            print(dia)
                    
                except:
                    erros[1].append(dia) #? salva erros em indentação no nível de datas

                    if debug:                        
                        print(f'\nErro em: {i} -> {dia}\n')

                        #. if isinstance(dict_cal[i], dict):
                        #.     PrintarRecursivo(dict_cal[i][dia])
        
        else:
            erros[0].append(i) #? salva erros em indentação no nível de chaves-primárias
            
            if debug:
                print(f'\n{i} => não é Dicionário ({i} => {dict_cal[i]} : {type(dict_cal[i])})')
    
    listas = (datas, erros)

    if debug:
        print("\n__Erros__")
        i = 0

        for indent in listas[1]:
            for key in indent:
                print(f"{"CHAVE:" if i == 0 else "DATA:"}", key)

            i+=1

    return listas
