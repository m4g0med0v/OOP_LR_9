#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу:
# Напишите программу, состоящую из двух списков Listbox . В первом будет,
# например, перечень товаров, заданный программно. Второй изначально пуст,
# пусть это будет перечень покупок. При клике на одну кнопку товар должен
# переходить из одного списка в другой.
# При клике на вторую кнопку – возвращаться (человек передумал покупать).
# Предусмотрите возможность множественного выбора элементов списка и их
# перемещения.


from tkinter import (
    END,
    EXTENDED,
    Button,
    Frame,
    Listbox,
    Tk,
    messagebox,
)


def move_to_list_2() -> None:
    # Получаем индексы выбранных элементов в listbox_1
    selected_items = list(listbox_1.curselection())  # type: ignore[no-untyped-call]

    # Проверяем, выбраны ли элементы
    if not selected_items:
        messagebox.showinfo("Информация", "Выберите элементы для перемещения.")
        return

    # Перемещаем элементы из listbox_1 в listbox_2
    for i in selected_items[::-1]:
        listbox_2.insert(END, listbox_1.get(i))
        listbox_1.delete(i)


def move_to_list_1() -> None:
    # Получаем индексы выбранных элементов в listbox_2
    selected_items = list(listbox_2.curselection())  # type: ignore[no-untyped-call]

    # Проверяем, выбраны ли элементы
    if not selected_items:
        messagebox.showinfo("Информация", "Выберите элементы для перемещения.")
        return

    # Перемещаем элементы из listbox_2 в listbox_1
    for i in selected_items[::-1]:
        listbox_1.insert(END, listbox_2.get(i))
        listbox_2.delete(i)


root = Tk()
root.title("Списки")

# Создаем фреймы для списков и кнопок
leftFrame = Frame(root)
leftFrame.grid(row=0, column=0)

midFrame = Frame(root)
midFrame.grid(row=0, column=1)

rightFrame = Frame(root)
rightFrame.grid(row=0, column=2)

# Создаем список товаров
listbox_1 = Listbox(leftFrame, selectmode=EXTENDED)
listbox_1.pack(padx=10, pady=10)

# Добавляем товары в список
items = [
    "яблоки",
    "бананы",
    "морковь",
    "хлеб",
    "масло",
    "мясо",
    "картошка",
    "ананас",
]
for item in items:
    listbox_1.insert(END, item)

# Создаем список покупок
listbox_2 = Listbox(rightFrame, selectmode=EXTENDED)
listbox_2.pack(padx=10, pady=10)

# Создаем кнопки для перемещения элементов
button_1 = Button(
    midFrame,
    text=">>>",
    command=move_to_list_2,
)
button_1.pack(padx=5)

button_2 = Button(
    midFrame,
    text="<<<",
    command=move_to_list_1,
)
button_2.pack(padx=5)


if __name__ == "__main__":
    root.mainloop()
