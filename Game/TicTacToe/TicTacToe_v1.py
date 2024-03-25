import time
import turtle
import random

window = turtle.Screen()
bok = 600
X = -300
Y = 300
window.setup(bok, bok)
window.title("Kółko i krzyżyk")
window.bgcolor("black")

xo = turtle.Turtle()
xo.color("white")
xo.pensize(7)
xo.speed(0)
xo.hideturtle()

tab = [[None, None, None], [None, None, None], [None, None, None]]

# tablica [wiersz] kolumna[]
kolej = random.choice(["x", "o"])

# siatka
odstep = int(bok/3)

for a in [1, 2]:
    xo.penup()
    xo.goto(X + a * odstep, Y)
    xo.pendown()
    xo.goto(X + a * odstep, -Y)

    xo.penup()
    xo.goto(X, Y - a * odstep)
    xo.pendown()
    xo.goto(-X, Y - a * odstep)

def sprawdz():

    # po skosie
    if tab[0][0] == tab[1][1] == tab[2][2]: return tab[2][2]
    if tab[0][2] == tab[1][1] == tab[2][0]: return tab[2][0]

    #  w poziomie (wierszu)
    for w in range(2):
        if tab[w][0] == tab[w][1] == tab[w][2]: return tab[w][2]

    #  w pionie (kolumnie)
    for k in range(2):
        if tab[0][k] == tab[1][k] == tab[2][k]: return tab[2][k]

def click(x, y):

    global kolej

    # w które pole kliknięto

    kolumna = 0
    if x < X + odstep: kolumna = 0
    elif x > X + 2*odstep: kolumna = 2
    else: kolumna = 1

    wiersz = 0
    if y < Y - 2*odstep: wiersz = 2
    elif y > Y - odstep: wiersz = 0
    else: wiersz = 1

    print(wiersz, kolumna)

    # pole jest puste (zignorowanie kliknięcia)
    if tab [wiersz][kolumna] != None: return

    # jeżeli pole nie jest puste - narysować odpowiedni znak

    kolumna_srodek = (kolumna * odstep + odstep/2) - bok/2
    wiersz_srodek = (-wiersz * odstep - odstep/2) + bok/2
    xo.penup()
    xo.goto(kolumna_srodek-50, wiersz_srodek-70)
    if kolej == "x": xo.write("X", font=("Arial", 100))
    else: xo.write("O", font=("Arial", 100))

    # zapamiętanie kolejnego ruchu - zapis w tablicy
    tab[wiersz][kolumna] = kolej
    if kolej == "o": kolej = "x"
    else: kolej = "o"

    # sprawdzenie wyniku
    if sprawdz() != None:
        xo.penup()
        xo.goto(-150, 0)
        time.sleep(1)
        xo.clear()
        xo.write("Wygrały " + sprawdz(), font=("Arial", 50))

window.onclick(click)
window.listen()
window.mainloop()
