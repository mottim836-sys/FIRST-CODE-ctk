import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Форматирование слов")
root.geometry("700x400")
root.resizable(True, True)

def click_upper():
    if upper_check.get() == 1:
        lower_check.deselect()

def click_lower():
    if lower_check.get() == 1:
        upper_check.deselect()

def format_text():
    user_word = d_entry.get()
    if not user_word.strip():
        result_label.configure(text='Сначало введите слово!', text_color='red')
        return

    if upper_check.get() == 1 and lower_check.get() == 1:
        result_label.configure(text='Выберите ОДИН регистр!', text_color='orange')

    elif upper_check.get() == 1:
        ready_word = user_word.upper()
        result_label.configure(text=f'Результат: {ready_word}', text_color='green')

    elif lower_check.get() == 1:
        ready_word = user_word.lower()
        result_label.configure(text=f'Результат: {ready_word}', text_color='green')

    else:
        result_label.configure(text='Вы не выбрали не одного регистра', text_color='orange')

ut_label = ctk.CTkLabel(root, text='Введите слово для форматирования:', font=("Arial", 14))
ut_label.pack(pady=(20, 5))

d_entry = ctk.CTkEntry(root, placeholder_text='Поле ввода', width=250, height=35)
d_entry.pack(pady=10)

upper_check = ctk.CTkCheckBox(root, text='Верхний регистр', command=click_upper)
upper_check.pack(pady=5)

lower_check = ctk.CTkCheckBox(root, text='Нижний регистр', command=click_lower)
lower_check.pack(pady=5)

process_button = ctk.CTkButton(root, text='Форматировать', command=format_text)
process_button.pack(pady=15)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 15, "bold"))
result_label.pack(pady=10)

root.mainloop()