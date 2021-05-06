from flask import Flask, request
import json

app = Flask("consultaPlaca")

with open("dadosplacas.json") as f:
    dados = json.load(f)

@app.route("/teste", methods=["GET"])
def teste():
    return {"Testes": "Echo"}


@app.route("/consultar", methods=["POST"])
def consultaPlaca():

    body = request.get_json()

    if("placa" not in body):
        return geraResponse(400, "O parametro Placa é obrigatorio")

    for placas in dados:
        if placa == placas["placa"]:
            unidade_gestora = placas["unidade_gestora"]
            categoria = placas["categoria"]
            tipo = placas["tipo"]
            propriedade = placas["propriedade"]
            marca = placas["marca"]
            modelo = placas["modelo"]
            cor = placas["cor"]
            ano_fabricacao = placas["ano_fabricacao"]
            ano_modelo = placas["ano_modelo"]
            chassi = placas["chassi"]
            renavam = placas["renavam"]
            placa = placas["placa"]
            localizacao = placas["localizacao"]
            situacao = placas["situacao"]

            retornar = [
                {
                    "unidade_gestora": unidade_gestora,
                    "categoria": categoria,
                    "tipo": tipo,
                    "propriedade": propriedade,
                    "marca": marca,
                    "modelo": modelo,
                    "cor": cor,
                    "ano_fabricacao": ano_fabricacao,
                    "ano_modelo": ano_modelo,
                    "chassi": chassi,
                    "renavam": renavam,
                    "placa": placa,
                    "localizacao": localizacao,
                    "situacao": situacao
                }
            ]
    
    return geraResponse(200, retornar)

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response

app.run()
