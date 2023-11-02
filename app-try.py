import random
import string
import PySimpleGUI as sg

def generar_contrasena(longitud, incluir_mayusculas=True, incluir_simbolos=True):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    if not incluir_mayusculas:
        caracteres = ''.join(c for c in caracteres if c not in string.ascii_uppercase)
    if not incluir_simbolos:
        caracteres = ''.join(c for c in caracteres if c not in string.punctuation)
    
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def copiar_al_portapapeles(contrasena):
    sg.clipboard_set(contrasena)
    sg.popup("Contraseña copiada al portapapeles.")

def guardar_historial(contrasena):
    with open('historial_contraseñas.txt', 'a') as file:
        file.write(contrasena + '\n')

def obtener_preferencias():
    sg.theme("LightGrey1")

    layout = [
        [sg.Text("Generador de Contraseñas Seguras", font=("Helvetica", 18), justification="center", size=(40, 1))],
        [sg.Text("Longitud de la Contraseña"), sg.InputText(default_text="12", key="-LONGITUD-", size=(10, 1))],
        [sg.Checkbox("Incluir mayúsculas", default=True, key="-MAYUSCULAS-")],
        [sg.Checkbox("Incluir símbolos", default=True, key="-SIMBOLOS-")],
        [sg.Button("Generar", size=(10, 1)), sg.Button("Copiar al Portapapeles", key="-COPIAR-", size=(20, 1)), sg.Button("Guardar Contraseña", size=(15, 1))],
        [sg.Text("", size=(50, 1), key="-RESULTADO-", justification="center", font=("Helvetica", 14))],
        [sg.Text("", size=(50, 1), key="-FORTALEZA-", justification="center", font=("Helvetica", 12))],
    ]

    window = sg.Window("Generador de Contraseñas", layout, finalize=True, margins=(20, 20))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Salir":
            window.close()
            break

        if event == "Generar":
            try:
                longitud = int(values["-LONGITUD-"])
                incluir_mayusculas = values["-MAYUSCULAS-"]
                incluir_simbolos = values["-SIMBOLOS-"]
                contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_simbolos)
                window["-RESULTADO-"].update(f"Contraseña generada: {contrasena}")

                # Evaluar la fortaleza de la contraseña
                if longitud < 8:
                    fortaleza = "Débil"
                elif longitud < 12:
                    fortaleza = "Moderada"
                else:
                    fortaleza = "Fuerte"
                window["-FORTALEZA-"].update(f"Fortaleza: {fortaleza}")
            except ValueError:
                sg.popup_error("Por favor, ingresa una longitud válida.")

        if event == "-COPIAR-":
            contrasena_generada = window["-RESULTADO-"].get()
            if contrasena_generada:
                copiar_al_portapapeles(contrasena_generada)

        if event == "Guardar Contraseña":
            contrasena_generada = window["-RESULTADO-"].get()
            if contrasena_generada:
                guardar_historial(contrasena_generada)
                sg.popup("Contraseña guardada en el historial.")

if __name__ == "__main__":
    obtener_preferencias()
