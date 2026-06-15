from flask import Flask, render_template, request, redirect, url_for, session, flash
import db

app = Flask(__name__)
app.secret_key = "rekrutacja_pwr_secret"

# ==================== AUTH ====================

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        haslo = request.form["haslo"]
        rola = request.form["rola"]

        if rola == "kandydat":
            user = db.login_candidate(email, haslo)
            if user:
                session["user_id"] = user["IdKandydata"]
                session["rola"] = "kandydat"
                session["imie"] = user["ImieKD"]
                return redirect(url_for("candidate_panel"))
        else:
            user = db.login_worker(email, haslo)
            if user:
                session["user_id"] = user["IdPracownika"]
                session["rola"] = "pracownik"
                session["imie"] = user["ImiePC"]
                return redirect(url_for("worker_panel"))

        flash("Nieprawidłowy email lub hasło.")
    return render_template("login.html")

@app.route("/rejestracja", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            db.register_candidate(request.form)
            flash("Konto utworzone. Możesz się zalogować.")
            return redirect(url_for("login"))
        except Exception as e:
            flash(f"Błąd rejestracji: {e}")
    return render_template("register.html")

@app.route("/wyloguj")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ==================== KANDYDAT ====================

def require_candidate():
    if session.get("rola") != "kandydat":
        return redirect(url_for("login"))

@app.route("/kandydat")
def candidate_panel():
    if session.get("rola") != "kandydat":
        return redirect(url_for("login"))
    kandydat = db.get_candidate(session["user_id"])
    wyniki = db.get_wyniki(session["user_id"])
    osiagniecia = db.get_osiagniecia(session["user_id"])
    aplikacje = db.get_aplikacje_kandydata(session["user_id"])
    egzaminy = db.get_all_egzaminy()
    kierunki = db.get_kierunki()
    return render_template("candidate.html",
        kandydat=kandydat, wyniki=wyniki, osiagniecia=osiagniecia,
        aplikacje=aplikacje, egzaminy=egzaminy, kierunki=kierunki)

@app.route("/kandydat/dane", methods=["POST"])
def update_dane():
    if session.get("rola") != "kandydat":
        return redirect(url_for("login"))
    db.update_candidate(session["user_id"], request.form)
    flash("Dane zaktualizowane.")
    return redirect(url_for("candidate_panel"))

@app.route("/kandydat/wynik", methods=["POST"])
def add_wynik():
    if session.get("rola") != "kandydat":
        return redirect(url_for("login"))
    db.add_wynik(session["user_id"], request.form["id_egzaminu"], request.form["wartosc"])
    flash("Wynik dodany.")
    return redirect(url_for("candidate_panel"))

@app.route("/kandydat/osiagniecie", methods=["POST"])
def add_osiagniecie():
    if session.get("rola") != "kandydat":
        return redirect(url_for("login"))
    db.add_osiagniecie(session["user_id"], request.form)
    flash("Osiągnięcie dodane.")
    return redirect(url_for("candidate_panel"))

@app.route("/kandydat/aplikacja", methods=["POST"])
def add_aplikacja():
    if session.get("rola") != "kandydat":
        return redirect(url_for("login"))
    ok = db.add_aplikacja(session["user_id"], request.form["id_kierunku"], request.form["priorytet"])
    flash("Aplikacja złożona." if ok else "Już aplikowałeś na ten kierunek.")
    return redirect(url_for("candidate_panel"))

@app.route("/kandydat/wycofaj/<int:id_kierunku>")
def wycofaj(id_kierunku):
    if session.get("rola") != "kandydat":
        return redirect(url_for("login"))
    db.wycofaj_aplikacje(session["user_id"], id_kierunku)
    flash("Aplikacja wycofana.")
    return redirect(url_for("candidate_panel"))

# ==================== PRACOWNIK ====================

@app.route("/pracownik")
def worker_panel():
    if session.get("rola") != "pracownik":
        return redirect(url_for("login"))
    kandydaci = db.get_all_kandydaci()
    aplikacje = db.get_all_aplikacje()
    kierunki = db.get_kierunki()
    return render_template("worker.html",
        kandydaci=kandydaci, aplikacje=aplikacje, kierunki=kierunki)

@app.route("/pracownik/kandydat/<int:id_kandydata>")
def kandydat_detail(id_kandydata):
    if session.get("rola") != "pracownik":
        return redirect(url_for("login"))
    kandydat = db.get_kandydat_full(id_kandydata)
    return render_template("kandydat_detail.html", kandydat=kandydat)

@app.route("/pracownik/zatwierdz_wynik/<int:id_kandydata>/<int:id_egzaminu>")
def zatwierdz_wynik(id_kandydata, id_egzaminu):
    if session.get("rola") != "pracownik":
        return redirect(url_for("login"))
    db.zatwierdz_wynik(id_kandydata, id_egzaminu)
    flash("Wynik zatwierdzony.")
    return redirect(url_for("kandydat_detail", id_kandydata=id_kandydata))

@app.route("/pracownik/zatwierdz_osiagniecie/<int:id_osiagniecia>/<int:id_kandydata>")
def zatwierdz_osiagniecie(id_osiagniecia, id_kandydata):
    if session.get("rola") != "pracownik":
        return redirect(url_for("login"))
    db.zatwierdz_osiagniecie(id_osiagniecia)
    flash("Osiągnięcie zatwierdzone.")
    return redirect(url_for("kandydat_detail", id_kandydata=id_kandydata))

@app.route("/pracownik/zatwierdz_aplikacje/<int:id_kandydata>/<int:id_kierunku>")
def zatwierdz_aplikacje(id_kandydata, id_kierunku):
    if session.get("rola") != "pracownik":
        return redirect(url_for("login"))
    db.zatwierdz_aplikacje(id_kandydata, id_kierunku, session["user_id"])
    flash("Aplikacja zatwierdzona.")
    return redirect(url_for("worker_panel"))

@app.route("/pracownik/zamknij_rekrutacje", methods=["POST"])
def zamknij_rekrutacje():
    if session.get("rola") != "pracownik":
        return redirect(url_for("login"))
    db.zamknij_rekrutacje()
    flash("Rekrutacja zamknięta. Przydzielono miejsca na podstawie punktów.")
    return redirect(url_for("worker_panel"))

@app.route("/pracownik/raport")
def raport():
    if session.get("rola") != "pracownik":
        return redirect(url_for("login"))
    id_kierunku = request.args.get("kierunek")
    kierunki = db.get_kierunki()
    przyjeci = db.raport_przyjętych(id_kierunku)
    return render_template("raport.html", przyjeci=przyjeci, kierunki=kierunki, wybrany=id_kierunku)

if __name__ == "__main__":
    app.run(debug=True)
