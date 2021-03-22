from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfilename
from numpy import mean, std  # для начала установить pip install numpy==1.19.3
import math

root = Tk()
root.title("Калькулятор")
root.geometry('434x232')
root['bg'] = '#F6DFD9'

entr = Entry(root, width=43, justify=RIGHT, font=('Calibri', '14'))
entr.grid(row=0, column=0, columnspan=7)
entr.focus_set()

data_for_save = []


def my_eval(exp):
    """Функция вместо eval()"""
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    def polish_eval(elements):
        pile = []
        while elements:
            e = elements.pop(0)
            if e in operators:
                b = pile.pop()
                a = pile.pop()
                pile.append(operators[e](a, b))
            else:
                try:
                    pile.append(float(e))
                except SyntaxError or TypeError or ValueError or IndexError:
                    messagebox.showerror('Ошибка!', 'Неправильно введены данные')
                    entr.delete(0, END)
        return pile[0]

    def convert(s):
        lex = parse(s)
        symbol = []
        result_list = []
        oper = ["+", "-", "*", "/", "(", ")"]
        for a in lex:
            if a == "(":
                symbol = [a] + symbol
            elif a in oper:
                if not symbol:
                    symbol = [a]
                elif a == ")":
                    while True:
                        q = symbol[0]
                        symbol = symbol[1:]
                        if q == "(":
                            break
                        result_list += [q]
                elif priority(symbol[0]) < priority(a):
                    symbol = [a] + symbol
                else:
                    while True:
                        if not symbol:
                            break
                        q = symbol[0]
                        result_list += [q]
                        symbol = symbol[1:]
                        if priority(q) == priority(a):
                            break
                    symbol = [a] + symbol
            else:
                result_list += [a]
        while symbol:
            q = symbol[0]
            result_list += [q]
            symbol = symbol[1:]
        return result_list

    def priority(o):
        if o == "+" or o == "-":
            return 1
        elif o == "*" or o == "/":
            return 2
        elif o == "(":
            return 0

    def parse(s):
        delims = ["+", "-", "*", "/", "(", ")"]
        lex = []
        tmp = ""
        itr = iter(s)
        for a in itr:
            if a != " ":
                if a == '{' and next(itr) == '-':
                    string = '-'
                    next_iteration = next(itr)
                    while next_iteration.isdigit():
                        string += f'{next_iteration}'
                        next_iteration = next(itr)
                    lex.append(string)
                elif a in delims:
                    if tmp != "":
                        lex += [tmp]
                    lex += [a]
                    tmp = ""
                else:
                    tmp += a
        if tmp != "":
            lex += [tmp]

        return lex

    return polish_eval(convert(exp))


