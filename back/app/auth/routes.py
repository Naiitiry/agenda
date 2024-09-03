from flask import Blueprint,request,jsonify
from app.models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token


auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    data = request.get_json()
    user = User(username=data['username'],email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message':'User registered successfully'}), 201

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        # Implementar token o sesión
        return jsonify(access_token = access_token), 200
    return jsonify({'message':'Invalid credentials'}), 401

@auth_bp.route('/logout',methods=['GET','POST'])
def logout():
    db.session.close()
    return jsonify({'message':'Logout succesfull'})