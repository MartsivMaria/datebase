from dao.notifications_dao import NotificationDAO

class NotificationService:
    def __init__(self, mysql):
        self.dao = NotificationDAO(mysql)

    def get_notifications(self):
        return self.dao.get_all_notifications()

    def add_notifications(self, notifications):
        return self.dao.insert_notifications(notifications)

    def modify_notifications(self, notification_id, notifications):
        return self.dao.update_notifications(notification_id, notifications)

    def remove_notifications(self, notification_id):
        return self.dao.delete_notifications(notification_id)
