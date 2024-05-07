import random


def jugar():
    opciones = ['piedra', 'papel', 'tijeras']
    eleccion_usuario = input(
        "Elige tu jugada (piedra, papel o tijeras): ").lower()

    if eleccion_usuario not in opciones:
        print("Por favor, elige una opción válida.")
        return

    eleccion_maquina = random.choice(opciones)

    print("Elegiste:", eleccion_usuario)
    print("La computadora eligió:", eleccion_maquina)

    resultado = determinar_ganador(eleccion_usuario, eleccion_maquina)
    actualizar_resultados(resultado)


def determinar_ganador(usuario, maquina):
    if usuario == maquina:
        return "Empate"
    elif (usuario == 'piedra' and maquina == 'tijeras') or \
     (usuario == 'papel' and maquina == 'piedra') or \
     (usuario == 'tijeras' and maquina == 'papel'):
        return "Usuario"
    else:
        return "Maquina"


def actualizar_resultados(resultado):
    global ganadas_usuario, ganadas_maquina

    if resultado == "Usuario":
        ganadas_usuario += 1
        print("¡Ganaste, felicidades!")
    elif resultado == "Maquina":
        ganadas_maquina += 1
        print("¡La computadora ganó!")
    else:
        print("¡Empate!")

    print("Resultado del juego:")
    print("Usuario:", ganadas_usuario, "veces ganadas")
    print("Maquina:", ganadas_maquina, "veces ganadas")

    jugar_de_nuevo()


def jugar_de_nuevo():
    respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()

    if respuesta == 's':
        jugar()
    elif respuesta == 'n':
        print("¡Gracias por jugar!")
    else:
        print("Respuesta inválida.")
        jugar_de_nuevo()


# Inicialización de variables
ganadas_usuario = 0
ganadas_maquina = 0

print("¡Bienvenido a Piedra, Papel o Tijeras!")

# Comienza el juego
jugar()
