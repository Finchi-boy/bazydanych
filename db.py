import sqlite3

DB_PATH = "database.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# --- AUTH ---


def register_candidate(dane):
    with get_conn() as conn:
        conn.execute(
            """
            INSERT INTO Kandydaci (NazwiskoKD, ImieKD, DrugieImieKD, PeselKD, DataUrodzeniaKD, TelefonKD, EmailKD, HasloKD)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                dane["nazwisko"],
                dane["imie"],
                dane.get("drugie_imie", ""),
                dane.get("pesel", ""),
                dane.get("data_urodzenia", ""),
                dane.get("telefon", ""),
                dane["email"],
                dane["haslo"],
            ),
        )


def login_candidate(email, haslo):
    with get_conn() as conn:
        row = conn.execute(
            "SELECT * FROM Kandydaci WHERE EmailKD=? AND HasloKD=?", (email, haslo)
        ).fetchone()
        return dict(row) if row else None


def login_worker(email, haslo):
    with get_conn() as conn:
        row = conn.execute(
            "SELECT * FROM Pracownicy WHERE EmailPC=? AND HasloPC=?", (email, haslo)
        ).fetchone()
        return dict(row) if row else None


# --- KANDYDAT ---


def get_candidate(id):
    with get_conn() as conn:
        row = conn.execute(
            "SELECT * FROM Kandydaci WHERE IdKandydata=?", (id,)
        ).fetchone()
        return dict(row) if row else None


def update_candidate(id, dane):
    with get_conn() as conn:
        conn.execute(
            """
            UPDATE Kandydaci SET NazwiskoKD=?, ImieKD=?, DrugieImieKD=?, PeselKD=?,
            DataUrodzeniaKD=?, TelefonKD=?, EmailKD=? WHERE IdKandydata=?
        """,
            (
                dane["nazwisko"],
                dane["imie"],
                dane.get("drugie_imie", ""),
                dane.get("pesel", ""),
                dane.get("data_urodzenia", ""),
                dane.get("telefon", ""),
                dane["email"],
                id,
            ),
        )


# --- WYNIKI ---


def get_wyniki(id_kandydata):
    with get_conn() as conn:
        rows = conn.execute(
            """
            SELECT W.*, E.NazwaE FROM Wyniki W
            JOIN Egzaminy E ON W.IdEgzaminu = E.IdEgzaminu
            WHERE W.IdKandydata=?
        """,
            (id_kandydata,),
        ).fetchall()
        return [dict(r) for r in rows]


def add_wynik(id_kandydata, id_egzaminu, wartosc):
    with get_conn() as conn:
        existing = conn.execute(
            "SELECT 1 FROM Wyniki WHERE IdKandydata=? AND IdEgzaminu=?",
            (id_kandydata, id_egzaminu),
        ).fetchone()
        if existing:
            conn.execute(
                "UPDATE Wyniki SET WartoscWN=?, StatusWN='oczekujacy' WHERE IdKandydata=? AND IdEgzaminu=?",
                (wartosc, id_kandydata, id_egzaminu),
            )
        else:
            conn.execute(
                "INSERT INTO Wyniki (IdKandydata, IdEgzaminu, WartoscWN, StatusWN) VALUES (?, ?, ?, 'oczekujacy')",
                (id_kandydata, id_egzaminu, wartosc),
            )


def get_all_egzaminy():
    with get_conn() as conn:
        rows = conn.execute("SELECT * FROM Egzaminy").fetchall()
        return [dict(r) for r in rows]


# --- OSIAGNIECIA ---


def get_osiagniecia(id_kandydata):
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT * FROM Osiagniecia WHERE IdKandydata=?", (id_kandydata,)
        ).fetchall()
        return [dict(r) for r in rows]


def add_osiagniecie(id_kandydata, dane):
    with get_conn() as conn:
        conn.execute(
            """
            INSERT INTO Osiagniecia (NazwaOS, TytulOS, PunktyOS, StatusOS, IdKandydata)
            VALUES (?, ?, ?, 'oczekujacy', ?)
        """,
            (dane["nazwa"], dane["tytul"], dane.get("punkty", 0), id_kandydata),
        )


# --- APLIKACJE ---


def get_kierunki():
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT K.*, W.NazwaWD FROM Kierunki K
            JOIN Wydzialy W ON K.IdWydzialu = W.IdWydzialu
        """).fetchall()
        return [dict(r) for r in rows]


def get_aplikacje_kandydata(id_kandydata):
    with get_conn() as conn:
        rows = conn.execute(
            """
            SELECT A.*, K.NazwaKR, K.PoziomKR FROM Aplikacje A
            JOIN Kierunki K ON A.IdKierunku = K.IdKierunku
            WHERE A.IdKandydata=?
            ORDER BY A.PriorytetA
        """,
            (id_kandydata,),
        ).fetchall()
        return [dict(r) for r in rows]


