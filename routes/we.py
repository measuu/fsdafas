from flask import render_template

from app import app


@app.route("/we", methods=["GET", "POST"])
def we():
    return render_template("we.html")


if __name__ == "__main__":
    app.run(debug=True)
