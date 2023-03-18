import pandas as pd
import numpy as np
from src.constants import size,boat1,boat2,boat3,boat4,boat


def own_board (size=size,boat1=boat1,boat2=boat2,boat3=boat3,boat4=boat4,boat=boat):
    '''
    Función que dado un tamaño N
    devuelve la visual de un tablero (Pandas Dataframe)
    con X barcos de Y tipo

    Los barcos por defecto son:
    - 4 barcos de tamaño 1
    - 3 barcos de tamaño 2
    - 2 barcos de tamaño 3
    - 1 barco de tamaño 4

    El barco por defecto es "\u26F4"
    '''
    nboard = size
    own_board = np.full((nboard,nboard),0)
    n_boats1 = 0
    n_boats2 = 0
    n_boats3 = 0
    n_boats4 = 0
    while True:
        rng1 = np.random.randint(0, nboard)
        rng2 = np.random.randint(0, nboard)
        orientation = np.random.randint(1,3)
        if orientation == 1:
            barco_2 = np.full((1, 2),boat)
            barco_3 = np.full((1, 3),boat)
            barco_4 = np.full((1, 4),boat)
            size_until_border = own_board[rng1:rng1+1, rng2-1:-1]
            while (own_board[rng1,rng2] != boat)&(n_boats1<boat1):
                own_board[rng1,rng2]=boat
                n_boats1+=1
            while (own_board[rng1,rng2] != boat) & (len(barco_2[0])<=len(size_until_border[0])) & (boat not in size_until_border)&(n_boats2<boat2):
                own_board[rng1:rng1+1, rng2:len(barco_2[0])+rng2]= barco_2
                n_boats2+=1         
            while (own_board[rng1,rng2] != boat) & (len(barco_3[0])<=len(size_until_border[0])) & (boat not in size_until_border)&(n_boats3<boat3):
                own_board[rng1:rng1+1, rng2:len(barco_3[0])+rng2]= barco_3
                n_boats3+=1
            while (own_board[rng1,rng2] != boat) & (len(barco_4[0])<=len(size_until_border[0])) & (boat not in size_until_border)&(n_boats4<boat4):
                own_board[rng1:rng1+1, rng2:len(barco_4[0])+rng2]= barco_4
                n_boats4+=1
        elif orientation == 2:
            barco_2 = np.full((2, 1),boat)
            barco_3 = np.full((3, 1),boat)
            barco_4 = np.full((4, 1),boat)
            size_until_border = own_board[rng1-1:-1, rng2:rng2+1]
            while (own_board[rng1,rng2] != boat)&(n_boats1<boat1):
                own_board[rng1,rng2]=boat
                n_boats1+=1
            while (own_board[rng1,rng2] != boat) & (len(barco_2)<=len(size_until_border)) & (boat not in size_until_border)&(n_boats2<boat2):
                    own_board[rng1:rng1+len(barco_2), rng2:rng2+1]= barco_2
                    n_boats2+=1         
            while (own_board[rng1,rng2] != boat) & (len(barco_3)<=len(size_until_border)) & (boat not in size_until_border)&(n_boats3<boat3):
                own_board[rng1:rng1+len(barco_3), rng2:rng2+1]= barco_3
                n_boats3+=1
            while (own_board[rng1,rng2] != boat) & (len(barco_4)<=len(size_until_border)) & (boat not in size_until_border)&(n_boats4<boat4):
                own_board[rng1:rng1+len(barco_4), rng2:rng2+1]= barco_4
                n_boats4+=1

        if (n_boats1 == boat1)&(n_boats2 == boat2)&(n_boats3 == boat3)&(n_boats4 == boat4):
            break
    return own_board

def enemy_board(size=size,boat1=boat1,boat2=boat2,boat3=boat3,boat4=boat4,boat=boat):
    '''
    Función hermana de own_board

    Función que dado un tamaño n
    devuelve un tablero (Pandas Dataframe) SIN VISUAL
    con X barcos de Y tipo

    Los barcos por defecto son:
    - 4 barcos de tamaño 1
    - 3 barcos de tamaño 2
    - 2 barcos de tamaño 3
    - 1 barco de tamaño 4

    El barco por defecto es "\u26F4"
    '''
    nboard = size
    enemy_board = np.full((nboard,nboard),0)
    n_boats1 = 0
    n_boats2 = 0
    n_boats3 = 0
    n_boats4 = 0
    while True:
        rng1 = np.random.randint(0, nboard)
        rng2 = np.random.randint(0, nboard)
        orientation = np.random.randint(1,3)
        if orientation == 1:
            barco_2 = np.full((1, 2),boat)
            barco_3 = np.full((1, 3),boat)
            barco_4 = np.full((1, 4),boat)
            size_until_border = enemy_board[rng1:rng1+1, rng2-1:-1]
            while (enemy_board[rng1,rng2] != boat)&(n_boats1<boat1):
                enemy_board[rng1,rng2]=boat
                n_boats1+=1
            while (enemy_board[rng1,rng2] != boat) & (len(barco_2[0])<=len(size_until_border[0])) & (boat not in size_until_border)&(n_boats2<boat2):
                enemy_board[rng1:rng1+1, rng2:len(barco_2[0])+rng2]= barco_2
                n_boats2+=1         
            while (enemy_board[rng1,rng2] != boat) & (len(barco_3[0])<=len(size_until_border[0])) & (boat not in size_until_border)&(n_boats3<boat3):
                enemy_board[rng1:rng1+1, rng2:len(barco_3[0])+rng2]= barco_3
                n_boats3+=1
            while (enemy_board[rng1,rng2] != boat) & (len(barco_4[0])<=len(size_until_border[0])) & (boat not in size_until_border)&(n_boats4<boat4):
                enemy_board[rng1:rng1+1, rng2:len(barco_4[0])+rng2]= barco_4
                n_boats4+=1
        elif orientation == 2:
            barco_2 = np.full((2, 1),boat)
            barco_3 = np.full((3, 1),boat)
            barco_4 = np.full((4, 1),boat)
            size_until_border = enemy_board[rng1-1:-1, rng2:rng2+1]
            while (enemy_board[rng1,rng2] != boat)&(n_boats1<boat1):
                enemy_board[rng1,rng2]=boat
                n_boats1+=1
            while (enemy_board[rng1,rng2] != boat) & (len(barco_2)<=len(size_until_border)) & (boat not in size_until_border)&(n_boats2<boat2):
                    enemy_board[rng1:rng1+len(barco_2), rng2:rng2+1]= barco_2
                    n_boats2+=1         
            while (enemy_board[rng1,rng2] != boat) & (len(barco_3)<=len(size_until_border)) & (boat not in size_until_border)&(n_boats3<boat3):
                enemy_board[rng1:rng1+len(barco_3), rng2:rng2+1]= barco_3
                n_boats3+=1
            while (enemy_board[rng1,rng2] != boat) & (len(barco_4)<=len(size_until_border)) & (boat not in size_until_border)&(n_boats4<boat4):
                enemy_board[rng1:rng1+len(barco_4), rng2:rng2+1]= barco_4
                n_boats4+=1

        if (n_boats1 == boat1)&(n_boats2 == boat2)&(n_boats3 == boat3)&(n_boats4 == boat4):
            break
    return enemy_board

def blank_board(size=size):
    nboard = size
    board_blank = np.full((nboard,nboard),0)
    return board_blank
