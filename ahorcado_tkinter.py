# importamos
import tkinter as tk
from tkinter import messagebox
import random

# creamos la clase
class JuegoAhorcado:
    def __init__(self, root):
        # hacemos la ventana
        root.title("Le pendu")
        root.geometry("400x300")
        root.resizable(False, False)

        # variables generales
        self.letras_adivinadas = set()
        self.intentos_maximos = 6
        self.intentos_realizados = 0
        self.palabra_secreta = self.obtener_palabra_aleatoria()

        # etiquetas etc en la ventana
        enunciado = tk.Label(root, text="Devinez l'animal...")
        enunciado.pack(pady=30)

        self.etiqueta_palabra = tk.Label(root, text=self.obtener_palabra_oculta())
        self.etiqueta_palabra.pack(pady=10)

        uneletre = tk.Label(root, text="Entrez une lettre:")
        uneletre.pack(pady=5)

        self.entry_letra = tk.Entry(root)
        self.entry_letra.config(text="lettre")
        self.entry_letra.pack(pady=10)

        boton_adivinar = tk.Button(root, text="Deviner", command=self.adivinar_letra)
        boton_adivinar.pack(pady=10)

    # funciones
    def obtener_palabra_aleatoria(self):
        palabras = ["chien", "chat", "chameau", "rhinoceros", "zebre", "iguane", "requin"]
        return list(random.choice(palabras))

    def obtener_palabra_oculta(self):
        return " ".join([letra if letra in self.letras_adivinadas else "_" for letra in self.palabra_secreta])

    def adivinar_letra(self):
        letra = self.entry_letra.get().lower()

        # logica
        if letra in self.letras_adivinadas:
            messagebox.showinfo("Attention", "Vous avez déjà deviné cette lettre. Essaie un autre.")
        else:
            self.letras_adivinadas.add(letra)

            if letra not in self.palabra_secreta:
                self.intentos_realizados += 1
                messagebox.showinfo("Incorrect", f"La lettre '{letra}' n'est pas dans le mot. Tentatives restantes: {self.intentos_maximos - self.intentos_realizados}")
            else:
                messagebox.showinfo("Correct", f"La lettre '{letra}' est dans le mot.")

            palabra_oculta = self.obtener_palabra_oculta()
            self.etiqueta_palabra.config(text=palabra_oculta)

            if palabra_oculta.replace(" ", "") == "".join(self.palabra_secreta):
                messagebox.showinfo("Félicitations!", "Vous avez deviné le mot!")
                self.root.destroy()

            if self.intentos_realizados == self.intentos_maximos:
                messagebox.showinfo("Fin du jeu", f"Vous avez épuisé vos tentatives. Le mot était '{''.join(self.palabra_secreta)}'. ¡Tu as perdu!")
                self.root.destroy()

# inicio app
if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoAhorcado(root)
    root.mainloop()
