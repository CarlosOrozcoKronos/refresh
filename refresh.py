import json

while True:
    # TODO peticion a BBDD

    response = None

    # TODO mockear el response

    data = None
    mensajes =[]
    with open("refreshMocker.json") as jsonFile:
        data = json.load(jsonFile)
    
    for element in data["mensajes"]:
        mensaje = [
            element["user"],
            element["timestamp"],
            element["txt"]
            ]
        mensajes.append(mensaje)

    # print(mensajes)
    
    # TODO generar JSON desde el response de BDD

    # TODO enviar JSON a FRONT

    # TODO esperar 1 segundo
