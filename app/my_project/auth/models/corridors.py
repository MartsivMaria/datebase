class Corridors:
    def __init__(self, id, corridor_id, object_id, name):
        self.id = id
        self.corridor_id = corridor_id
        self.object_id = object_id
        self.name = name


    def  to_dict(self):
        return {
            "id": self.id,
            "corridor_id": self.corridor_id,
            "object_id": self.object_id,
            "name": self.name,
        }