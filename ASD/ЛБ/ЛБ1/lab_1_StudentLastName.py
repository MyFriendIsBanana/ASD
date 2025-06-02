import turtle

# Настройка окна
turtle.speed(0)
turtle.bgcolor("black")
turtle.pencolor("gold")  # Золотой цвет для символа мира
turtle.pensize(3)

def draw_peace_swastika():
    size = 60  # Длина основного сегмента
    hook = size // 2  # Длина крюка

    for _ in range(4):
        turtle.forward(size)      # Основная линия
        turtle.left(90)          # Поворот против часовой стрелки для крюка
        turtle.forward(hook)     # Рисуем крюк
        turtle.back(hook)        # Возвращаемся
        turtle.right(90)         # Возвращаем ориентацию
        turtle.forward(size)     # Продолжаем основную линию
        turtle.left(90)          # Поворачиваем для следующей части

# Рисуем свастику один раз
draw_peace_swastika()
turtle.hideturtle()  # Скрываем черепаху после рисования
turtle.done()  # Оставляем окно открытым