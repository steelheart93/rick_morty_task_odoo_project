import xmlrpc.client
from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Task

odoo_bp = Blueprint('odoo', __name__, url_prefix='/odoo')

@odoo_bp.route('/send/<int:task_id>')
@login_required
def send_task_to_odoo(task_id):
    task = Task.query.get_or_404(task_id)

    # Configuración de Odoo
    url = 'http://localhost:8069'
    db = 'odoo_db'
    username = 'admin'
    password = 'admin'

    try:
        # Autenticación
        common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
        uid = common.authenticate(db, username, password, {})

        # Acceso a modelos
        models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

        result = models.execute_kw(db, uid, password, 'rick.task', 'create', [{
            'title': task.title,
            'description': task.description,
            'due_date': str(task.due_date),
            'status': task.status.lower().replace(" ", "_"),
            'character_name': task.character_name,
            'character_image': task.character_image,
        }])

        flash('Tarea enviada a Odoo correctamente.')
    except Exception as e:
        print(e)
        flash('Error al enviar tarea a Odoo.')

    return redirect(url_for('tasks.task_list'))
