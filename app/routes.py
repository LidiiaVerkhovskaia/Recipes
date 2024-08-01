from flask import Blueprint, render_template, flash, redirect, url_for, request
from app import db
from app.forms import *
from app.models import *
from urllib.parse import urlsplit

bp = Blueprint('routes', __name__)


@bp.route('/')
@bp.route('/recipes', methods=['GET', 'POST'])
def recipes():

    if request.args.get('delete') == "delete":
        recipe_id = request.args.get('recipe')

        recipe_on_del = Recipe.query.filter_by(id=int(recipe_id)).first()

        db.session.delete(recipe_on_del)
        db.session.commit()

    all_recipes = Recipe.query.all()

    return render_template('recipes.html', title='Recipes', recipes=all_recipes)


@bp.route('/recipe', methods=['GET', 'POST'])
def recipe():

    recipe_id = request.args.get('recipe')

    changed_recipe = Recipe.query.filter_by(id=int(recipe_id)).first()

    return render_template('recipe.html', title='recipe', recipe=changed_recipe)


@bp.route('/creator_recipe', methods=['GET', 'POST'])
def creator_recipe():

    form = RecipeForm()

    if form.validate_on_submit():
        recipe = Recipe(title=form.title.data, category=form.category.data, ingredients=form.ingredients.data,
                        steps=form.steps.data, time=form.time.data)

        db.session.add(recipe)
        db.session.commit()

        flash('Рецепт успешно добавлен!')

        return redirect(url_for('routes.recipes'))

    return render_template('creator_recipe.html', title="Creator_recipe", form=form)

