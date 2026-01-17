class Sensors:
    def __init__(self, id, sensor_id, room_id, type):
        self.id = id
        self.sensor_id = sensor_id
        self.room_id = room_id
        self.type = type

    def  to_dict(self):
        return {
            "id": self.id,
            "sensor_id": self.sensor_id,
            "room_id": self.room_id,
            "type": self.type,
        }
 