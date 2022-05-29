from flask import Response, request
from flask_restful import Resource
import json

class UserProfileListEndpoint(Resource):
    def __init__(self, firebase):
        self.firebase_app = firebase
        pass

class UserProfileDetailEndpoint(Resource):

    def __init__(self, firebase):
        self.firebase_app = firebase
        pass

    def get(self, id):
        db_module = self.firebase_app.getFirebaseDatabase()
        user_profile = db_module.child("userprofile").get().val()
        if id in user_profile:
            return Response(json.dumps(user_profile), mimetype="application/json",status=200)   
        else:
            return Response(json.dumps({"message" : "No User"}), mimetype="application/json",status=400)

    def post(self, id):
        body = request.get_json()
        
        data = {}
        data['name'] = body.get('name')
        data['funds'] = body.get('funds')

        db_module = self.firebase_app.getFirebaseDatabase()
        db_module.child("userprofile").child(id).set(data)
        return Response(json.dumps({"message" : "User profile created successfully!!"}), mimetype="application/json",status=200)

    def delete(self, id):
        db_module = self.firebase_app.getFirebaseDatabase()
        db_module.child("userprofile").child(id).remove()
        
        return Response(json.dumps({"message":  "User profile id={0} successfully deleted".format(id)}), mimetype="application/json", status=200)

def initialize_routes(api, firebase):

    api.add_resource(
        UserProfileListEndpoint, 
        '/userprofile',        
        '/userprofile/',
        resource_class_kwargs={"firebase": firebase}
    )

    api.add_resource(
        UserProfileDetailEndpoint, 
        '/userprofile/<string:id>/',
        '/userprofile/<string:id>',
        resource_class_kwargs={"firebase": firebase}
    )