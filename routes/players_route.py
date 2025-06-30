from flask import render_template
from sqlalchemy import select

from app import app
from models import Player
from settings import Session


@app.route("/player", methods=["GET", "POST"])
def player():
    with Session() as session:
        stmt = select(Player)
        teams = session.scalars(stmt)
        print(teams)
        return render_template(
            "player.html",
            teams=teams
        )

@app.route("/players/<team_name>")
def simple(team_name):
    with Session() as session:
        stmt = select(Player).where(Player.name == team_name)
        player = session.scalars(stmt).first()
    return render_template("/players/simple.html", player=player)