from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja

class Dojo:
    DB = 'dojos_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def all_dojos(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def add_dojo(cls,data):
        query = '''INSERT INTO dojos (name)
            VALUES(%(name)s)'''
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def all_dojos_and_ninjas(cls, data):
        query = '''SELECT * FROM dojos 
        LEFT JOIN ninjas ON ninjas.dojo_id = dojo_id 
        WHERE dojos.id = %(id);'''
        results = connectToMySQL(cls.DB).query_db(query, data)
        dojo = cls(results[0])
        for ninja in results:
            ninja_data = {
                'id' : ninja['ninja.id'],
                'first_name' : ninja['ninja.first_name'],
                'last_name' : ninja['ninja.last_name'],
                'age' : ninja['ninja.age'],
                'dojo_id' : ninja['ninja.dojo_id']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))