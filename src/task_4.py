#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создание рисунка домика

from tkinter import Canvas, Tk

# Создаем главное окно приложения
root = Tk()
root.title("Рисунок на холсте")

# Создаем холст (Canvas) для рисования
canvas = Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Рисуем солнце (круг)
canvas.create_oval(200, 50, 250, 100, fill="yellow", outline="yellow")
# Рисуем крышу домика (треугольник)
canvas.create_polygon(50, 175, 150, 75, 250, 175, fill="lightblue", outline="black")
# Рисуем основание домика (прямоугольник)
canvas.create_rectangle(75, 175, 225, 275, fill="lightblue", outline="black")

# Рисуем траву (серия линий)
for x in range(-45, 300, 15):
    canvas.create_line(
        x, 300, x + 5, 250, x + 30, 250, fill="green", smooth=True, width=2
    )

# Запуск главного цикла приложения
if __name__ == "__main__":
    root.mainloop()
