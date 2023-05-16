from zadanie1kolejka import Queue

def zabawaWZiemniaka(uczestnicy,liczbaOperacji):
    kolejka = Queue()
    for u in uczestnicy:
        kolejka.enqueue(u)

    while kolejka.size() > 1:
        for i in range(liczbaOperacji):
            kolejka.enqueue(kolejka.denqueue())
        kolejka.denqueue()

    return kolejka.denqueue()


uczestnicy = ["Jan","Paweł","Ignacy","Agata","Maurycy","Ludwik","Małgorzata"]

liczbaOperacji = int(input("Podaj liczbę operacji po których należy wyeliminować uczestnika z gry:"))

print("Zwycięzcą jest "+str(zabawaWZiemniaka(uczestnicy,liczbaOperacji)))