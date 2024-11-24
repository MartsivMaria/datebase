from flask import Flask
from config import Config 
from controller.objects_controller import create_objects_controller
from controller.users_controller import create_users_controller
from controller.notifications_controller import create_notifications_controller
from controller.sensor_notification_controller import create_sensor_notification_controller
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)

objects_controller = create_objects_controller(mysql)
app.register_blueprint(objects_controller)

users_controller = create_users_controller(mysql)
app.register_blueprint(users_controller)

notifications_controller = create_notifications_controller(mysql)
app.register_blueprint(notifications_controller)

sensor_notification_controller = create_sensor_notification_controller(mysql)
app.register_blueprint(sensor_notification_controller)

if __name__ == '__main__':
    app.run(debug=True)