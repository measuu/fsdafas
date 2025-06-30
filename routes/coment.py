from flask import flash, redirect, render_template, request, session, url_for
from markupsafe import escape

from app import app

reviews = []


@app.route("/coment", methods=["GET", "POST"])
def coment():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if name and email and message:
            reviews.append(
                {
                    "name": escape(name),
                    "email": escape(email),
                    "message": escape(message),
                }
            )
            return redirect(url_for("review"))

    return render_template("coment.html")


@app.route("/review")
def review():
    return render_template("review.html", reviews=reviews)


if __name__ == "__main__":
    app.run(debug=True)
