from dao.sensor_notification_dao import SensorNotificationDAO

class SensorNotificationService:
    def __init__(self, mysql):
        self.dao = SensorNotificationDAO(mysql)

    # Зв'язок М:М
    def get_all_sensors_notifications(self):
        return self.dao.get_all_sensors_notifications()