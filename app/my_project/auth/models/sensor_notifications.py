class SensorNotifications:
    def __init__(self, id, notification_id, status, timestamp):
        self.id = id
        self.notification_id = notification_id
        self.status = status
        self.timestamp = timestamp

    def  to_dict(self):
        return {
            "id": self.id,
            "notification_id": self.notification_id,
            "status": self.status,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
        }
 