def calc(key):
    global result
    if key == "=":
        try:
            result = my_eval(entr.get())
            entr.insert(END, ' = ' + str(result))
            data_for_save.append(result)
        except ZeroDivisionError:
            messagebox.showerror('Ошибка', 'Вы поделили на ноль!')
            entr.delete(0, END)
        except:
            messagebox.showerror('Ошибка',
                                 'Расставьте правильно знаки!\nОтрицательные числа возьмите в фигурные скобки { }')
            entr.delete(0, END)

    elif key == "C":
        entr.delete(0, END)

    elif key == "π":
        result = math.pi
        entr.insert(END, result)
        data_for_save.append(result)

    elif key == "e":
        result = math.e
        entr.insert(END, result)
        data_for_save.append(result)

    elif key == "xⁿ":
        entr.insert(END, "**")

    elif key == "sin(rad)":
        try:
            result = str(math.sin(float(entr.get())))
            entr.insert(END, " = " + result)
            data_for_save.append(result)
        except ValueError:
            messagebox.showerror('Ошибка', 'Сначала введите число!')

    elif key == "cos(rad)":
        try:
            result = str(math.cos(float(entr.get())))
            entr.insert(END, " = " + result)
            data_for_save.append(result)
        except ValueError:
            messagebox.showerror('Ошибка', 'Сначала введите число!')

    elif key == "sin(°)":
        try:
            result = str(math.sin(math.radians(float(entr.get()))))
            entr.insert(END, " = " + result)
            data_for_save.append(result)
        except ValueError:
            messagebox.showerror('Ошибка', 'Сначала введите число!')

    elif key == "cos(°)":
        try:
            result = str(math.cos(math.radians(float(entr.get()))))
            entr.insert(END, " = " + result)
            data_for_save.append(result)
        except ValueError:
            messagebox.showerror('Ошибка', 'Сначала введите число!')

    elif key == "tan(°)":
        try:
            result = str(math.cos(math.radians(float(entr.get()))))
            entr.insert(END, " = " + result)
            data_for_save.append(result)
        except ValueError:
            messagebox.showerror('Ошибка', 'Сначала введите число!')

    elif key == "tan(rad)":
        try:

            result = str(math.tan(float(entr.get())))
            entr.insert(END, " = " + result)
            data_for_save.append(result)
        except ValueError:
            messagebox.showerror('Ошибка', 'Сначала введите число!')

    elif key == "back":
        entr.delete(len(entr.get()) - 1)

    elif key == "(":
        entr.insert(END, "(")

    elif key == ")":
        entr.insert(END, ")")

    elif key == "n!":
        try:
            result = str(math.factorial(int(entr.get())))
            entr.insert(END, "! = " + result)
            data_for_save.append(result)
        except ValueError:
            messagebox.showerror('Ошибка', 'Сначала введите число!')

    elif key == "√x":
        try:
            result = str(math.sqrt(int(entr.get())))
            entr.insert(END, " = " + result)
            data_for_save.append(result)
        except ValueError:
            messagebox.showerror('Ошибка', 'Сначала введите число!')

    else:
        if "=" in entr.get():
            entr.delete(0, END)
        entr.insert(END, key)


Button(root, text='7', relief=GROOVE, command=lambda: calc(7),
       height=2, width=6, bg='#F6DFD9').grid(row=2, column=0, sticky="nsew")
Button(root, text='4', relief=GROOVE, command=lambda: calc(4),
       height=2, width=6, bg='#F6DFD9').grid(row=3, column=0, sticky="nsew")
Button(root, text='1', relief=GROOVE, command=lambda: calc(1),
       height=2, width=6, bg='#F6DFD9').grid(row=4, column=0, sticky="nsew")
Button(root, text='n!', relief=GROOVE, command=lambda: calc('n!'),
       height=2, width=6, ).grid(row=5, column=0, sticky="nsew")
Button(root, text='=', relief=GROOVE, command=lambda: calc('='),
       height=2, width=6, bg='#F6DFD9').grid(row=6, column=0, columnspan=3, sticky="nsew")

Button(root, text='8', relief=GROOVE, command=lambda: calc(8),
       height=2, width=6, bg='#F6DFD9').grid(row=2, column=1, sticky="nsew")
Button(root, text='5', relief=GROOVE, command=lambda: calc(5),
       height=2, width=6, bg='#F6DFD9').grid(row=3, column=1, sticky="nsew")
Button(root, text='2', relief=GROOVE, command=lambda: calc(2),
       height=2, width=6, bg='#F6DFD9').grid(row=4, column=1, sticky="nsew")
Button(root, text='0', relief=GROOVE, command=lambda: calc(0),
       height=2, width=6, bg='#F6DFD9').grid(row=5, column=1, sticky="nsew")

Button(root, text='9', relief=GROOVE, command=lambda: calc(9),
       height=2, width=6, bg='#F6DFD9').grid(row=2, column=2, sticky="nsew")
Button(root, text='6', relief=GROOVE, command=lambda: calc(6),
       height=2, width=6, bg='#F6DFD9').grid(row=3, column=2, sticky="nsew")
Button(root, text='3', relief=GROOVE, command=lambda: calc(3),
       height=2, width=6, bg='#F6DFD9').grid(row=4, column=2, sticky="nsew")
Button(root, text='.', relief=GROOVE, command=lambda: calc('.'),
       height=2, width=6, ).grid(row=5, column=2, sticky="nsew")

Button(root, text='⌫', relief=GROOVE, command=lambda: calc('back'),
       height=2, width=6, bg='#E3B5B8').grid(row=2, column=3, sticky="nsew")
Button(root, text='+', relief=GROOVE, command=lambda: calc('+'),
       height=2, width=6, bg='#E3B5B8').grid(row=3, column=3, sticky="nsew")
