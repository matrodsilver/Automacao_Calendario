import json


def json2dict(path) -> dict:
    # * Transforma um arquivo JSON em um dicionário Python
    with open(path, "r", encoding='utf-8') as calendario_JSON:
        dicionario = json.load(calendario_JSON)

    return dicionario


def dict2json(path, dict_cal):
    # * Salva um dicionário Python para um arquivo JSON
    with open(path, "w") as calendario_JSON:
        if len(dict_cal) > 0:
            dict_cal.update(dict_cal)
            print(dict_cal)
            calendario_JSON.truncate()
            json.dump(dict_cal, calendario_JSON)
