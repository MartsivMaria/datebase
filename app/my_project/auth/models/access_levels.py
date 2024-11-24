class AccessLevels:
    def __init__(self, id, access_id, access_level, zone_id):
        self.id = id
        self.access_id = access_id
        self.access_level = access_level
        self.zone_id = zone_id

    def  to_dict(self):
        return {
            "id": self.id,
            "access_id": self.access_id,
            "access_level": self.access_level,
            "zone_id": self.zone_id,
        }
 