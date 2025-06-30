from datetime import datetime

from flask import flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required
from sqlalchemy import select

from app import app
from models import Team
from settings import Session, config


@app.route("/club", methods=["GET", "POST"])
def club():
    with Session() as session:
        stmt = select(Team).where(Team.id == 1)
        team = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Team).where(Team.id == 2)
        team1 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Team).where(Team.id == 3)
        team2 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Team).where(Team.id == 4)
        team3 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Team).where(Team.id == 5)
        team4 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Team).where(Team.id == 6)
        team5 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Team).where(Team.id == 7)
        team6 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Team).where(Team.id == 8)
        team7 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Team).where(Team.id == 9)
        team8 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Team).where(Team.id == 10)
        team9 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Team).where(Team.id == 11)
        team10 = session.scalars(stmt).first()
    with Session() as session:
        stmt = select(Team).where(Team.id == 12)
        team11 = session.scalars(stmt).first()
    return render_template(
        "club.html",
        team=team,
        team1=team1,
        team2=team2,
        team3=team3,
        team4=team4,
        team5=team5,
        team6=team6,
        team7=team7,
        team8=team8,
        team9=team9,
        team10=team10,
        team11=team11,
    )


@app.route("/navi")
def navi():
    with Session() as session:
        stmt = select(Team).where(Team.id == 1)
        team = session.scalars(stmt).first()
    return render_template("/clubs/Navi.html", team=team)


@app.route("/fnatic")
def fnatic():
    with Session() as session:
        stmt = select(Team).where(Team.id == 2)
        team = session.scalars(stmt).first()
    return render_template("/clubs/Fnatic.html", team=team)


@app.route("/nip")
def nip():
    with Session() as session:
        stmt = select(Team).where(Team.id == 3)
        team = session.scalars(stmt).first()
    return render_template("/clubs/Nip.html", team=team)


@app.route("/cloude9")
def cloude9():
    with Session() as session:
        stmt = select(Team).where(Team.id == 4)
        team = session.scalars(stmt).first()
    return render_template("/clubs/Cloude9.html", team=team)


@app.route("/astralis")
def astralis():
    with Session() as session:
        stmt = select(Team).where(Team.id == 5)
        team = session.scalars(stmt).first()
    return render_template("/clubs/Astralis.html", team=team)


@app.route("/mouz")
def mouz():
    with Session() as session:
        stmt = select(Team).where(Team.id == 6)
        team = session.scalars(stmt).first()
    return render_template("/clubs/Mouz.html", team=team)


@app.route("/gambit")
def gambit():
    with Session() as session:
        stmt = select(Team).where(Team.id == 7)
        team = session.scalars(stmt).first()
    return render_template("/clubs/Gambit.html", team=team)


@app.route("/vitality")
def vitality():
    with Session() as session:
        stmt = select(Team).where(Team.id == 8)
        team = session.scalars(stmt).first()
    return render_template("/clubs/Vitality.html", team=team)


@app.route("/g2")
def g2():
    with Session() as session:
        stmt = select(Team).where(Team.id == 9)
        team = session.scalars(stmt).first()
    return render_template("/clubs/G2.html", team=team)


@app.route("/faze")
def faze():
    with Session() as session:
        stmt = select(Team).where(Team.id == 10)
        team = session.scalars(stmt).first()
    return render_template("/clubs/Faze.html", team=team)


@app.route("/liquid")
def liquid():
    with Session() as session:
        stmt = select(Team).where(Team.id == 11)
        team = session.scalars(stmt).first()
    return render_template("/clubs/Liquid.html", team=team)


@app.route("/virtus")
def virtus():
    with Session() as session:
        stmt = select(Team).where(Team.id == 12)
        team = session.scalars(stmt).first()
    return render_template("/clubs/Virtus.html", team=team)


if __name__ == "__main__":
    app.run(debug=True)
