#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу:
# Напишите программу по следующему описанию. Нажатие Enter в однострочном
# текстовом поле приводит к перемещению текста из него в список
# (экземпляр Listbox ). При двойном клике ( <Double-Button-1> ) по
# элементу-строке списка, она должна копироваться в текстовое поле.


from tkinter import END, Entry, Event, Listbox, Tk


# Функция для добавления текста из текстового поля в список
def add_to_list(event: Event) -> None:
    text = entry.get()
    if text.strip():
        listbox.insert(END, text)
        entry.delete(0, END)


# Функция для копирования выбранного элемента из списка в текстовое поле
def copy_to_entry(event: Event) -> None:
    selected_item_index: tuple[int] = listbox.curselection()  # type: ignore[no-untyped-call]
    print(selected_item_index)
    if selected_item_index:
        text = listbox.get(selected_item_index[0])
        entry.delete(0, END)
        entry.insert(0, text)


# Создаем главное окно приложения
root = Tk()
root.title("Текстовое поле и список")

# Создаем текстовое поле и.pack его в окно
entry = Entry(root, width=30)
entry.pack(pady=10)
# Привязываем нажатие Enter к функции add_to_list
entry.bind("<Return>", add_to_list)

# Создаем список и.pack его в окно
listbox = Listbox(root, width=30, height=10)
listbox.pack(pady=10)
# Привязываем двойной клик к функции copy_to_entry
listbox.bind("<Double-Button-1>", copy_to_entry)


# Запуск главного цикла приложения
if __name__ == "__main__":
    root.mainloop()
