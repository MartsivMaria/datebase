from flask import Blueprint, jsonify
from services.sensor_notification_service import SensorNotificationService

def create_sensor_notification_controller(mysql):
    sensor_notification_controller = Blueprint('sensor_notification', __name__)
    service = SensorNotificationService(mysql)

    @sensor_notification_controller.route('/sensors_notifications', methods=['GET'])
    def get_sensors_notifications():
        try:
            grouped_data = service.get_all_sensors_notifications()

            return jsonify(grouped_data)  
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return sensor_notification_controller
