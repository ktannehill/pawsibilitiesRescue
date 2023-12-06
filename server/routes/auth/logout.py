from flask import session
from flask_restful import Resource

class Logout(Resource): 
    def delete(self):  
        if "user_id" in session:
            del session["user_id"]
        return {}, 204