print("Merhaba dünya") # terminalde çalışır

#GUI = General User Interface
# tkinter

import tkinter as tk
from tkinter import ttk 

pencere = tk.Tk()
pencere.geometry("300x200")
pencere.title("Selamlama Sayfası")

mesaj = tk.Label(pencere,
                text="Merhaba,Dünya!",
                font=("Helvetica",20),
                bg="#066620")
mesaj.pack()

buton = ttk.Button(pencere,
                    text= "EXIT",
                    command=lambda: pencere.quit())
buton.pack()

pencere.mainloop()