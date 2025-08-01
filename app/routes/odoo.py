import xmlrpc.client
from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Task

odoo_bp = Blueprint('odoo', __name__, url_prefix='/odoo')

@odoo_bp.route('/send/<int:task_id>')
@login_required
def send_task_to_odoo(task_id):
    task = Task.query.get_or_404(task_id)

    # Configuración de conexión
    url = 'http://localhost:8069'
    db = 'odoo'  # Nombre de tu base Odoo
    username = 'admin'  # Usuario Odoo
    password = 'admin'  # Contraseña Odoo

    try:
        common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
        uid = common.authenticate(db, username, password, {})

        models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

        models.execute_kw(db, uid, password, 'rick.task', 'create', [{
            'title': task.title,
            'description': task.description,
            'due_date': str(task.due_date),
            'status': task.status.lower().replace(" ", "_"),
            'character_name': task.character_name,
            'character_image': task.character_image
        }])

        flash("Tarea enviada a Odoo correctamente.")
    except Exception as e:
        print("Error:", e)
        flash("Error al conectar con Odoo.")

    return redirect(url_for('tasks.task_list'))
