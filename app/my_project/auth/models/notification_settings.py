class NotificationSettings:
    def __init__(self, id, user_id, notification_type, treshold):
        self.id = id
        self.user_id = user_id
        self.notification_type = notification_type
        self.treshold = treshold

    def  to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "notification_type": self.notification_type,
            "treshold": str(self.treshold),
        }
 