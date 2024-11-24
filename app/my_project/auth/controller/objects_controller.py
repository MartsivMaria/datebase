from flask import Blueprint, request, jsonify
from services.objects_service import ObjectsService

def create_objects_controller(mysql):
    objects_controller = Blueprint('objects', __name__)
    service = ObjectsService(mysql)

    @objects_controller.route('/objects', methods=['GET'])
    def get_objects():
        objects = service.get_objects()
        return jsonify([objects.to_dict() for objects in objects])
    
    @objects_controller.route('/objects', methods=['POST'])
    def create_objects():

        data = request.json
        if not data or 'object_id' not in data or 'name' not in data or 'location' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_objects(data)
            return jsonify({"message": "Objects created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @objects_controller.route('/objects/<int:object_id>', methods=['PUT'])
    def update_objects(object_id):
        data = request.json
        if not data or 'object_id' not in data or 'name' not in data or 'location' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_objects(object_id, data)
            return jsonify({"message": "Objects updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @objects_controller.route('/objects/<int:object_id>', methods=['DELETE'])
    def delete_objects(object_id):
        try:
            service.remove_objects(object_id)
            return jsonify({"message": "Objects deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    return objects_controller