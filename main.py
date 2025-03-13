import customtkinter
import moex

class App(customtkinter.CTk):
    
    #todo Функция открытия истории
    def history(self):
        print(":)")
        
    # Функция "Обычный калькулятор"
    def calc(self):
        self.entry = customtkinter.CTkEntry(self, width=self.button_size, state = "disabled")
        self.entry.grid(row=1, column=0, columnspan=4, padx=self.padx, pady=self.pady)

        self.button_7 = customtkinter.CTkButton(self, text="7", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_7.cget("text")))
        self.button_7.grid(row=2, column=0, padx=self.padx, pady=self.pady)

        self.button_8 = customtkinter.CTkButton(self, text="8", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_8.cget("text")))
        self.button_8.grid(row=2, column=1, padx=self.padx, pady=self.pady)

        self.button_9 = customtkinter.CTkButton(self, text="9", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_9.cget("text")))
        self.button_9.grid(row=2, column=2, padx=self.padx, pady=self.pady)

        self.button_4 = customtkinter.CTkButton(self, text="4", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_4.cget("text")))
        self.button_4.grid(row=3, column=0, padx=self.padx, pady=self.pady)

        self.button_5 = customtkinter.CTkButton(self, text="5", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_5.cget("text")))
        self.button_5.grid(row=3, column=1, padx=self.padx, pady=self.pady)

        self.button_6 = customtkinter.CTkButton(self, text="6", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_6.cget("text")))
        self.button_6.grid(row=3, column=2, padx=self.padx, pady=self.pady)

        self.button_1 = customtkinter.CTkButton(self, text="1", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_1.cget("text")))
        self.button_1.grid(row=4, column=0, padx=self.padx, pady=self.pady)

        self.button_2 = customtkinter.CTkButton(self, text="2", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_2.cget("text")))
        self.button_2.grid(row=4, column=1, padx=self.padx, pady=self.pady)

        self.button_3 = customtkinter.CTkButton(self, text="3", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_3.cget("text")))
        self.button_3.grid(row=4, column=2, padx=self.padx, pady=self.pady)

        # Функциональные кнопки
        self.button_plus = customtkinter.CTkButton(self, text="+", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_plus.cget("text")))
        self.button_plus.grid(row=2, column=3, padx=self.padx, pady=self.pady)

        self.button_minus = customtkinter.CTkButton(self, text="-", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_minus.cget("text")))
        self.button_minus.grid(row=3, column=3, padx=self.padx, pady=self.pady)

        self.button_multiplication = customtkinter.CTkButton(self, text="x", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_multiplication.cget("text")))
        self.button_multiplication.grid(row=4, column=3, padx=self.padx, pady=self.pady)

        self.button_division = customtkinter.CTkButton(self, text="/", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_division.cget("text")))
        self.button_division.grid(row=5, column=3, padx=self.padx, pady=self.pady)

        self.button_result = customtkinter.CTkButton(self, text="=", width=self.button_size, height=self.button_size, command=lambda:self.entry_text(self.button_result.cget("text")))
        self.button_result.grid(row=5, column=0, columnspan=3, padx=self.padx, pady=self.pady)

    # Функция "Калькулятор валют"
    def currency_calculator(self):
        print(":)")

    def change_flag(self, choice):
        if choice == "Калькулятор":
            self.flag_change = 0
            self.calc()
        elif choice == "Калькулятор валют":
            self.flag_change = 1
            self.currency_calculator()
        print(choice)

    def emt(self):
            print("ЧО КАК")

    def entry_text(self,text):
        self.entry.configure(state = "normal")
        self.entry.insert('end',text)
        self.entry.configure(state = "disabled")

    def __init__(self):
        super().__init__()

        # Настройки прилоржения
        self.geometry("300x300")
        self.minsize(250, 250)
        self.title("Calculator")
        
        self.padx = 5
        self.pady = 5
        self.button_size = 9999
        self.flag_change = 0

        # Виджеты
        self.options = ["Калькулятор", "Калькулятор валют"]
        self.option_menu = self.option_menu = customtkinter.CTkOptionMenu(self, values=self.options, width=self.button_size, command=self.change_flag)
        self.option_menu.grid(row=0, column=0, columnspan=3, padx=self.padx, pady=self.pady, sticky="w")

        self.button_history = customtkinter.CTkButton(self, text="📝", width=self.button_size, command=self.history)
        self.button_history.grid(row=0, column=3, padx=self.padx, pady=self.pady)
            
        # Режим калькулятора
        if self.flag_change == 0:
            self.calc()
        if self.flag_change == 1:
            self.currency_calculator()

        #Настройка сетки
        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(1, weight=10)
        self.grid_columnconfigure(2, weight=10)
        self.grid_columnconfigure(3, weight=10)

        self.grid_rowconfigure(2, weight=10)
        self.grid_rowconfigure(3, weight=10)
        self.grid_rowconfigure(4, weight=10)
        self.grid_rowconfigure(5, weight=10)

app = App()
app.mainloop()