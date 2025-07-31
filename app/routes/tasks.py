from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from .. import db
from ..models import Task

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_bp.route('/')
@login_required
def task_list():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)

@tasks_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        status = request.form['status']
        new_task = Task(
            title=title,
            description=description,
            due_date=due_date,
            status=status,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('tasks.task_list'))
    return render_template('create_task.html')

@tasks_bp.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        return "No autorizado", 403
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.due_date = request.form['due_date']
        task.status = request.form['status']
        db.session.commit()
        return redirect(url_for('tasks.task_list'))
    return render_template('edit_task.html', task=task)

@tasks_bp.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        return "No autorizado", 403
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.task_list'))
