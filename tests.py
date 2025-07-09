
# # str multiplication

# for n in range(10):
#     print("\t"*n, "t")


# # test calendario_funcs. recursividade

# import calendario_funcs as cf

# caminho_json = "./AutoCalendario/calendario.json"

# entradas = {
#     "paradas_programadas": {
#         "04/08": {
#             "instância": "Chiller",
#             "notas": "Parada de um Chiller para manutenção, estimativa de 1 horas"},
#         "05/08": {
#             "instância": "MCAG-B1",
#             "notas": "Parada do MCAG-B1 para manutenção, estimativa de 3 horas"
#         },
#         "key_indent1": {
#             "key_indent2": {
#                 "key_indent3": "value_indent3",
#                 "key_indent3-2": "value_indent3-2",
#                 "key_indent3-3": {
#                     "key_indent4": "value_indent4"
#                 }
#             },
#             "key_indent2-2": "value_indent2-2"
#         },
#     }
# }

# print(cf.atualizarRecursivo(entradas, debug=True))


# # test atualizar dados

# entrada = {
#     "paradas_programadas": {
#         "04/08": {
#             "instância": "Chiller",
#             "notas": "Parada de um Chiller para manutenção, estimativa de 1 horas"},
#         "05/08": {
#             "instância": "MCAG-B1",
#             "notas": "Parada do MCAG-B1 para manutenção, estimativa de 3 horas"
#         },
#         "key_indent1": {
#             "key_indent2": {
#                 "key_indent3": "value_indent3",
#                 "key_indent3-2": "value_indent3-2",
#                 "key_indent3-3": {
#                     "key_indent4": "value_indent4"
#                 }
#             },
#             "key_indent2-2": "value_indent2-2"
#         },
#     },

#     "paradas_variáveis":
#     {
#         "key_indent2" : {
#             "key_indent3": "value_indent3",

#         }
#     }
# }

# entrada2 = {
#     "paradas_programadas": {
#         "nova/data": {
#             "instância": "ph i",
#             "notas": "ph n"},
#     },
#     "novas_paradas" : "novos_valores"
# }

# for i in entrada2:
#     if i not in entrada: #! se instância não existe na principal
#         entrada[i] = entrada2[i]

#     else: #! se instância já existe na principal
#         ## --checagem de conflito--
#         if entrada[i] == entrada2[i]:
#             continue

#         elif type(entrada2) == dict:
#             pass

#             #* recursividade *#
#             for j in entrada2[i]:
#                 if j not in entrada[i]:
#                     entrada[i][j] = entrada2[i][j]

#                 else:
#                     pass

# print(entrada)


# # test 2 atualizar dados

# import calendario_funcs as cf
# a = {
#     "key_indent1": {
#         "key_indent2": {
#             "key_indent3": "value_indent3",
#             "key_indent3-2": "value_indent3-2",
#             "key_indent3-3": {
#                 "key_indent4": "value_indent4"
#             }}}}
# b = {
#     "1": {
#         "2": {
#             "3": "4",
#             "5": "6",
#             "7": {
#                 "8": "9"
#             }}}}

# cf.AtualizarRecursivo(b, a)


# # # test Dict 2 JSON

# import calendario_funcs as cf

# dict_calendario = cf.JSON2Dict("./AutoCalendario/calendario.json")
# novas_datas = {
#     "paradas_programadas": {
#         "00/00":
#         {
#             "instância": "testInstancia",
#             "notas": "testNotas"
#         },
#         "01/00":
#         {
#             "instância": "testInstancia",
#             "notas": "testNotas"
#         },
#         "02/00":
#         {
#             "instância": "testInstancia",
#             "notas": "testNotas"
#         }
#     }
# }

# for k in novas_datas:
#     dict_calendario[k] = novas_datas[k]

# print(dict_calendario)

# for instancia in dict_calendario:
#     instancia = sorted(instancia)


# # test GetDatas

import calendario_funcs as cf

dict_calendario = cf.JSON2Dict("./AutoCalendario/calendario.json")

retorno = cf.GetDatas(dict_calendario)
