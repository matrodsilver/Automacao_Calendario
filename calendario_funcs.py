
import json


def json2dict(path: str) -> dict:
    #* Transforma um arquivo JSON em um dicionário Python

    with open(path, "r", encoding='utf-8') as calendario_JSON:
        dicionario = json.load(calendario_JSON)

    return dicionario


def dict2json(path: str, dict_cal: dict):
    #* Salva um dicionário Python para um arquivo JSON

    with open(path, "w", encoding='utf-8') as calendario_JSON:
        if len(dict_cal) > 0:
            # . dict_cal.update(dict_cal)
            print(dict_cal)
            calendario_JSON.truncate()
            json.dump(dict_cal, calendario_JSON, ensure_ascii=False)


def atualizarRecursivo(dict_cal: dict, new_entry: dict, indent: int = 0, debug: bool = True):
    #* Recursivamente verifica itens

    lvl = "|----"*indent

    for i in dict_cal:
        try:
            if type(dict_cal[i]) == dict:
                
                if debug:  #? debug
                    print(("\n" if indent == 0 else "") + lvl + i) #? END debug

                dict_cal = atualizarRecursivo(dict_cal[i], indent=indent+1, debug=debug)

            else:
                
                if debug:  #? debug
                    print(lvl + f"{i} => {dict_cal[i]}") #? END debug

        except:
            print("exception")


def atualizarRecursivoV2(new_entry: dict, dict_cal: dict, indent: int = 0, debug: bool = True):
    # * Recursivamente verifica e atualiza itens

    lvl = "|----"*indent

    for i in new_entry:

        if debug:  #? debug
            print(("\n" if indent == 0 else "") + lvl + i)  #? END debug

        if i not in dict_cal:
            dict_cal[i] = new_entry[i]

        else:
            if new_entry[i] != dict_cal[i]:
                if type(new_entry[i]) == dict:
                    atualizarRecursivo(new_entry[i], dict_cal[i], indent=indent+1, debug=debug)

                else:
                    if debug:  #? debug
                        print(lvl + f"{i} => {dict_cal[i]}")  #? END debug


if __name__ == "__main__":  #? debug test
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

    print(1, "\n", a, "\n", b, "\n")
    atualizarRecursivoV2(b, a)
    print(2, "\n", a, "\n", b, "\n")
