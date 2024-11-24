from models.objects import Objects

class ObjectsDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_objects(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM objects")
        objects = cur.fetchall()
        cur.close()
        return [Objects(object_id=row[0], name=row[1], 
            location=row[2]) for row in objects]
    
    def insert_objects(self, objects):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO objects (object_id, name, location) VALUES (%s, %s, %s)", 
                    (objects['object_id'], objects['name'], objects['location']))
        self.mysql.connection.commit()
        cur.close()

    def update_objects(self, object_id, objects):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE objects SET object_id = %s, name = %s, location = %s WHERE object_id = %s", 
                    (objects['object_id'], objects['name'], objects['location'], object_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_objects(self, object_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM objects WHERE object_id = %s", (object_id,))
        self.mysql.connection.commit()
        cur.close()