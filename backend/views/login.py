from flask import Response, request
from flask_restful import Resource
import json
import pyrebase

class SignInListEndpoint(Resource):
    def __init__(self, firebase):
        self.firebase_app = firebase
        pass

    def post(self):
        body = request.get_json()
        # print(body)
        email = body.get("email")
        password = body.get("password")
        authentication_module = self.firebase_app.getFirebaseAuth()
        user_info = authentication_module.sign_in_with_email_and_password(email, password)
        print(user_info)
        return Response(json.dumps(user_info), mimetype="application/json",status=200)

def initialize_routes(api, firebase):
    api.add_resource(
        SignInListEndpoint, 
        '/login',
        resource_class_kwargs={"firebase": firebase}
    )