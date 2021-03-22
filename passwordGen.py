from tkinter import *
from tkinter import messagebox
import random


root = Tk()
root.geometry('360x480')
root['bg'] = 'floral white'

Label(text='Генератор паролей', font=('Arial', 14), bg='floral white').grid(row=0, column=0, padx='70px')
entry = Entry(width=24, )
entry.grid(row=1, column=0, padx='70px', pady=('20px', '10px'))
entry.insert(0, 'Ваш пароль появится тут')

Label(text='Введите количество символов в пароле', bg='floral white').grid(row=2, column=0,)
length = Entry(width=22)
length.grid(row=3, column=0, padx='70px')

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

numbers = Checkbutton(text='Цирфы', variable=var1, bg='floral white')
numbers.grid(row=4, column=0, pady=('10px', 0), padx=(0, '56px'))

letters = Checkbutton(text='Буквы', variable=var2, bg='floral white')
letters.grid(row=5, column=0, pady=('5px', 0), padx=(0, '61px'))

symbols = Checkbutton(text='Символы(@#$!%^&)', variable=var3, bg='floral white')
symbols.grid(row=6, column=0, pady=('5px', 0))


def gener():
    entry.delete(0, END)
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 't', 's', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
                    'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                    'Q', 'R', 'T', 'S', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-',
                    '+', '=', '"', '№', ';', ':', '?', '*']

    res = []

    if var1.get():
        res += numbers_list
    if var2.get():
        res += letters_list
    if var3.get():
        res += symbols_list
    try:
        length_of_password = int(length.get())
    except ValueError:
        length_of_password = 8

    password_lst = []
    if res:
        for c in range(length_of_password):
            password_lst.append(random.choice(res))
        password = ''.join(password_lst)
        entry.insert(0, password)
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo('Успех', 'Ваш пароль был скопирован в буфер обмена')
    else:
        messagebox.showerror('Ошибка', 'Поставьте хотя бы одну галочку')



btn = Button(text='Сгенерировать', bg='papaya whip', command=gener)
btn.grid(row=7, column=0, pady=('10px', 0))

root.mainloop()