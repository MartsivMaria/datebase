from dao.objects_dao import ObjectsDAO

class ObjectsService:
    def __init__(self, mysql):
        self.dao = ObjectsDAO(mysql)

    def get_objects(self):
        return self.dao.get_all_objects()

    def add_objects(self, objects):
        return self.dao.insert_objects(objects)

    def modify_objects(self, object_id, objects):
        return self.dao.update_objects(object_id, objects)

    def remove_objects(self, object_id):
        return self.dao.delete_objects(object_id)