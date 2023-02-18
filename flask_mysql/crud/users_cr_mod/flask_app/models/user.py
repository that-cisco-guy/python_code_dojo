from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def read_users(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def show_user(cls,data):
        query  = 'SELECT * FROM users WHERE id = %(id)s;'
        result = connectToMySQL('users_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def create_user(cls, data):
        query = '''INSERT INTO users (first_name, last_name, email) 
            VALUES(%(first_name)s, %(last_name)s, %(email)s);'''
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def delete_user(cls, data):
        query = '''DELETE FROM users 
            WHERE id = %(id)s;'''
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)