Button(root, text='*', relief=GROOVE, command=lambda: calc('*'),
       height=2, width=6, bg='#E3B5B8').grid(row=4, column=3, sticky="nsew")
Button(root, text='(', relief=GROOVE, command=lambda: calc('('),
       height=2, width=6, bg='#E3B5B8').grid(row=5, column=3, sticky="nsew")
Button(root, text='{', relief=GROOVE, command=lambda: calc('{'),
       height=2, width=6, bg='#E3B5B8').grid(row=6, column=3, sticky="nsew")

Button(root, text='C', relief=GROOVE, command=lambda: calc('C'),
       height=2, width=6, bg='#E3B5B8').grid(row=2, column=4, sticky="nsew")
Button(root, text='-', relief=GROOVE, command=lambda: calc('-'),
       height=2, width=6, bg='#E3B5B8').grid(row=3, column=4, sticky="nsew")
Button(root, text='/', relief=GROOVE, command=lambda: calc('/'),
       height=2, width=6, bg='#E3B5B8').grid(row=4, column=4, sticky="nsew")
Button(root, text=')', relief=GROOVE, command=lambda: calc(')'),
       height=2, width=6, bg='#E3B5B8').grid(row=5, column=4, sticky="nsew")
Button(root, text='}', relief=GROOVE, command=lambda: calc('}'),
       height=2, width=6, bg='#E3B5B8').grid(row=6, column=4, sticky="nsew")

Button(root, text='sin(°)', relief=GROOVE, command=lambda: calc('sin(°)'),
       height=2, width=6, bg='#DCE0AD').grid(row=2, column=5, sticky="nsew")
Button(root, text='cos(°)', relief=GROOVE, command=lambda: calc('cos(°)'),
       height=2, width=6, bg='#DCE0AD').grid(row=3, column=5, sticky="nsew")
Button(root, text='tan(°)', relief=GROOVE, command=lambda: calc('tan(°)'),
       height=2, width=6, bg='#DCE0AD').grid(row=4, column=5, sticky="nsew")
Button(root, text='√x', relief=GROOVE, command=lambda: calc('√x'),
       height=2, width=6, bg='#DCE0AD').grid(row=5, column=5, sticky="nsew")
Button(root, text='e', relief=GROOVE, command=lambda: calc('e'),
       height=2, width=6, bg='#DCE0AD').grid(row=6, column=5, sticky="nsew")

Button(root, text='sin(rad)', relief=GROOVE, command=lambda: calc('sin(rad)'),
       height=2, width=6, bg='#DCE0AD').grid(row=2, column=6, sticky="nsew")
Button(root, text='cos(rad)', relief=GROOVE, command=lambda: calc('cos(rad)'),
       height=2, width=6, bg='#DCE0AD').grid(row=3, column=6, sticky="nsew")
Button(root, text='tan(rad)', relief=GROOVE, command=lambda: calc('tan(rad)'),
       height=2, width=6, bg='#DCE0AD').grid(row=4, column=6, sticky="nsew")
Button(root, text='xⁿ', relief=GROOVE, command=lambda: calc('xⁿ'),
       height=2, width=6, bg='#DCE0AD').grid(row=5, column=6, sticky="nsew")
Button(root, text='π', relief=GROOVE, command=lambda: calc('π'),
       height=2, width=6, bg='#DCE0AD').grid(row=6, column=6, sticky="nsew")


def take_last_result():
    try:
        entr.delete(0, END)
        entr.insert(END, result)
    except NameError:
        messagebox.showerror('Ошибка', 'Ещё не было ни ондого значения!')


def save_result():
    out = asksaveasfile(mode='w', defaultextension='txt')
    try:
        for i in data_for_save:
            out.write(str(i) + '\n')
    except AttributeError:
        messagebox.showerror("Ошибка!", "Что-то пошло не так :(")


def clear_result():
    global result
    result = None
    messagebox.showinfo('Изменено', 'Последний результат был успешно удалён')


def m_plus():
    """Функция М+"""

    try:
        a = int(result) + int(entr.get())
        entr.delete(0, END)
        entr.insert(END, a)
    except NameError:
        messagebox.showerror('Ошибка', 'Ещё не было ни ондого значения!')


