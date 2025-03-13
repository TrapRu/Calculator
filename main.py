import customtkinter
import moex
flag_change = 0

class App(customtkinter.CTk):  
    def result_entry(self):
        result = eval(self.entry.get())
        self.entry.delete('0', 'end')
        self.entry.insert('end', result)

    def entry_text(self,text):
        self.entry.insert('insert',text)

    def __init__(self):
        super().__init__()

        # Настройки приложения
        self.geometry("300x400")
        self.title("Calculator")
        padx = 5
        pady = 5
        button_size = 9999
        my_font = customtkinter.CTkFont(family="Fira Code", size=30)
        button_font = customtkinter.CTkFont(family="Fira Code", size=20)
        # Виджеты
             
        # Цифры
        if flag_change == 0:
            self.entry = customtkinter.CTkEntry(self, width=9999, fg_color= "#242424", border_color= "#242424", height=80, font = my_font, takefocus = True)
            self.entry.grid(row=0, column=0, columnspan=4, padx=padx, pady=pady)
            self.update()
            self.entry.focus_set()

            self.button_7 = customtkinter.CTkButton(self, text="7", fg_color= "#808080", width=button_size, height=button_size, font = button_font, command=lambda:self.entry_text(self.button_7.cget("text")))
            self.button_7.grid(row=2, column=0, padx=padx, pady=pady)

            self.button_8 = customtkinter.CTkButton(self, text="8", fg_color= "#808080", width=button_size, height=button_size, font = button_font, command=lambda:self.entry_text(self.button_8.cget("text")))
            self.button_8.grid(row=2, column=1, padx=padx, pady=pady)

            self.button_9 = customtkinter.CTkButton(self, text="9", fg_color= "#808080", width=button_size, height=button_size, font = button_font, command=lambda:self.entry_text(self.button_9.cget("text")))
            self.button_9.grid(row=2, column=2, padx=padx, pady=pady)

            self.button_4 = customtkinter.CTkButton(self, text="4", fg_color= "#808080", width=button_size, height=button_size, font = button_font, command=lambda:self.entry_text(self.button_4.cget("text")))
            self.button_4.grid(row=3, column=0, padx=padx, pady=pady)

            self.button_5 = customtkinter.CTkButton(self, text="5", fg_color= "#808080", width=button_size, height=button_size, font = button_font, command=lambda:self.entry_text(self.button_5.cget("text")))
            self.button_5.grid(row=3, column=1, padx=padx, pady=pady)

            self.button_6 = customtkinter.CTkButton(self, text="6", fg_color= "#808080", width=button_size, height=button_size, font = button_font, command=lambda:self.entry_text(self.button_6.cget("text")))
            self.button_6.grid(row=3, column=2, padx=padx, pady=pady)

            self.button_1 = customtkinter.CTkButton(self, text="1", fg_color= "#808080", width=button_size, height=button_size, font = button_font, command=lambda:self.entry_text(self.button_1.cget("text")))
            self.button_1.grid(row=4, column=0, padx=padx, pady=pady)

            self.button_2 = customtkinter.CTkButton(self, text="2", fg_color= "#808080", width=button_size, height=button_size, font = button_font, command=lambda:self.entry_text(self.button_2.cget("text")))
            self.button_2.grid(row=4, column=1, padx=padx, pady=pady)

            self.button_3 = customtkinter.CTkButton(self, text="3", fg_color= "#808080", width=button_size, height=button_size, font = button_font, command=lambda:self.entry_text(self.button_3.cget("text")))
            self.button_3.grid(row=4, column=2, padx=padx, pady=pady)
            
            self.button_0 = customtkinter.CTkButton(self, text="0", fg_color= "#808080", width=button_size, height=button_size, font = button_font, command=lambda:self.entry_text(self.button_0.cget("text")))
            self.button_0.grid(row=5, column=1, padx=padx, pady=pady)
            
            self.button_dot = customtkinter.CTkButton(self, text=".", fg_color= "#808080", width=button_size, height=button_size, font = button_font, command=lambda:self.entry_text(self.button_dot.cget("text")))
            self.button_dot.grid(row=5, column=0, padx=padx, pady=pady)
            
            #Настройка сетки
            self.grid_columnconfigure(0, weight=10)
            self.grid_columnconfigure(1, weight=10)
            self.grid_columnconfigure(2, weight=10)
            self.grid_columnconfigure(3, weight=10)
            self.grid_columnconfigure(4, weight=10)
            
            self.grid_rowconfigure(1, weight=10)
            self.grid_rowconfigure(2, weight=10)
            self.grid_rowconfigure(3, weight=10)
            self.grid_rowconfigure(4, weight=10)
            self.grid_rowconfigure(5, weight=10)
            
            
            # Функциональные кнопки
            self.button_plus = customtkinter.CTkButton(self, text="+",  fg_color= "#474747",width=button_size, height=button_size,  font = button_font,command=lambda:self.entry_text(self.button_plus.cget("text")))
            self.button_plus.grid(row=2, column=3, padx=padx, pady=pady)
            
            self.button_backspace = customtkinter.CTkButton(self, text="↫",  fg_color= "#474747",width=button_size, height=button_size,  font = button_font,command=lambda:self.entry_text(self.button_degree.cget("text")))
            self.button_backspace.grid(row=1, column=3, padx=padx, pady=pady)

            self.button_minus = customtkinter.CTkButton(self, text="-", fg_color= "#474747",width=button_size, height=button_size, font = button_font,command=lambda:self.entry_text(self.button_minus.cget("text")))
            self.button_minus.grid(row=3, column=3, padx=padx, pady=pady)

            self.button_multiplication = customtkinter.CTkButton(self, fg_color= "#474747",text="x", width=button_size, font = button_font,height=button_size, command=lambda:self.entry_text(self.button_multiplication.cget("text")))
            self.button_multiplication.grid(row=4, column=3, padx=padx, pady=pady)

            self.button_division = customtkinter.CTkButton(self, text="/", fg_color= "#474747",width=button_size, height=button_size, font = button_font,command=lambda:self.entry_text(self.button_division.cget("text")))
            self.button_division.grid(row=1, column=0, padx=padx, pady=pady)

            self.button_result = customtkinter.CTkButton(self, text="=", fg_color= "#555194", width=button_size, height=button_size, font = button_font,command=self.result_entry)
            self.button_result.grid(row=5, column=2, columnspan=2, padx=padx, pady=pady)
            fg_color= "#474747"
            self.button_degree = customtkinter.CTkButton(self, text="^", fg_color= "#474747",width=button_size, height=button_size,font = button_font, command=lambda:self.entry_text(self.button_degree.cget("text")))
            self.button_degree.grid(row=1, column=1, columnspan=1, padx=padx, pady=pady)
            
            self.button_root = customtkinter.CTkButton(self, text="√", fg_color= "#474747",width=button_size, height=button_size, font = button_font,command=lambda:self.entry_text(self.button_root.cget("text")))
            self.button_root.grid(row=1, column=2, columnspan=1, padx=padx, pady=pady)

        
        
        

# !moex.get_moex_currency_rates() 

app = App()
app.mainloop()