from models.notifications import Notifications

class NotificationDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_notifications(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM notifications")
        notifications = cur.fetchall()
        cur.close()
        return [Notifications(notification_id=row[0], sensor_id=row[1], message=row[2], 
                    timestamp=row[3]) for row in notifications]
    
    def insert_notifications(self, notifications):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO notifications (sensor_id, message, timestamp) VALUES (%s, %s, %s)", 
                    (notifications['sensor_id'], notifications['message'], notifications['timestamp']))
        self.mysql.connection.commit()
        cur.close()

    def update_notifications(self, notification_id, notifications):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE notifications SET sensor_id = %s, message = %s, timestamp = %s WHERE notification_id = %s", 
                    (notifications['sensor_id'], notifications['message'], notifications['timestamp'], notification_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_notifications(self, notification_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM notifications WHERE notification_id = %s", (notification_id,))
        self.mysql.connection.commit()
        cur.close()