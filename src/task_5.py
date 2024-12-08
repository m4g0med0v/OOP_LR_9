#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: в данной программе создается анимация круга, который движется
# от левой границы холста до правой.

# Выражение c.coords(ball) возвращает список текущих координат объекта
# (в данном случае это ball). Третий элемент списка соответствует его второй
# координате x. Метод after вызывает функцию, переданную вторым аргументом,
# через количество миллисекунд, указанных первым аргументом.

# Изучите приведенную программу и самостоятельно запрограммируйте постепенное
# движение фигуры в ту точку холста, где пользователь кликает левой кнопкой
# мыши. Координаты события хранятся в его атрибутах x и y
# ( event.x , event.y ).


from tkinter import Canvas, Event, Tk


# Функция для движения круга к целевой точке
def motion() -> None:
    # Расчет разницы координат между текущей позицией круга и целевой точкой
    dx = target_x - c.coords(ball)[0]
    dy = target_y - c.coords(ball)[1]

    # Расчет расстояния между текущей позицией и целевой точкой
    distance = (dx**2 + dy**2) ** 0.5

    # Если расстояние больше 1 пикселя, продолжаем движение
    if distance > 1:
        # Нормализация вектора движения
        dx, dy = dx / distance, dy / distance
        # Перемещение круга на небольшое расстояние в направлении целевой точки
        c.move(ball, dx * speed, dy * speed)
        # Вызов функции motion через 10 миллисекунд для продолжения движения
        root.after(10, motion)


# Функция для обработки клика левой кнопкой мыши
def on_click(event: Event) -> None:
    global target_x, target_y
    # Обновление целевых координат по клику мыши
    target_x, target_y = event.x, event.y
    # Запуск движения круга к новой целевой точке
    motion()


# Создание главного окна приложения
root = Tk()

# Создание холста (Canvas) для рисования
c = Canvas(root, width=300, height=200, bg="white")
c.pack()

# Создание круга в левой части холста
ball = c.create_oval(0, 100, 40, 140, fill="green")

# Инициализация целевых координат как начальной позиции круга
target_x, target_y = c.coords(ball)[0], c.coords(ball)[1]

# Скорость движения круга
speed: int = 2

# Привязка события клика левой кнопкой мыши к функции on_click
c.bind("<Button-1>", on_click)

# Запуск главного цикла приложения
if __name__ == "__main__":
    root.mainloop()
