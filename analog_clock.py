# ascii_clock.py
import math
import time
import os

def draw_clock(h, m, s):
    size = 21  # diameter van de klok (moet oneven zijn)
    radius = size // 2
    canvas = [[" " for _ in range(size)] for _ in range(size)]

    # klokrand
    for deg in range(0, 360, 6):
        x = int(radius + radius * math.cos(math.radians(deg)))
        y = int(radius + radius * math.sin(math.radians(deg)))
        if 0 <= x < size and 0 <= y < size:
            canvas[y][x] = "o"

    # uurmarkeringen
    for i in range(12):
        angle = math.radians(90 - i * 30)
        x = int(radius + (radius - 2) * math.cos(angle))
        y = int(radius + (radius - 2) * math.sin(angle))
        canvas[y][x] = str((i if i != 0 else 12))

    # wijzers
    def plot(angle, length, char):
        for r in range(1, length):
            x = int(radius + r * math.cos(angle))
            y = int(radius + r * math.sin(angle))
            if 0 <= x < size and 0 <= y < size:
                canvas[y][x] = char

    # bereken hoeken
    hour_angle = math.radians(90 - (h % 12) * 30 - m * 0.5)
    min_angle = math.radians(90 - m * 6)
    sec_angle = math.radians(90 - s * 6)

    plot(hour_angle, radius - 6, "H")
    plot(min_angle, radius - 3, "M")
    plot(sec_angle, radius - 1, ".")

    # klok printen
    os.system("clear")  # gebruik "cls" op Windows
    for row in canvas:
        print("".join(row))

def run():
    while True:
        t = time.localtime()
        draw_clock(t.tm_hour, t.tm_min, t.tm_sec)
        time.sleep(1)

if __name__ == "__main__":
    run()
