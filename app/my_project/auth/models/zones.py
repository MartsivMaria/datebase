class Zones:
    def __init__(self, id, zone_id, object_id, name):
        self.id = id
        self.zone_id = zone_id
        self.object_id = object_id
        self.name = name

    def  to_dict(self):
        return {
            "id": self.id,
            "zone_id": self.zone_id,
            "object_id": self.object_id,
            "name": self.name,
        }
 