import numpy as np
import random

def move_left1(pl):
    
    new_pl = np.copy(pl)
    for i in range(0, 4):
        for movIndex in range(0, 3):
            if new_pl[i][movIndex] == new_pl[i][movIndex + 1]:
                new_pl[i][movIndex + 1] = 2 * new_pl[i][movIndex]
                new_pl[i][movIndex] = 0
            if new_pl[i][movIndex + 1] == 0:
                new_pl[i][movIndex + 1] = new_pl[i][movIndex]
                new_pl[i][movIndex] = 0
    return new_pl
def move_left2(pl):
    new_pl = np.copy(pl)
    for i in range(0, 4):
        for movIndex in range(3, 0, -1):  # Iteracja od prawej do lewej strony planszy
            if new_pl[i][movIndex] == new_pl[i][movIndex - 1]:
                new_pl[i][movIndex - 1] = 2 * new_pl[i][movIndex]
                new_pl[i][movIndex] = 0
            if new_pl[i][movIndex - 1] == 0:
                new_pl[i][movIndex - 1] = new_pl[i][movIndex]
                new_pl[i][movIndex] = 0
 
    return new_pl
def move_left(pl):
    new_pl = np.copy(pl)
    for i in range(0, 4):
        for movIndex in range(1, 4):
            if new_pl[i][movIndex] != 0:
                targetIndex = movIndex
                while targetIndex > 0 and new_pl[i][targetIndex - 1] == 0:
                    new_pl[i][targetIndex - 1] = new_pl[i][targetIndex]
                    new_pl[i][targetIndex] = 0
                    targetIndex -= 1
                if targetIndex > 0 and new_pl[i][targetIndex - 1] == new_pl[i][targetIndex]:
                    new_pl[i][targetIndex - 1] *= 2
                    new_pl[i][targetIndex] = 0
    return new_pl
def move_right(pl):      
    flipped_pl = np.flip(pl, axis=1)
    moved_pl = move_left(flipped_pl)
    new_pl = np.flip(moved_pl, axis=1)
    return new_pl
def move_up(pl):    

    transposed_pl = np.transpose(pl)
    moved_pl = move_left(transposed_pl)
    new_pl = np.transpose(moved_pl)
    return new_pl
    
def move_down(pl):
    transposed_pl = np.transpose(pl)
    flipped_pl = np.flip(transposed_pl, axis=0)
    moved_pl = move_right(flipped_pl)
    new_pl = np.flip(moved_pl, axis=0)
    new_pl = np.transpose(new_pl)
    return new_pl

# Tworzenie planszy
plansza = np.zeros((4, 4))
value = [0,2, 4,0]  # Dostępne wartości dla nowych kafelków

# Wypełnianie planszy losowymi wartościami
for row in plansza:
    for i in range(len(row)):
        rand_int = random.randint(0, 3)
        row[i] = value[rand_int]

def showPlansza(plansza):
    plt.imshow(plansza, cmap='Greys', interpolation='nearest')
    for i in range(plansza.shape[0]):
        for j in range(plansza.shape[1]):
            plt.text(j, i, str(plansza[i, j]), ha='center', va='center', color='white')
    plt.xticks(np.arange(0, 4), np.arange(1, 5))
    plt.yticks(np.arange(0, 4), np.arange(1, 5))
    plt.xlabel('Kolumna')
    plt.ylabel('Wiersz')
    plt.title('Plansza 2048')
    plt.show()

    import matplotlib.pyplot as plt

print("Początkowa plansza:")
showPlansza(plansza)
while True :
    inputValue = input("Podaj litere: u- up, d - down, r - right , l - left , b -break")
    if inputValue == "u":
        plansza = move_up(plansza)
    elif inputValue == "d":
        plansza = move_down(plansza)
    elif inputValue == "r":
        plansza = move_right(plansza)
    elif inputValue == "l":
        plansza = move_left(plansza) 
    elif inputValue == "b":
        break
    showPlansza(plansza)
 