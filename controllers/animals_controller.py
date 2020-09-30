from flask import Flask, render_template
from flask import Blueprint
from models.animal import animal
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", all_animals = animals)