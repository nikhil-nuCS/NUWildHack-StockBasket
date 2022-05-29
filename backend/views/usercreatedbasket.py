from flask import Response, request
from flask_restful import Resource
import json
import shortuuid

class UserCreatedBasketListEndpoint(Resource):
    def __init__(self, firebase):
        self.firebase_app = firebase
        pass

    def post(self):
        body = request.get_json()
        id = shortuuid.ShortUUID().random(length=7)
        data = {}
        data['name'] = body.get('name')
        data['price'] = body.get('price')
        data['type'] = body.get('type')
        data['description'] = body.get('description')
        data['riskType'] = body.get('riskType')
        data['creatorid'] = body.get('creatorid')
        data['stocks'] = body.get('stocks')
        data['CAGR'] = body.get('CAGR')
        data["imageurl"] = body.get("imageurl")
        email = body.get('creatorid')


        db_module = self.firebase_app.getFirebaseDatabase()
        db_module.child("baskets").child(id).set(data)

        invested_baskets = db_module.child("investedbaskets").get().val()
        if invested_baskets:
            if email in invested_baskets:
                invest_details = invested_baskets[email]
                # bucket_id = body.get("bucketid")
                # print(invest_details.keys())
                # if(str(bucket_id) in invest_details.keys()):
                #     invest_details[str(body.get("bucketid"))] = int(body.get("quantity")) + invest_details[bucket_id]
                # else:
                invest_details[id] = 1
                db_module.child("investedbaskets").child(email).update(invest_details)
                return Response(json.dumps(invest_details), mimetype="application/json",status=200)
            else:
                data = {}
                data[id] = 1
                db_module.child("investedbaskets").child(email).set(data)
                return Response(json.dumps({"message" : "Invested bucket added !"}), mimetype="application/json",status=200)

        else:
            data = {}
            data[id] = 1
            db_module.child("investedbaskets").child(email).set(data)
            return Response(json.dumps({"message" : "Invested bucket added !"}), mimetype="application/json",status=200)


class UserCreatedDetailEndpoint(Resource):

    def __init__(self, firebase):
        self.firebase_app = firebase
        pass

def initialize_routes(api, firebase):

    api.add_resource(
        UserCreatedBasketListEndpoint, 
        '/usercreatedbaskets',
        resource_class_kwargs={"firebase": firebase}
    )