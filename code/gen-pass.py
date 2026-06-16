import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

password = ""


def slider_callback(value):
    slid_label.configure(text=f'Длина: {int(value)}')


def generate():
    global password
    chars = ""
    if m_check.get() == 1:
        chars += "0123456789"
    if n_check.get() == 1:
        chars += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if c_check.get() == 1:
        chars += "!@#$%^&*()_+-="
    if chars == "":
        out_label.configure(text="Выберите параметры!", text_color="red")
        return
    length = int(slider.get())
    password = "".join(random.choice(chars) for _ in range(length))
    out_label.configure(text=f'Результат: {password}', text_color='green')


def copy():
    full_text = out_label.cget("text")
    pure_password = full_text.replace("Результат: ", "")
    if pure_password == "" or pure_password == "Результат:" or pure_password == "Выберите параметры!":
        return

    root.clipboard_clear()
    root.clipboard_append(pure_password)

    out_label.configure(text='УСПЕШНО СКОПИРОВАНО', text_color='green')

    root.after(1500, lambda: out_label.configure(text=f'Результат: {password}', text_color='green'))


root = ctk.CTk()
root.title("Генератор паролей")
root.geometry('800x400')
root.resizable(False, False)

gl_label = ctk.CTkLabel(root, text='Генератор паролей', text_color='white', font=('Arial', 16, 'bold'))
gl_label.grid(row=0, column=1, columnspan=3, pady=20)

m_check = ctk.CTkCheckBox(root, text='Цифры')
m_check.grid(row=1, column=0, padx=20, pady=10)

n_check = ctk.CTkCheckBox(root, text='Буквы')
n_check.grid(row=1, column=1, padx=20, pady=10)

c_check = ctk.CTkCheckBox(root, text='Спец. символы')
c_check.grid(row=1, column=2, padx=20, pady=10)

gen_button = ctk.CTkButton(root, text='Генерировать', command=generate)
gen_button.grid(row=1, column=3, padx=30, pady=10)

copy_button = ctk.CTkButton(root, text='Скопировать', command=copy)
copy_button.grid(row=2, column=3, padx=30, pady=10)

out_label = ctk.CTkLabel(root, text="Результат:", width=250)
out_label.grid(row=2, column=1, padx=20, pady=20)

slid_label = ctk.CTkLabel(root, text=f'Длина: 8')
slid_label.grid(row=3, column=1, padx=20, pady=20)

slider = ctk.CTkSlider(root, from_=8, to=24, number_of_steps=16, command=slider_callback)
slider.grid(row=4, column=0, columnspan=3, sticky="ew", padx=20, pady=20)
slider.set(8)

root.mainloop()
