import customtkinter
import moex
flag_change = 1

class App(customtkinter.CTk):
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
        self.title("Calculator")
        padx = 5
        pady = 5
        button_size = 9999

        # Виджеты
        
            
        # Цифры
        if flag_change == 0:
            self.entry = customtkinter.CTkEntry(self, width=button_size, state = "disabled")
            self.entry.grid(row=0, column=0, columnspan=4, padx=padx, pady=pady)

            self.button_7 = customtkinter.CTkButton(self, text="7", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_7.cget("text")))
            self.button_7.grid(row=1, column=0, padx=padx, pady=pady)

            self.button_8 = customtkinter.CTkButton(self, text="8", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_8.cget("text")))
            self.button_8.grid(row=1, column=1, padx=padx, pady=pady)

            self.button_9 = customtkinter.CTkButton(self, text="9", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_9.cget("text")))
            self.button_9.grid(row=1, column=2, padx=padx, pady=pady)

            self.button_4 = customtkinter.CTkButton(self, text="4", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_4.cget("text")))
            self.button_4.grid(row=2, column=0, padx=padx, pady=pady)

            self.button_5 = customtkinter.CTkButton(self, text="5", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_5.cget("text")))
            self.button_5.grid(row=2, column=1, padx=padx, pady=pady)

            self.button_6 = customtkinter.CTkButton(self, text="6", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_6.cget("text")))
            self.button_6.grid(row=2, column=2, padx=padx, pady=pady)

            self.button_1 = customtkinter.CTkButton(self, text="1", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_1.cget("text")))
            self.button_1.grid(row=3, column=0, padx=padx, pady=pady)

            self.button_2 = customtkinter.CTkButton(self, text="2", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_2.cget("text")))
            self.button_2.grid(row=3, column=1, padx=padx, pady=pady)

            self.button_3 = customtkinter.CTkButton(self, text="3", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_3.cget("text")))
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
            self.button_plus = customtkinter.CTkButton(self, text="+", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_plus.cget("text")))
            self.button_plus.grid(row=1, column=3, padx=padx, pady=pady)

            self.button_minus = customtkinter.CTkButton(self, text="-", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_minus.cget("text")))
            self.button_minus.grid(row=2, column=3, padx=padx, pady=pady)

            self.button_multiplication = customtkinter.CTkButton(self, text="x", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_multiplication.cget("text")))
            self.button_multiplication.grid(row=3, column=3, padx=padx, pady=pady)

            self.button_division = customtkinter.CTkButton(self, text="/", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_division.cget("text")))
            self.button_division.grid(row=4, column=3, padx=padx, pady=pady)

            self.button_result = customtkinter.CTkButton(self, text="=", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_result.cget("text")))
            self.button_result.grid(row=4, column=0, columnspan=3, padx=padx, pady=pady)
        
        
        if flag_change == 1:
            self.entry = customtkinter.CTkEntry(self, width=button_size, state = "disabled")
            self.entry.grid(row=0, column=0, columnspan=4, padx=padx, pady=pady)

            self.button_7 = customtkinter.CTkButton(self, text="7", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_7.cget("text")))
            self.button_7.grid(row=1, column=0, padx=padx, pady=pady)

            self.button_8 = customtkinter.CTkButton(self, text="8", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_8.cget("text")))
            self.button_8.grid(row=1, column=1, padx=padx, pady=pady)

            self.button_9 = customtkinter.CTkButton(self, text="9", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_9.cget("text")))
            self.button_9.grid(row=1, column=2, padx=padx, pady=pady)

            self.button_4 = customtkinter.CTkButton(self, text="4", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_4.cget("text")))
            self.button_4.grid(row=2, column=0, padx=padx, pady=pady)

            self.button_5 = customtkinter.CTkButton(self, text="5", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_5.cget("text")))
            self.button_5.grid(row=2, column=1, padx=padx, pady=pady)

            self.button_6 = customtkinter.CTkButton(self, text="6", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_6.cget("text")))
            self.button_6.grid(row=2, column=2, padx=padx, pady=pady)

            self.button_1 = customtkinter.CTkButton(self, text="1", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_1.cget("text")))
            self.button_1.grid(row=3, column=0, padx=padx, pady=pady)

            self.button_2 = customtkinter.CTkButton(self, text="2", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_2.cget("text")))
            self.button_2.grid(row=3, column=1, padx=padx, pady=pady)

            self.button_3 = customtkinter.CTkButton(self, text="3", width=button_size, height=button_size, command=lambda:self.entry_text(self.button_3.cget("text")))
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
"""
moex.get_moex_currency_rates() 
"""
app = App()
app.mainloop()