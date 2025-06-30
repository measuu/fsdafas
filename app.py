from flask import Flask
from flask_login import LoginManager
from flask_wtf import CSRFProtect

from models import User
from settings import DatabaseConfig, Session

app = Flask(__name__)
app.config.from_object(DatabaseConfig)

csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    user = User.get(user_id)
    return user


from routes.club_route import *
from routes.coment import *
from routes.cs import *
from routes.errors import *
from routes.main import *
from routes.players_route import *
from routes.users import *
from routes.we import *

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True, port=5050)
