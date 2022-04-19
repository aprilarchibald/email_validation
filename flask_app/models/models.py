from operator import is_
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

DATABASE = "email_validation_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        user_id= connectToMySQL(DATABASE).query_db( query, data )
        return user_id 

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            emails = []
            for email in results:
                emails.append( cls(email) )
            return emails
        return []

    @classmethod
    def delete(cls, data:dict):
        query= "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # @staticmethod
    # def validate_email( email ):
    #     is_valid = True
        # query = "SELECT * FROM emails WHERE email = %(email)s;"
        # results = connectToMySQL(DATABASE).query_db(query,email)
    #     if len(results) <= 0:
    #     if not EMAIL_REGEX.match(email['email']): 
    #         flash("Invalid email address!")
    #         is_valid = False
    #     return is_valid

    @staticmethod
    def validator(form_data: dict):
        is_valid = True
        if len(form_data['email']) <= 0:
            flash('email is required', 'err_email')
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!", 'err_email')
            is_valid = False
        return is_valid