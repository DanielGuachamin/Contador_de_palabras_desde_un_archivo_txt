def abrirLeertxt():
  #La estructura try permite que el programa funcione aunque
  #haya errores y mostrara una notificacion
    try:
        archi = open("Book4TheGobletofFire.txt", encoding='utf-8')
        palabrasText = archi.read()
        caracApart = ',;.-¿”!“¡()—:/?\n|\t"'
        print("\tBienvenido al contador de palabras de un archivo en formato .txt\n")
        for _ in caracApart:
            palabrasText = palabrasText.replace(_, "")

        palabrasText = palabrasText.lower()
        palabras = palabrasText.split(" ")
        #declaro conjunto de nombre freq para la frecuencia de las palabras
        freq = {}
        for palabra in palabras:
            if palabra in freq:
                freq[palabra] += 1
            else:
                freq[palabra] = 1
        for palabra in freq:
            frecuencia = freq[palabra]
            print(f"({palabra},{frecuencia})")
        archi.close()

    except FileNotFoundError:
        print("El archivo .txt no pudo abrirse con éxito")
#Llama a la funcion definida
abrirLeertxt()