from models.users import Users

class UsersDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_users(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        cur.close()
        return [Users(*row).to_dict() for row in rows]

    def insert_users(self, users):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO users (access_id, username, email) VALUES (%s, %s, %s)", (users['access_id'], users['username'], users['email']))
        self.mysql.connection.commit()
        cur.close()

    def update_users(self, user_id, users):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE users SET username = %s, email = %s WHERE user_id = %s", (users['username'], users['email'], user_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_users(self, user_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        self.mysql.connection.commit()
        cur.close()

    def get_users_with_threshold(self, user_id):
        cur = self.mysql.connection.cursor()
        query = """
            SELECT u.user_id, u.username, u.email, ns.id, ns.threshold
            FROM users u
            LEFT JOIN notificationSettings ns ON u.user_id = ns.user_id
            WHERE u.user_id = %s
        """
        cur.execute(query, (user_id,))
        rows = cur.fetchall()
        cur.close()

        user_data = None
        thresholds = []
        for row in rows:
            if not user_data:
                user_data = {
                    "user_id": row[0],
                    "username": row[1],
                    "email": row[2]
                }
            if row[3]: 
                thresholds.append({
                    "user_id": row[3],
                    "threshold": row[4]
                })

        if user_data:
            user_data["threshold"] = thresholds
        return user_data
    