import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Настройки прилоржения
        self.geometry("300x300")
        self.title("Calculator")
        padx = 5
        pady = 5
        button_size = 9999

        # Виджеты

        # Цифры
        self.entry = customtkinter.CTkEntry(self, width=button_size)
        self.entry.grid(row=0, column=0, columnspan=4, padx=padx, pady=pady)

        self.button_7 = customtkinter.CTkButton(self, text="7", width=button_size, height=button_size)
        self.button_7.grid(row=1, column=0, padx=padx, pady=pady)

        self.button_8 = customtkinter.CTkButton(self, text="8", width=button_size, height=button_size)
        self.button_8.grid(row=1, column=1, padx=padx, pady=pady)

        self.button_9 = customtkinter.CTkButton(self, text="9", width=button_size, height=button_size)
        self.button_9.grid(row=1, column=2, padx=padx, pady=pady)

        self.button_4 = customtkinter.CTkButton(self, text="4", width=button_size, height=button_size)
        self.button_4.grid(row=2, column=0, padx=padx, pady=pady)

        self.button_5 = customtkinter.CTkButton(self, text="5", width=button_size, height=button_size)
        self.button_5.grid(row=2, column=1, padx=padx, pady=pady)

        self.button_6 = customtkinter.CTkButton(self, text="6", width=button_size, height=button_size)
        self.button_6.grid(row=2, column=2, padx=padx, pady=pady)

        self.button_1 = customtkinter.CTkButton(self, text="1", width=button_size, height=button_size)
        self.button_1.grid(row=3, column=0, padx=padx, pady=pady)

        self.button_2 = customtkinter.CTkButton(self, text="2", width=button_size, height=button_size)
        self.button_2.grid(row=3, column=1, padx=padx, pady=pady)

        self.button_3 = customtkinter.CTkButton(self, text="3", width=button_size, height=button_size)
        self.button_3.grid(row=3, column=2, padx=padx, pady=pady)

        #Настройка сетки
        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(1, weight=10)
        self.grid_columnconfigure(2, weight=10)
        self.grid_columnconfigure(3, weight=10)

        self.grid_rowconfigure(1, weight=10)
        self.grid_rowconfigure(2, weight=10)
        self.grid_rowconfigure(3, weight=10)
        self.grid_rowconfigure(4, weight=10)

        # Функциональные кнопки
        self.button_plus = customtkinter.CTkButton(self, text="+", width=button_size, height=button_size)
        self.button_plus.grid(row=1, column=3, padx=padx, pady=pady)

        self.button_minus = customtkinter.CTkButton(self, text="-", width=button_size, height=button_size)
        self.button_minus.grid(row=2, column=3, padx=padx, pady=pady)

        self.button_multiplication = customtkinter.CTkButton(self, text="x", width=button_size, height=button_size)
        self.button_multiplication.grid(row=3, column=3, padx=padx, pady=pady)

        self.button_division = customtkinter.CTkButton(self, text="/", width=button_size, height=button_size)
        self.button_division.grid(row=4, column=3, padx=padx, pady=pady)

        self.button_division = customtkinter.CTkButton(self, text="=", width=button_size, height=button_size)
        self.button_division.grid(row=4, column=0, columnspan=3, padx=padx, pady=pady)

app = App()
app.mainloop()