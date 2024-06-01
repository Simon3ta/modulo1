while True:
    word = input("escribe palabras en francés que no entiendas (toda la palabra en minúscula):")
    diccionario = {
        "oui":  "Sí",
        "merci":  "Gracias",
        "de rien":  "De nada",
        "bonjour": "¡Hola!",
        "au revoir":  "¡Adiós!",
        "Enchanté":  "Encantado o gusto conocerte",
        "bienvenue":  "Bienvenido",
        "comment allez-vous":  "¿Cómo estás tú?",
        "á bientot":  "Hasta pronto",
        "s’il vous plaît":  "Por favor",
    }
    if word in diccionario.keys():
        print("la palabra es:")
        print(diccionario[word])
        print("----------------------------")
    else:
        print("la palabra no esta en este diccionario")
        print("----------------------------")
