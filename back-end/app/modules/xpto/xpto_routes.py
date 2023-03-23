from flask import Blueprint,request

xpto_routes = Blueprint("xpto", __name__)

@xpto_routes.route("/api/v1/xpto")
def get_xpto():
  print("Acessando a rota do Get do xpto")
  return {"msg": "Essa e a nossa primeira rota"}

@xpto_routes.route("/api/v1/xpto", methods=["POST"])
def salvar_xpto():
  print("--------- HEADER ----------")
  print(request.headers)
  print("--------- JSON ----------")
  print(request.json)

  if "xpto" in request.json:
    if "nome" in request.json["xpto"]:
      return {"msg":f"xpto {request.json['xpto']['nome']} salvo com sucesso"}
  else:
    return {"msg": "Não foi encontrado o campo o nome na requisição"},500