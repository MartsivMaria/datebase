class Users:
    def __init__(self, user_id, access_id, username, email):
        self.user_id = user_id
        self.access_id = access_id
        self.username = username
        self.email = email


    def  to_dict(self):
        return {
            "user_id": self.user_id,
            "access_id": self.access_id,
            "username": self.username,
            "email": self.email,
        }
 