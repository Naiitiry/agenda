from flask import Blueprint, request, jsonify
from app.models import Task, db
from datetime import datetime, timedelta
from flask_jwt_extended import jwt_required, get_jwt_identity


tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/all_tasks',methods = ['GET'], endpoint='funcion1')
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    tasks_json = [
        {'id':task.id, 'title':task.title, 'description':task.description,
        'creation_date':task.creation_date, 'deadline':task.deadline,
        'complete':task.completed} for task in tasks
    ]
    return jsonify(tasks_json), 200

@tasks_bp.route('/create_tasks',methods = ['GET','POST'], endpoint='funcion2')
@jwt_required()
def create_task():
    data = request.get_json()
    user_id = get_jwt_identity()
    new_task = Task(
        title = data['title'],
        description = data.get('description'),
        deadline = datetime.fromisoformat(data['deadline']),
        user_id = user_id
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message':'Task created successfully'}), 201

@tasks_bp.route('/update_tasks/<int:task_id>', methods = ['GET','POST'], endpoint='funcion3')
@jwt_required()
def update_task(task_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    task = Task.query.get_or_404(task_id)
    if task.user_id != user_id:
        return jsonify({'message':'You do not have permission to update this task'}), 403
    
    # Aquí actualizas los campos de la tarea
    task.title = data['title']
    task.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'}), 200

@tasks_bp.route('/extend_tasks/<int:task_id>/extend', methods = ['POST'], endpoint='funcion4')
@jwt_required()
def extend_task(task_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    task = Task.query.get(task_id)
    if task.user_id != user_id:
        return jsonify({'message':'You do not have permission to update this task'}), 403
    # Extender el plazo de la tarea
    if 'days' in data:
        task.deadline += timedelta(days=data['days'])
        db.session.commit()
        return jsonify({'message': 'Task deadline extended'}), 200
    return jsonify({'message': 'Task not found'}), 404