"""
Seed script - wypełnia bazę przykładowymi danymi testowymi.
Uruchom: python seed.py
"""

import sqlite3
from datetime import date

DB_PATH = "database.db"


def seed():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # --- WYDZIAŁY ---
    wydzialy = [
        (
            1,
            "Wydział Informatyki i Telekomunikacji",
            "ul. Wybrzeże Wyspiańskiego 27, Wrocław",
            "W4",
        ),
        (2, "Wydział Matematyki", "ul. Wybrzeże Wyspiańskiego 27, Wrocław", "W13"),
        (3, "Wydział Elektroniki", "ul. Wybrzeże Wyspiańskiego 27, Wrocław", "W4N"),
    ]
    cur.executemany("INSERT OR IGNORE INTO Wydzialy VALUES (?,?,?,?)", wydzialy)

    # --- KIERUNKI ---
    kierunki = [
        (1, "Informatyka", "INF", "inżynierskie", 120, 1),
        (2, "Informatyka stosowana", "INS", "inżynierskie", 80, 1),
        (3, "Cyberbezpieczeństwo", "CYB", "inżynierskie", 60, 1),
        (4, "Matematyka stosowana", "MAS", "inżynierskie", 50, 2),
        (5, "Elektronika i telekomunikacja", "ELT", "inżynierskie", 90, 3),
        (6, "Informatyka", "INF-M", "magisterskie", 40, 1),
    ]
    cur.executemany("INSERT OR IGNORE INTO Kierunki VALUES (?,?,?,?,?,?)", kierunki)

    # --- EGZAMINY ---
    egzaminy = [
        (1, "Matematyka rozszerzona"),
        (2, "Fizyka rozszerzona"),
        (3, "Informatyka rozszerzona"),
        (4, "Język angielski rozszerzony"),
    ]
    cur.executemany("INSERT OR IGNORE INTO Egzaminy VALUES (?,?)", egzaminy)

    # --- PRZELICZNIKI ---
    # (IdEgzaminu, IdKierunku, Mnoznik, Minimum)
    przeliczniki = [
        (1, 1, 1.5, 40.0),  # Matematyka → Informatyka
        (3, 1, 2.0, 30.0),  # Informatyka → Informatyka
        (2, 1, 1.0, 0.0),  # Fizyka → Informatyka (opcjonalna)
        (1, 2, 1.5, 40.0),
        (3, 2, 2.0, 30.0),
        (1, 3, 1.5, 40.0),
        (3, 3, 2.5, 35.0),
        (1, 4, 2.0, 50.0),
        (2, 4, 1.5, 30.0),
        (1, 5, 1.5, 40.0),
        (2, 5, 2.0, 35.0),
    ]
    cur.executemany("INSERT OR IGNORE INTO Przeliczniki VALUES (?,?,?,?)", przeliczniki)

    # --- PRACOWNICY ---
    pracownicy = [
        (1, "Kowalski", "Jan", "jan.kowalski@pwr.edu.pl", "admin123"),
        (2, "Nowak", "Anna", "anna.nowak@pwr.edu.pl", "admin123"),
        (3, "Wiśniewski", "Piotr", "p.wisniewski@pwr.edu.pl", "admin123"),
    ]
    cur.executemany("INSERT OR IGNORE INTO Pracownicy VALUES (?,?,?,?,?)", pracownicy)

    # --- KANDYDACI ---
    kandydaci = [
        (
            1,
            "Kowalczyk",
            "Marek",
            None,
            "03241512345",
            "2003-04-15",
            "501234567",
            "marek.kowalczyk@gmail.com",
            "haslo123",
        ),
        (
            2,
            "Nowak",
            "Julia",
            "Maria",
            "04050367890",
            "2004-05-03",
            "502345678",
            "julia.nowak@gmail.com",
            "haslo123",
        ),
        (
            3,
            "Wiśniewska",
            "Katarzyna",
            None,
            "03121598765",
            "2003-12-15",
            "503456789",
            "k.wisniewska@gmail.com",
            "haslo123",
        ),
        (
            4,
            "Zając",
            "Tomasz",
            None,
            "04070412345",
            "2004-07-04",
            "504567890",
            "tomasz.zajac@gmail.com",
            "haslo123",
        ),
        (
            5,
            "Lewandowski",
            "Michał",
            "Jan",
            "03091523456",
            "2003-09-15",
            "505678901",
            "m.lewandowski@gmail.com",
            "haslo123",
        ),
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO Kandydaci (IdKandydata,NazwiskoKD,ImieKD,DrugieImieKD,PeselKD,DataUrodzeniaKD,TelefonKD,EmailKD,HasloKD) VALUES (?,?,?,?,?,?,?,?,?)",
        kandydaci,
    )

    # --- WYNIKI ---
    wyniki = [
        # (IdKandydata, IdEgzaminu, Wartosc, Status, IdPracownika)
        (1, 1, 85.0, "zatwierdzony", 1),
        (1, 3, 90.0, "zatwierdzony", 1),
        (1, 4, 72.0, "oczekujacy", None),
        (2, 1, 78.0, "zatwierdzony", 1),
        (2, 2, 65.0, "zatwierdzony", 2),
        (2, 4, 88.0, "oczekujacy", None),
        (3, 1, 92.0, "zatwierdzony", 1),
        (3, 3, 95.0, "zatwierdzony", 2),
        (4, 1, 60.0, "oczekujacy", None),
        (4, 2, 55.0, "oczekujacy", None),
        (5, 1, 70.0, "zatwierdzony", 1),
        (5, 3, 75.0, "oczekujacy", None),
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO Wyniki (IdKandydata,IdEgzaminu,WartoscWN,StatusWN,IdPracownika) VALUES (?,?,?,?,?)",
        wyniki,
    )

    # --- OSIĄGNIĘCIA ---
    osiagniecia = [
        (
            1,
            "Olimpiada Informatyczna",
            "Laureat etapu okręgowego",
            15.0,
            "zatwierdzony",
            1,
            1,
        ),
        (2, "Olimpiada Matematyczna", "Finalista", 10.0, "zatwierdzony", 2, 2),
        (3, "Certyfikat językowy", "Cambridge C1", 5.0, "oczekujacy", 3, None),
        (4, "Hackhaton PWR", "II miejsce", 8.0, "oczekujacy", 4, None),
        (
            5,
            "Olimpiada Fizyczna",
            "Laureat etapu okręgowego",
            15.0,
            "zatwierdzony",
            5,
            1,
        ),
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO Osiagniecia (IdOsiagniecia,NazwaOS,TytulOS,PunktyOS,StatusOS,IdKandydata,IdPracownika) VALUES (?,?,?,?,?,?,?)",
        osiagniecia,
    )

    # --- APLIKACJE ---
    # Punkty = suma (wynik * mnoznik) dla zatwierdzonych wyników
    # Marek: mat 85*1.5 + inf 90*2.0 = 127.5 + 180 = 307.5
    # Julia: mat 78*1.5 + fiz 65*1.0 = 117 + 65 = 182  (→ INS)
    # Katarzyna: mat 92*1.5 + inf 95*2.0 = 138 + 190 = 328
    # Tomasz: brak zatwierdzonych → 0
    # Michał: mat 70*1.5 = 105
    aplikacje = [
        # (IdKandydata, IdKierunku, Data, Punkty, Oplata, Status, Priorytet, IdPracownika)
        (1, 1, "2025-06-01", 307.5, 85.0, "zatwierdzona", 1, 1),
        (1, 3, "2025-06-01", 307.5, 85.0, "złożona", 2, None),
        (2, 2, "2025-06-02", 182.0, 85.0, "zatwierdzona", 1, 1),
        (3, 1, "2025-06-01", 328.0, 85.0, "zatwierdzona", 1, 2),
        (4, 1, "2025-06-03", 0.0, 85.0, "złożona", 1, None),
        (5, 1, "2025-06-02", 105.0, 85.0, "zatwierdzona", 1, 1),
        (5, 2, "2025-06-02", 105.0, 85.0, "złożona", 2, None),
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO Aplikacje (IdKandydata,IdKierunku,DataZgloszeniaA,PunktyA,OplataA,StatusA,PriorytetA,IdPracownika) VALUES (?,?,?,?,?,?,?,?)",
        aplikacje,
    )

    conn.commit()
    conn.close()
    print("✓ Dane testowe dodane pomyślnie!")
    print()
    print("=== KONTA TESTOWE ===")
    print()
    print("PRACOWNICY (email / hasło):")
    print("  jan.kowalski@pwr.edu.pl   / admin123")
    print("  anna.nowak@pwr.edu.pl     / admin123")
    print()
    print("KANDYDACI (email / hasło):")
    print("  marek.kowalczyk@gmail.com / haslo123")
    print("  julia.nowak@gmail.com     / haslo123")
    print("  k.wisniewska@gmail.com    / haslo123")
    print("  tomasz.zajac@gmail.com    / haslo123  (brak zatwierdzonych wyników)")
    print("  m.lewandowski@gmail.com   / haslo123")


if __name__ == "__main__":
    seed()
