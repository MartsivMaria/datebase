class Objects:
    def __init__(self, object_id, name, location):
        self.object_id = object_id
        self.name = name
        self.location = location


    def  to_dict(self):
        return {
            "object_id": self.object_id,
            "name": self.name,
            "location": self.location,
        }
 