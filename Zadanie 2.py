import sqlite3

connect=sqlite3.connect('baza_danych')
connect.row_factory=sqlite3.Row

c=connect.cursor()

c.executescript("""
        DROP TABLE IF EXISTS ksiazka;
        CREATE TABLE IF NOT EXISTS ksiazka (
                id INTEGER PRIMARY KEY ASC,
                tytul varchar(250) NOT NULL,
                autor varchar(250) NOT NULL,
                rok varchar(250) NOT NULL
        )""")

ksiazki = (
        (None, 'Rok 1984', 'George Orwell', '1949')
)
c.execute('INSERT INTO ksiazka VALUES(?, ?, ?, ?);', ksiazki)



def addRow():
        tytul = input('Podaj tytuł książki: ')
        autor = input('Podaj imię i nazwisko autora: ')
        rok = input('Podaj rok wydania: ')
        c.execute('INSERT INTO ksiazka VALUES(NULL, ?, ?, ?);', (tytul, autor, rok))
        connect.commit()

def deleteRow():
        x = input("Podaj ID książki, którą chcesz usunąć. ")
        while True:
                print()
                y = input(f"Czy na pewno chcesz usunąć książkę o id {x} ? t/n ")
                if y == 't':
                        c.execute('DELETE FROM ksiazka WHERE id=?', x)
                        break
                elif y == 'n':
                        break
                else:
                        print("Błąd")

def editRow():
        x = int(input('Który wiersz chcesz edytować? Podaj jego ID. '))
        while True:
                print()
                y = int(input("Który element wiersza chcesz edytować?\n1. Tytuł\n2. Autor\n3. Rok wydania\n0. Koniec edycji\n"))
                if y == 1:
                        tytul = input('Wprowadź nowy tytuł: ')
                        c.execute("UPDATE ksiazka SET tytul=? WHERE id=?", (tytul, x,))
                elif y == 2:
                        autor = input('Wprowadź nowe imię i nazwisko autora: ')
                        c.execute('UPDATE ksiazka SET autor=? WHERE id=?', (autor, x,))
                elif y == 3:
                        rok = input('Wprowadź nowy rok wydania: ')
                        c.execute('UPDATE ksiazka SET rok=? WHERE id=?', (rok, x,))
                elif y == 0:
                        break
                else:
                        print("Błąd")

def showTable():
        c.execute("""
        SELECT * FROM ksiazka;
        """)
        ksiazki = c.fetchall()
        for ksiazka in ksiazki:
                print(ksiazka['id'], ksiazka['tytul'], ksiazka['autor'], ksiazka['rok'])



print("Wybierz opcję, którą ma wykonać program: \n1. Dodać wiersz do tabeli\n2. Usunąć wiersz z tabeli\n3. Wyświetlić dane\n4. Edytować wiersz\n0. Wyjście")
print()
option = int(input("Wybierz opcję od 0 do 4: "))
print()
while option != 0:
        if option == 1:
                addRow()
        elif option == 2:
                deleteRow()
        elif option == 3:
                showTable()
        elif option == 4:
                editRow()
        else:
                print()
                print("Błąd")
        
        print()
        print("Wybierz opcję, którą ma wykonać program: \n1. Dodać wiersz do tabeli\n2. Usunąć wiersz z tabeli\n3. Wyświetlić dane\n4. Edytować wiersz\n0. Wyjście")
        print()
        option = int(input("Wybierz opcję od 0 do 4: "))
        print()

c.close()
connect.close()