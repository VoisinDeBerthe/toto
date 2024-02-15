# https://www.sharemycode.fr/pythonj5

# lanceur de dés exo 4

# coding: utf-8
import tkinter as tk
from tkinter import font

import dice


class Window:
    def __init__(self):
        # exo 1
        self.root = tk.Tk()
        self.root.title('Lanceur de dé')

        window_width = 500
        window_height = 700

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}'
                           f'+{center_x}+{center_y}')
        self.root.iconbitmap("./d20.ico")

        # attributs
        self.fg_color = "#ffffff"
        self.bg_color = "#350259"
        self.dice = dice.Dice(20)
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Candara", size=12)

        # variable de controle
        self.var_lancer = tk.StringVar()
        self.var_lancer.set("")

        # exo 2
        self.label = tk.Label(
            self.root,
            text="Lanceur de dés",
            fg=self.fg_color,
            bg=self.bg_color,
            font=("Candara", 16, "bold")
        )

        self.btn_change_nb_faces = tk.Button(
            self.root,
            text="Changer le nombre de faces du dé",
            command=self.change_nb_faces_de,
            font=("Candara", 12)

        )

        self.btn_lancer_de = tk.Button(
            self.root,
            text="Lancer le dé",
            command=self.lancer_de,
            font=("Candara", 12)

        )

        self.label_resultat_lancer = tk.Label(
            self.root,
            textvariable=self.var_lancer,
            fg=self.fg_color,
            bg=self.bg_color,
            font=("Arial", 60, "bold")
        )

        # organisation des pack
        self.label.pack(fill="both", ipady=20)
        self.label_resultat_lancer.pack(side="bottom", fill="both", expand=True)

        self.btn_change_nb_faces.pack(side="left", expand=True, pady=20)
        self.btn_lancer_de.pack(side="right", expand=True, pady=20)

        self.root.mainloop()

    def change_nb_faces_de(self):
        self.dice.nb_faces = 6

    def lancer_de(self):
        resultat = str(self.dice.lancer())
        self.var_lancer.set(resultat)


if __name__ == '__main__':
    win = Window()


# lanceur de dé exo 3
# coding: utf-8
import tkinter as tk
from tkinter import font

import dice


class Window:
    def __init__(self):
        # exo 1
        self.root = tk.Tk()
        self.root.title('Lanceur de dé')

        window_width = 500
        window_height = 700

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}'
                           f'+{center_x}+{center_y}')
        self.root.iconbitmap("./d20.ico")

        # attributs
        self.fg_color = "#ffffff"
        self.bg_color = "#350259"
        self.dice = dice.Dice(20)
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Candara", size=12)

        # exo 2
        self.label = tk.Label(
            self.root,
            text="Lanceur de dés",
            fg=self.fg_color,
            bg=self.bg_color,
            font=("Candara", 16, "bold")
        )


        self.btn_change_nb_faces = tk.Button(
            self.root,
            text="Changer le nombre de faces du dé",
            command=self.change_nb_faces_de,

            font = ("Candara", 12)

        )

        self.btn_lancer_de = tk.Button(
            self.root,
            text="Lancer le dé",
            command=self.lancer_de,

            font = ("Candara", 12)

        )

        # organisation des pack
        self.label.pack(fill="both", ipady=20)
        self.btn_change_nb_faces.pack(side="left", expand=True, pady=20)
        self.btn_lancer_de.pack(side="right", expand=True, pady=20)

        self.root.mainloop()

    def change_nb_faces_de(self):
        self.dice.nb_faces = 6

    def lancer_de(self):
        pass

if __name__ == '__main__':
    win = Window()


# boutons 2
import tkinter as tk


#

class Window:
    def __init__(self):
        self.root = tk.Tk()

        self.btn = tk.Button(
            self.root,
            text="Hello",
            command=self.print_hello
        )

        self.btn.pack()

        self.root.mainloop()

    def print_hello(self):
        print("Hello !")


if __name__ == '__main__':
    win = Window()



