from flask import Flask
from flask_restful import Api

from db_setup import db
from resources import Computers, SingleComputer

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
api = Api(app)

api.add_resource(Computers, "/api/computers/")
api.add_resource(SingleComputer, "/api/computers/<int:id>")


@app.before_request
def create_table():
    db.create_all()


@app.route("/")
def home():
    return "<h1>Welcome to the RESTfulDB Project</h1>"


if __name__ == "__main__":
    app.run()
