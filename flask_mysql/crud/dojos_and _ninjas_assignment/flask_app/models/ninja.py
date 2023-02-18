from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = 'dojos_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def all_ninjas(cls):
        query = '''SELECT * FROM ninjas 
        LEFT JOIN dojos ON dojos.ninja_id = ninja_id 
        WHERE dojos.id = %(id);'''
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def add_ninja(cls,data):
        query = '''INSERT INTO ninjas (first_name, last_name, age, dojo_id)
            VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)'''
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results