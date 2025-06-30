from flask import render_template

from app import app


@app.route("/cs", methods=["GET", "POST"])
def cs():
    return render_template("cs.html")


if __name__ == "__main__":
    app.run(debug=True)
