from flask import Response, request
from flask_restful import Resource
import json
import pyrebase

class SignUpListEndpoint(Resource):
    def __init__(self, firebase):
        self.firebase_app = firebase
        pass

    def post(self):
        body = request.get_json()
        # print(body)
        email = body.get("email")
        password = body.get("password")
        authentication_module = self.firebase_app.getFirebaseAuth()
        created_info = authentication_module.create_user_with_email_and_password(email, password)
        print(created_info)
        return Response(json.dumps(created_info), mimetype="application/json",status=200)

def initialize_routes(api, firebase):
    api.add_resource(
        SignUpListEndpoint, 
        '/signup',
        resource_class_kwargs={"firebase": firebase}
    )