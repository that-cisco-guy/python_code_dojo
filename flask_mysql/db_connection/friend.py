# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    DB = 'friends_flask_mysql'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * from friends WHERE id = %(id)s'
        results = connectToMySQL(cls.DB).query_db(query, {'id' : id})
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT into friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(occupation)s , NOW() , NOW() );"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def update(cls, data):
        query = 'UPDATE friends SET first_name = %(first_name)s, last_name = %(last_name)s , occupation = %(occupation)s WHERE id = %(id)s;'
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def delete(cls, friend_id):
        query = 'DELETE FROM friends WHERE id = %(id)s;'
        return connectToMySQL(cls.DB).query_db(query, {'id': friend_id})