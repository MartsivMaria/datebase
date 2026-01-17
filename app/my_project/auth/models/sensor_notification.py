class SensorNotification:
    def __init__(self, sensor_id, notification_id, event_time):
        self.sensor_id = sensor_id
        self.notification_id = notification_id
        self.event_time = event_time


    def  to_dict(self):
        return {
            "sensor_id": self.sensor_id,
            "notification_id": self.notification_id,
            "event_time": self.event_time,
        }
 