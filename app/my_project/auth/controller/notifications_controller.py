from flask import Blueprint, request, jsonify
from services.notifications_service import NotificationService

def create_notifications_controller(mysql):
    notifications_controller = Blueprint('notifications', __name__)
    service = NotificationService(mysql)

    @notifications_controller.route('/notifications', methods=['GET'])
    def get_notifications():
        notifications = service.get_notifications()
        return jsonify([notification.to_dict() for notification in notifications])
    
    @notifications_controller.route('/notifications', methods=['POST'])
    def create_notifications():
        data = request.json
        if not data or 'sensor_id' not in data or 'message' not in data or 'timestamp' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_notifications(data)
            return jsonify({"message": "notification created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @notifications_controller.route('/notifications/<int:notification_id>', methods=['PUT'])
    def update_notifications(notification_id):
        data = request.json
        if not data or 'sensor_id' not in data or 'message' not in data or 'timestamp' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_notifications(notification_id, data)
            return jsonify({"message": "notification updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @notifications_controller.route('/notifications/<int:notification_id>', methods=['DELETE'])
    def delete_notifications(notification_id):
        try:
            service.remove_notifications(notification_id)
            return jsonify({"message": "notification deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    return notifications_controller