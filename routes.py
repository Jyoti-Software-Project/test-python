from flask import Blueprint, render_template, request, redirect, url_for
from controller import get_items, add_item, delete_item

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    items = get_items()
    return render_template("index.html", items=items)

@routes.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    add_item(name)
    return redirect(url_for('routes.index'))

@routes.route('/delete/<int:item_id>')
def delete(item_id):
    delete_item(item_id)
    return redirect(url_for('routes.index'))
