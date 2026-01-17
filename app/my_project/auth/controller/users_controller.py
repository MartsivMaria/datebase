from flask import Blueprint, request, jsonify
from services.users_service import UsersService

def create_users_controller(mysql):
    users_controller = Blueprint('user', __name__)
    service = UsersService(mysql)

    @users_controller.route('/users', methods=['GET'])
    def get_users():
        users = service.get_users()
        return jsonify(users)
    
    @users_controller.route('/users', methods=['POST'])
    def create_users():
        data = request.json
        if not data or 'access_id' not in data or 'username' not in data or 'email' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_users(data)
            return jsonify({"message": "User created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @users_controller.route('/users/<int:user_id>', methods=['PUT'])
    def update_users(user_id):
        data = request.json
        if not data or 'username' not in data or 'email' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.modify_users(user_id, data)
            return jsonify({"message": "User updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @users_controller.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_users(user_id):
        try:
            service.remove_users(user_id)
            return jsonify({"message": "User deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @users_controller.route('/users/<int:user_id>/threshold', methods=['GET'])
    def get_users_with_threshold(user_id):
        try:
            user_with_threshold = service.get_users_with_threshold(user_id)
            return jsonify(user_with_threshold)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    return users_controller