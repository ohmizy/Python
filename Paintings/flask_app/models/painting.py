# import the function that will return an instance of a connection
from operator import is_
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the painting table from our database
from pprint import pprint
from flask_app import flash

DATABASE = "paintings"

class Painting:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.price = data['price']
        self.user_id = data['user_id']
        if "first_name" in data:
          self.first_name = data["first_name"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

  # ! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM paintings;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of paintings
        paintings = []
        # Iterate over the db results and create instances of paintings with cls.
        for painting in results:
            paintings.append( cls(painting) )
        return paintings

    @classmethod
    def get_all_with_user(cls):
        query = "SELECT * FROM paintings JOIN users ON paintings.user_id = users.id;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # Create an empty list to append our instances of paintings
        paintings = []
        # Iterate over the db results and create instances of paintings with cls.
        for painting in results:
            paintings.append( cls(painting) )
        return paintings

    # ! READ/RETRIEVE
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM paintings JOIN users ON paintings.user_id = users.id WHERE paintings.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        painting = Painting(result[0])
        return painting 

# ! CREATE
    @classmethod
    def save(cls,data):
      query="INSERT INTO paintings (name, description, price, user_id ) VALUES (%(name)s, %(description)s, %(price)s, %(user_id)s);"
      return connectToMySQL(DATABASE).query_db(query,data)

    # ! UPDATE
    @classmethod
    def update(cls,data):
        query = "UPDATE paintings SET name = %(name)s, description = %(description)s, price = %(price)s, user_id = %(user_id)s WHERE id =%(id)s ;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! DELETE
    @classmethod
    def destroy (cls, data):
        query = "DELETE FROM paintings WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate_painting(painting:dict) -> bool:
        is_valid = True
        if len(painting['name']) < 3:
            flash('name is too short!!')
            is_valid = False
        return is_valid