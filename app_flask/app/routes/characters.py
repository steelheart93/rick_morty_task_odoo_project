from flask import Blueprint, render_template, request, redirect, url_for
import requests
from flask_login import login_required, current_user
from ..models import Task
from .. import db

characters_bp = Blueprint('characters', __name__, url_prefix='/characters')

API_URL = "https://rickandmortyapi.com/api/character"

@characters_bp.route('/')
@login_required
def character_list():
    page = request.args.get('page', 1, type=int)
    response = requests.get(f"{API_URL}?page={page}")
    data = response.json()

    return render_template('characters.html', characters=data['results'], page=page, pages=data['info']['pages'])

@characters_bp.route('/assign/<int:character_id>/<int:task_id>')
@login_required
def assign_character(character_id, task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        return "No autorizado", 403

    response = requests.get(f"{API_URL}/{character_id}")
    if response.status_code != 200:
        return "Personaje no encontrado", 404

    char = response.json()
    task.character_id = char['id']
    task.character_name = char['name']
    task.character_image = char['image']
    db.session.commit()

    return redirect(url_for('tasks.task_list'))
