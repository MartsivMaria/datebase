class Rooms:
    def __init__(self, id, room_id, object_id, name):
        self.id = id
        self.room_id = room_id
        self.object_id = object_id
        self.name = name


    def  to_dict(self):
        return {
            "id": self.id,
            "room_id": self.room_id,
            "object_id": self.object_id,
            "name": self.name,
        }