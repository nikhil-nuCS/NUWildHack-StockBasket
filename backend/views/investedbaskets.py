from flask import Response, request
from flask_restful import Resource
import json

class InvestedBasketListEndpoint(Resource):
    def __init__(self, firebase):
        self.firebase_app = firebase
        pass

    def get(self):
        body = request.get_json()
        email = body.get("email")
        db_module = self.firebase_app.getFirebaseDatabase()
        all_baskets = db_module.child("baskets").get().val()
        invested_baskets = db_module.child("investedbaskets").get().val()
        result = []
        if email in invested_baskets:
            invest_details = invested_baskets[email]
            user_invested_baskets = invest_details.keys()
            for each_basket_id in user_invested_baskets:
                basket_details = all_baskets[each_basket_id]
                basket_details["id"] = each_basket_id
                stocks = basket_details["stocks"]
                tmp = []
                for i in stocks:
                    dic = []
                    dic.append(i)
                    dic.append(stocks[i])
                    tmp.append(dic)
                basket_details["stocks"] = tmp
                result.append(basket_details)
            return Response(json.dumps(result), mimetype="application/json",status=200)
        else:
            return Response(json.dumps({"message" : "No User"}), mimetype="application/json",status=400)

    def post(self):
        body = request.get_json()
        email = body.get("email")
        basketid = body.get("basketid")
        quantity = body.get("quantity")

        db_module = self.firebase_app.getFirebaseDatabase()
        invested_baskets = db_module.child("investedbaskets").get().val()

        if invested_baskets:
            if email in invested_baskets:
                invest_details = invested_baskets[email]
                # bucket_id = body.get("bucketid")
                # print(invest_details.keys())
                # if(str(bucket_id) in invest_details.keys()):
                #     invest_details[str(body.get("bucketid"))] = int(body.get("quantity")) + invest_details[bucket_id]
                # else:
                invest_details[basketid] = quantity
                db_module.child("investedbaskets").child(email).update(invest_details)
                return Response(json.dumps(invest_details), mimetype="application/json",status=200)
            else:
                data = {}
                data[id] = 1
                db_module.child("investedbaskets").child(email).set(data)
                return Response(json.dumps({"message" : "Invested bucket added !"}), mimetype="application/json",status=200)

        else:
            data = {}
            data[basketid] = quantity
            db_module.child("investedbaskets").child(email).set(data)
            return Response(json.dumps({"message" : "Invested bucket added !"}), mimetype="application/json",status=200)


class InvestedBasketDetailEndpoint(Resource):

    def __init__(self, firebase):
        self.firebase_app = firebase
        pass

    def get(self, id):
        db_module = self.firebase_app.getFirebaseDatabase()
        all_baskets = db_module.child("baskets").get().val()
        invested_baskets = db_module.child("investedbaskets").get().val()
        result = []
        email = id
        if email in invested_baskets:
            invest_details = invested_baskets[email]
            user_invested_baskets = invest_details.keys()
            for each_basket_id in user_invested_baskets:
                basket_details = all_baskets[each_basket_id]
                basket_details["id"] = each_basket_id
                stocks = basket_details["stocks"]
                tmp = []
                for i in stocks:
                    dic = []
                    dic.append(i)
                    dic.append(stocks[i])
                    tmp.append(dic)
                basket_details["stocks"] = tmp
                result.append(basket_details)
            return Response(json.dumps(result), mimetype="application/json",status=200)
        else:
            return Response(json.dumps({"message" : "No User"}), mimetype="application/json",status=400)

    # def delete(self, id):
    #     db_module = self.firebase_app.getFirebaseDatabase()
    #     db_module.child("baskets").child(id).remove()
    #     return Response(json.dumps({"message":  "Basket id={0} successfully deleted".format(id)}), mimetype="application/json", status=200)

def initialize_routes(api, firebase):

    api.add_resource(
        InvestedBasketListEndpoint, 
        '/investedbaskets',
        resource_class_kwargs={"firebase": firebase}
    )

    api.add_resource(
        InvestedBasketDetailEndpoint, 
        '/investedbaskets/<string:id>',
        resource_class_kwargs={"firebase": firebase}
    )