# boutons 1

import tkinter as tk
#

class Window:
    def __init__(self):
        self.root = tk.Tk()

        self.btn = tk.Button(
            self.root,
            text="Fermer",
            command=self.root.quit
        )

        self.btn.pack()

        self.root.mainloop()


if __name__ == '__main__':
    win = Window()

# exo 2 lanceur de dés
# coding: utf-8
import tkinter as tk


class Window:
    def __init__(self):
        # exo 1
        self.root = tk.Tk()
        self.root.title('Lanceur de dé')

        window_width = 500
        window_height = 700

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}'
                           f'+{center_x}+{center_y}')
        self.root.iconbitmap("./d20.ico")

        self.fg_color = "#ffffff"
        self.bg_color = "#350259"
        # exo 2
        self.label = tk.Label(
            self.root,
            text="Lanceur de dés",
            fg=self.fg_color,
            bg=self.bg_color,
            font=("Candara", 16, "bold")
        )
        
        
        self.label.pack(fill="both", ipady=20)


        self.root.mainloop()


if __name__ == '__main__':
    win = Window()


# lanceur de dé étape 1
# coding: utf-8
import tkinter as tk


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Lanceur de dé')

        window_width = 500
        window_height = 700

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}'
                           f'+{center_x}+{center_y}')
        self.root.iconbitmap("./d20.ico")

        self.root.mainloop()


if __name__ == '__main__':
    win = Window()


# fenêtres 2

# coding: utf-8
import tkinter as tk

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Tkinter Window Demo')

        window_width = 900
        window_height = 700

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}'
                           f'+{center_x}+{center_y}')
        self.root.attributes('-alpha', 0.8)

        self.root.mainloop()



if __name__ == '__main__':
    win = Window()


# fenêtres 1
# coding: utf-8
import tkinter as tk

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Tkinter Window Demo')
        # title = self.root.title()
        # print(title)

        self.root.geometry('400x300+50+200')

        self.root.resizable(False, False)
        # self.root.iconbitmap("./logo.ico")
        self.root.mainloop()


if __name__ == '__main__':
    win = Window()


# tkinter hello world bonnes pratiques
import tkinter as tk

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="Hello, Tkinter")
        self.label.pack()

        self.root.mainloop()


if __name__ == '__main__':
    win = Window()



# tkinter version decouverte
import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hello, Tkinter")

label.pack()

root.mainloop()


# classe abstraite : démo
import abc


class Food(abc.ABC):
    @abc.abstractmethod
    def taste(self):
        pass


class FrenchFood(Food):
    def taste(self):
        print("Délicieux !")


class JapaneseFood(Food):
    def taste(self):
        print("Oishi ! ")


# food = Food() : TypeError: Can't instantiate abstract class Food with abstract method taste
fr_food = FrenchFood()
jp_food = JapaneseFood()
fr_food.taste()
jp_food.taste()
print(isinstance(fr_food, FrenchFood))
print(isinstance(fr_food, JapaneseFood))
print(isinstance(jp_food, FrenchFood))
print(isinstance(jp_food, JapaneseFood))


#générateurs en intention
import sys


ma_liste = [i for i in range(0, 1000) if i % 2 == 0]
print(sys.getsizeof(ma_liste))

ma_liste_2 = (i for i in range(0, 1000) if i % 2 == 0)
print(ma_liste_2, sys.getsizeof(ma_liste_2))

# générateurs démo
def my_generator():
    i = 12
    while i < 42:
        i += 10
        yield i
        # print("c'est reparti !")


for i in my_generator():
    print(i)


# itérateur démo
class MyIterator:
    def __init__(self):
        print("initialiation : 0")
        self.i = 0

    def __iter__(self):
        print("appel de __iter__, i = 12")
        self.i = 12
        return self

    def __next__(self):
        print("appel de __next__")
        self.i += 10
        if self.i > 42:
            raise StopIteration()
        return self.i


for i in MyIterator():
    print(i)
