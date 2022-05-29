from flask import Response, request
from flask_restful import Resource
import json

class ManagerProfileListEndpoint(Resource):
    def __init__(self, firebase):
        self.firebase_app = firebase
        pass

    def get(self):
        result = []
        db_module = self.firebase_app.getFirebaseDatabase()
        manager_profile = db_module.child("managerprofile").get()
        for item in manager_profile.each():
            dic = item.val()
            dic["email"] = item.key()
            result.append(dic)
        return Response(json.dumps(result), mimetype="application/json",status=200)

    def post(self):
        body = request.get_json()
        
        data = {}
        email = body.get("email")
        data['name'] = body.get('name')
        data['ratings'] = body.get('ratings')
        data["description"] = body.get("description")
        data["company"] = body.get("company")
        data["imageurl"] = body.get("imageurl")

        db_module = self.firebase_app.getFirebaseDatabase()
        db_module.child("managerprofile").child(email).set(data)
        return Response(json.dumps({"message" : "Manager profile created successfully!!"}), mimetype="application/json",status=200)

    def delete(self):
        body = request.get_json()
        email = body.get("email")
        db_module = self.firebase_app.getFirebaseDatabase()
        db_module.child("userprofile").child(email).remove()
        return Response(json.dumps({"message":  "Manager profile id={0} successfully deleted".format(email)}), mimetype="application/json", status=200)

class ManagerProfileDetailEndpoint(Resource):

    def __init__(self, firebase):
        self.firebase_app = firebase
        pass
   
    def get(self):
        body = request.get_json()
        email = body.get("email")
        db_module = self.firebase_app.getFirebaseDatabase()
        manager_profile = db_module.child("managerprofile").get().val()
        if email in manager_profile:
            return Response(json.dumps(manager_profile), mimetype="application/json",status=200)
        else:
            return Response(json.dumps({"message" : "No Manager"}), mimetype="application/json",status=400)


def initialize_routes(api, firebase):

    api.add_resource(
        ManagerProfileListEndpoint, 
        '/managerprofile',
        resource_class_kwargs={"firebase": firebase}
    )

    api.add_resource(
        ManagerProfileDetailEndpoint, 
        '/managerprofile/<string:id>',
        resource_class_kwargs={"firebase": firebase}
    )