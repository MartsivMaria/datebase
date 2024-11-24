class Notifications:
    def __init__(self, notification_id, sensor_id, message, timestamp):
        self.notification_id = notification_id
        self.sensor_id = sensor_id
        self.message = message
        self.timestamp = timestamp

    def  to_dict(self):
        return {
            "notification_id": self.notification_id,
            "sensor_id": self.sensor_id,
            "message": self.message,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
        }
 