def m_minus():
    """Функция М-"""

    try:
        a = int(result) - int(entr.get())
        entr.delete(0, END)
        entr.insert(END, a)
    except NameError:
        messagebox.showerror('Ошибка', 'Ещё не было ни ондого значения!')


list_of_const = [('e', 2.71), ('π', 3.14), ('c', 299792458), ('%', 0.01)]


def add_listbox_const():
    """Создает окно с листбоксом, где константы"""

    listbox_window = Tk()
    listbox_window.title('Константы')
    listbox_window['bg'] = '#90CED1'

    lbl = Label(listbox_window, text="Константы", bg='#90CED1')
    lbl.grid(sticky=W, pady=4, padx=5)

    listbox = Listbox(listbox_window)
    listbox.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E + W + S + N)
    listbox.insert(END, 'e')
    listbox.insert(END, 'π')
    listbox.insert(END, 'c')
    listbox.insert(END, '%')

    def fill_listbox():
        lst = ' '.join(listbox.get(0, END))
        for i in list_of_const:
            if i[0] not in lst:
                listbox.insert(END, i[0])

    fill_listbox()

    def add_const(a, b):
        """Добавление констант"""

        list_of_const.append((a, b))
        fill_listbox()

    def take_value():
        try:
            indx = listbox.curselection()[0]
            value = float(list_of_const[indx][1])
            entr.insert(END, value)
        except IndexError:
            messagebox.showerror('Ошибка', 'Вы не выбрали константу или задали ей некорректное значение!')

    name_const_lab = Label(listbox_window, text="Введите название константы:", bg='#90CED1')
    name_const_lab.grid(row=1, column=2, sticky="w")
    value_const_lab = Label(listbox_window, text="Введите значение константы:", bg='#90CED1')
    value_const_lab.grid(row=3, column=2, sticky="w")

    name_const = Entry(listbox_window, width=13, font=('Calibri', '14'))
    name_const.grid(row=2, column=2, padx=5, pady=5)
    value_const = Entry(listbox_window, width=13, font=('Calibri', '14'))
    value_const.grid(row=4, column=2, padx=5)

    Button(listbox_window, text='Добавить', relief=GROOVE,
           command=lambda: add_const(name_const.get(), value_const.get()), width=7).grid(row=5, column=2)
    Button(listbox_window, text='Взять значение', relief=GROOVE,
           command=take_value, width=13).grid(row=5, column=0, pady=5)

    Button(listbox_window, text="Готово", relief=GROOVE,
           command=lambda: listbox_window.destroy()).grid(row=5, column=3, padx=(0, 5))

    listbox_window.mainloop()


def stat_func():
    """Создает окно с статическими функциями"""

    static = Tk()
    static.geometry("295x200")
    static.title('Статичесике функции')
    static['bg'] = '#defbcf'

    lbl = Label(static, text="Введите цифры через пробел", bg='#defbcf')
    lbl.grid(row=0, column=0, sticky=W, columnspan=3, pady=10)

    def get_file():
        try:
            path_of_filename = askopenfilename()

            with open(path_of_filename, 'r') as info:
                data = []
                res = []

                for line in info:
                    data.append([x for x in line.split()])

                for i in data:
                    for k in i:
                        res.append(k)
                trash = (',', ';', ';', '  ', '   ')
                string = ' '.join(res)

                for i in trash:
                    if i in string:
                        reform_string = string.replace(i, '')
                    else:
                        reform_string = string
                entry_field.delete(0, END)
                entry_field.insert(END, reform_string)

        except FileNotFoundError or UnicodeDecodeError:
            messagebox.showerror('Ошибка', 'Что-то пошло не так :(')

    menu = Menu(static)
    menu.add_cascade(label="Import from file", command=get_file)
    static.config(menu=menu)

    entry_field = Entry(static, width=23, justify=RIGHT, font=('Calibri', '14'))
    entry_field.grid(row=1, column=0, columnspan=3, padx=5)
    entry_field.focus_set()

    Button(static, text='C', relief=GROOVE, command=lambda: entry_field.delete(0, END),
           height=1, width=2).grid(row=1, column=3, padx=(5, 0))

    def make_lst(n):
        lst = n.split(' ')
        lst_with_int = list(map(float, lst))
        return lst_with_int

    def summa():
        global result
        try:
            result = sum(make_lst(entry_field.get()))
            entry_field.insert(END, ' = ' + str(result))
        except ValueError:
            messagebox.showerror('Ошибка', 'Введите корректные данные!')

    def average():
        global result
        try:
            result = mean(make_lst(entry_field.get()))
            entry_field.insert(END, ' = ' + str(result))
        except ValueError:
            messagebox.showerror('Ошибка', 'Введите корректные данные!')

    def deviation():
        global result
        try:
            result = std(make_lst(entry_field.get()))
            entry_field.insert(END, ' = ' + str(result))
        except ValueError:
            messagebox.showerror('Ошибка', 'Введите корректные данные!')

    Button(static, text='Сумма', relief=GROOVE, command=summa,
           height=2, width=4).grid(row=2, column=0, sticky="nsew", pady=20, padx=7)
    Button(static, text='Среднее\nзначение', relief=GROOVE, command=average,
           height=2, width=4).grid(row=2, column=1, sticky="nsew", pady=20, padx=7)
    Button(static, text='Ср. квадр.\nотклон.', relief=GROOVE, command=deviation,
           height=2, width=4).grid(row=2, column=2, sticky="nsew", pady=20, padx=7)

    Button(static, text="Готово", command=lambda: static.destroy()).grid(row=3, column=3, pady=23)

    static.mainloop()


