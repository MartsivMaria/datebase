from models.sensor_notification import SensorNotification

class SensorNotificationDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_sensors_notifications(self):
        cur = self.mysql.connection.cursor()

        cur.execute("""
            SELECT s.sensor_id, s.type AS sensor_type, n.notification_id, n.message AS notification_message
            FROM sensors s
            JOIN sensor_notification sn ON s.sensor_id = sn.sensor_id
            JOIN notifications n ON sn.notification_id = n.notification_id
        """)
        result = cur.fetchall()
        cur.close()

        notifications_dict = {}

        for row in result:
            sensor_id = row[0]
            sensor_type = row[1]
            notification_id = row[2]
            notification_message = row[3]

            if notification_id not in notifications_dict:
                notifications_dict[notification_id] = {
                    'notification_message': notification_message,
                    'sensors': []
                }

            notifications_dict[notification_id]['sensors'].append({
                'sensor_id': sensor_id,
                'sensor_type': sensor_type
            })

        return [{'notification_id': notification_id, 
                 'notification_message': data['notification_message'],
                 'sensors': data['sensors']}
                for notification_id, data in notifications_dict.items()]