def add_aplikacja(id_kandydata, id_kierunku, priorytet):
    with get_conn() as conn:
        existing = conn.execute(
            "SELECT 1 FROM Aplikacje WHERE IdKandydata=? AND IdKierunku=?",
            (id_kandydata, id_kierunku),
        ).fetchone()
        if existing:
            return False
        from datetime import date

        conn.execute(
            """
            INSERT INTO Aplikacje (IdKandydata, IdKierunku, DataZgloszeniaA, PunktyA, OplataA, StatusA, PriorytetA)
            VALUES (?, ?, ?, 0, 0, 'złożona', ?)
        """,
            (id_kandydata, id_kierunku, date.today().isoformat(), priorytet),
        )
        return True


def wycofaj_aplikacje(id_kandydata, id_kierunku):
    with get_conn() as conn:
        conn.execute(
            "DELETE FROM Aplikacje WHERE IdKandydata=? AND IdKierunku=?",
            (id_kandydata, id_kierunku),
        )


# --- PRACOWNIK ---


def get_all_kandydaci():
    with get_conn() as conn:
        rows = conn.execute("SELECT * FROM Kandydaci ORDER BY NazwiskoKD").fetchall()
        return [dict(r) for r in rows]


def get_kandydat_full(id_kandydata):
    """Kandydat + jego wyniki + osiągniecia"""
    k = get_candidate(id_kandydata)
    k["wyniki"] = get_wyniki(id_kandydata)  # type: ignore
    k["osiagniecia"] = get_osiagniecia(id_kandydata)  # type: ignore
    k["aplikacje"] = get_aplikacje_kandydata(id_kandydata)  # type: ignore
    return k


def zatwierdz_wynik(id_kandydata, id_egzaminu):
    with get_conn() as conn:
        conn.execute(
            "UPDATE Wyniki SET StatusWN='zatwierdzony' WHERE IdKandydata=? AND IdEgzaminu=?",
            (id_kandydata, id_egzaminu),
        )


def zatwierdz_osiagniecie(id_osiagniecia):
    with get_conn() as conn:
        conn.execute(
            "UPDATE Osiagniecia SET StatusOS='zatwierdzony' WHERE IdOsiagniecia=?",
            (id_osiagniecia,),
        )


def zatwierdz_aplikacje(id_kandydata, id_kierunku, id_pracownika):
    with get_conn() as conn:
        conn.execute(
            """
            UPDATE Aplikacje SET StatusA='zatwierdzona', IdPracownika=?
            WHERE IdKandydata=? AND IdKierunku=?
        """,
            (id_pracownika, id_kandydata, id_kierunku),
        )


def get_all_aplikacje():
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT A.*, K.NazwiskoKD, K.ImieKD, KR.NazwaKR, KR.LimitMiejscKR
            FROM Aplikacje A
            JOIN Kandydaci K ON A.IdKandydata = K.IdKandydata
            JOIN Kierunki KR ON A.IdKierunku = KR.IdKierunku
            ORDER BY KR.NazwaKR, A.PunktyA DESC
        """).fetchall()
        return [dict(r) for r in rows]


def zamknij_rekrutacje():
    """Przyznaje przyjęcie/odrzucenie na podstawie punktów i limitu miejsc"""
    with get_conn() as conn:
        kierunki = conn.execute(
            "SELECT IdKierunku, LimitMiejscKR FROM Kierunki"
        ).fetchall()
        for k in kierunki:
            id_k, limit = k["IdKierunku"], k["LimitMiejscKR"]
            aplikacje = conn.execute(
                """
                SELECT IdKandydata FROM Aplikacje
                WHERE IdKierunku=? AND StatusA='zatwierdzona'
                ORDER BY PunktyA DESC
            """,
                (id_k,),
            ).fetchall()
            for i, a in enumerate(aplikacje):
                nowy_status = "przyjety" if i < limit else "nieprzyjety"
                conn.execute(
                    """
                    UPDATE Aplikacje SET StatusA=?
                    WHERE IdKandydata=? AND IdKierunku=?
                """,
                    (nowy_status, a["IdKandydata"], id_k),
                )


def raport_przyjętych(id_kierunku=None):
    with get_conn() as conn:
        query = """
            SELECT K.ImieKD, K.NazwiskoKD, K.EmailKD, KR.NazwaKR, A.PunktyA
            FROM Aplikacje A
            JOIN Kandydaci K ON A.IdKandydata = K.IdKandydata
            JOIN Kierunki KR ON A.IdKierunku = KR.IdKierunku
            WHERE A.StatusA='przyjety'
        """
        params = ()
        if id_kierunku:
            query += " AND A.IdKierunku=?"
            params = (id_kierunku,)
        query += " ORDER BY KR.NazwaKR, A.PunktyA DESC"
        rows = conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]
