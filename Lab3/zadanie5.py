def Hanoi(rozmiar, miejsce_p, miejsce_d):
    if rozmiar == 1:
        print("Weź krążek 1 z patyka " + str(miejsce_p) + " na " + str(miejsce_d) + " patyk")
    else:
        miejsce_t = 6 - miejsce_p - miejsce_d
        Hanoi(rozmiar-1, miejsce_p, miejsce_t)
        print("Weź krążek " + str(rozmiar) + " z patyka " + str(miejsce_p) + " na " + str(miejsce_d) + " patyk")
        Hanoi(rozmiar-1, miejsce_t, miejsce_d)


Hanoi(5,1,2) # Przykładowe wywołanie funkcji dla 5 krążków o patyku początkowym 1, a patyku docelowym 2