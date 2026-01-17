from dao.users_dao import UsersDAO

class UsersService:
    def __init__(self, mysql):
        self.dao = UsersDAO(mysql)

    def get_users(self):
        return self.dao.get_all_users()

    def add_users(self, users):
        return self.dao.insert_users(users)

    def modify_users(self, user_id, users):
        return self.dao.update_users(user_id, users)

    def remove_users(self, user_id):
        return self.dao.delete_users(user_id)
    
    # Зв'язок М:1
    def get_users_with_threshold(self, user_id):
        return self.dao.get_users_with_threshold(user_id)