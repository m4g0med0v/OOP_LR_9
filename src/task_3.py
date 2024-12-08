#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу:
# Напишите программу по описанию. Размеры многострочного текстового поля
# определяются значениями, введенными в однострочные текстовые поля. Изменение
# размера происходит при нажатии мышью на кнопку, а также при нажатии клавиши
# Enter. Цвет фона экземпляра Text светлосерый ( lightgrey ), когда поле не в
# фокусе, и белый, когда имеет фокус. Событие получения фокуса обозначается
# как <FocusIn> , потери – как <FocusOut> . Для справки: фокус перемещается
# по виджетам при нажатии Tab, Ctrl+Tab, Shift+Tab, а также при клике по ним
# мышью (к кнопкам последнее не относится).


from tkinter import Button, Entry, Event, Label, Text, Tk, messagebox


# Функция для обновления размера текстового поля
def update_text_size(event: Event = None) -> None:
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())

        text_widget.config(width=width, height=height)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числовые значения!")


# Функция для изменения цвета фона текстового поля при получении фокуса
def on_focus_in(event: Event) -> None:
    text_widget.config(bg="white")


# Функция для изменения цвета фона текстового поля при потере фокуса
def on_focus_out(event: Event) -> None:
    text_widget.config(bg="lightgrey")


# Создаем главное окно приложения
root = Tk()
root.title("Изменение размера текста")

# Создаем метку и поле ввода для ширины
width_label = Label(root, text="Ширина: ")
width_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
width_entry = Entry(root, width=5)
width_entry.insert(0, "25")
width_entry.grid(row=0, column=1, padx=5, pady=5)

# Создаем метку и поле ввода для высоты
height_label = Label(root, text="Высота: ")
height_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
height_entry = Entry(root, width=5)
height_entry.insert(0, "12")
height_entry.grid(row=1, column=1, padx=5, pady=5)

# Создаем кнопку для изменения размера текстового поля
resize_button = Button(root, text="Изменить", command=update_text_size)
resize_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

# Создаем многострочное текстовое поле
text_widget = Text(root, width=25, height=12, bg="lightgrey")
text_widget.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Привязываем события получения и потери фокуса к соответствующим функциям
text_widget.bind("<FocusIn>", on_focus_in)
text_widget.bind("<FocusOut>", on_focus_out)

# Привязываем нажатие Enter к функции обновления размера текстового поля
text_widget.bind("<Return>", update_text_size)


# Запуск главного цикла приложения
if __name__ == "__main__":
    root.mainloop()
