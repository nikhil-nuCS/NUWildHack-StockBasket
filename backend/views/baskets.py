from flask import Response, request
from flask_restful import Resource
import json
import shortuuid

class BasketListEndpoint(Resource):
    def __init__(self, firebase):
        self.firebase_app = firebase
        pass

    def get(self):
        db_module = self.firebase_app.getFirebaseDatabase()
        baskets = db_module.child("baskets").get()
        result = []
        for item in baskets.each():
            temp_dic = item.val()
            temp_dic["id"] = item.key()
            stocks = temp_dic["stocks"]
            tmp = []
            for i in stocks:
                dic = []
                dic.append(i)
                dic.append(stocks[i])
                tmp.append(dic)
            temp_dic["stocks"] = tmp
            result.append(temp_dic)
        return Response(json.dumps(result), mimetype="application/json",status=200)
    
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

        db_module = self.firebase_app.getFirebaseDatabase()
        db_module.child("baskets").child(id).set(data)
        return Response(json.dumps({"message" : "Stock basket created successfully!!"}), mimetype="application/json",status=200)


class BasketListDetailEndpoint(Resource):

    def __init__(self, firebase):
        self.firebase_app = firebase
        pass

    def delete(self, id):
        db_module = self.firebase_app.getFirebaseDatabase()
        db_module.child("baskets").child(id).remove()
        return Response(json.dumps({"message":  "Basket id={0} successfully deleted".format(id)}), mimetype="application/json", status=200)

def initialize_routes(api, firebase):

    api.add_resource(
        BasketListEndpoint, 
        '/baskets',
        resource_class_kwargs={"firebase": firebase}
    )

    api.add_resource(
        BasketListDetailEndpoint, 
        '/baskets/<string:id>',
        resource_class_kwargs={"firebase": firebase}
    )