def logarithm():
    """Создает окно с логарфмами"""

    log_window = Tk()
    log_window.title('Логарифмы')
    log_window.geometry('430x220')
    log_window['bg'] = ['#fbb6b6']

    def count_log(a, x):
        try:
            global result
            result = math.log(float(x), float(a))
            messagebox.showinfo('Result', f'Логарифм {x} по основанию {a} = ' + str(result))
        except ValueError:
            messagebox.showerror('Ошибка', 'Введите корректное значение!')

    def count_ln(x):
        try:
            global result
            result = math.log(float(x))
            messagebox.showinfo('Result', f'Натуральний логарифм {x} = ' + str(result))
        except ValueError:
            messagebox.showerror('Ошибка', 'Введите корректное значение!')

    lbl_log = Label(log_window, text="Логарифм(основа, аргумент)", bg='#fbb6b6')
    lbl_log.grid(row=0, column=0, padx=(15, 75), pady=(10, 0))
    base = Entry(log_window, width=13, justify=RIGHT, font=('Calibri', '14'))
    base.grid(row=1, column=0, padx=(0, 75), pady=15)
    argument = Entry(log_window, width=13, justify=RIGHT, font=('Calibri', '14'))
    argument.grid(row=2, column=0, padx=(0, 75))
    Button(log_window, text='Посчитать', relief=GROOVE,
           command=lambda: count_log(base.get(), argument.get())).grid(row=3, column=0, pady=15)

    lbl_ln = Label(log_window, text="Логарифм натуральный", bg='#fbb6b6')
    lbl_ln.grid(row=0, column=1, pady=(10, 0))
    argument_ln = Entry(log_window, width=13, justify=RIGHT, font=('Calibri', '14'))
    argument_ln.grid(row=1, column=1)
    Button(log_window, text='Посчитать', relief=GROOVE,
           command=lambda: count_ln(argument_ln.get())).grid(row=3, column=1, pady=15, padx=(65, 0))

    Button(log_window, text="Готово", command=lambda: log_window.destroy()).grid(column=1, pady=(20, 0), padx=(120, 0))

    log_window.mainloop()


main_menu = Menu()
main_menu.add_cascade(label="Use or add const", command=add_listbox_const)

dropdown = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Result", menu=dropdown)
dropdown.add_command(label="Last result", command=take_last_result)
dropdown.add_command(label="Save results", command=save_result)
dropdown.add_command(label="Clear result", command=clear_result)

main_menu.add_cascade(label="Static functions", command=stat_func)

dropdown_m = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="M", menu=dropdown_m)
dropdown_m.add_command(label="M+", command=m_plus)
dropdown_m.add_command(label="M-", command=m_minus)

main_menu.add_cascade(label="Logarithms", command=logarithm)

root.config(menu=main_menu)

root.mainloop()
