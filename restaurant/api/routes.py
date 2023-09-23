from api import api,make_response,jsonify
from flask_restful import Resource
from api.models import Restaurant,RestaurantPizza,Pizza,db,SerializerMixin





class Restaurants(Resource):
    def get(self):
        restaurants = Restaurant.query.all()

        restaurant_dict_list =[]
        for restaurant in restaurants:
            restuarant_dict = restaurant.to_dict()
            restaurant_dict_list.append(restuarant_dict)
        return make_response(restaurant_dict_list,200)

api.add_resource(Restaurants, '/restaurants')

class Restaurants_by_ID(Resource,SerializerMixin):
    def get(self,id):
        restaurant = Restaurant.query.filter_by(id=id).first()

        if restaurant:      
            restuarant_dict = restaurant.to_dict()        
            return make_response(restuarant_dict,200)
        else:
            response = { "error": "Restaurant not found" }
            return make_response(response,404)
        


    def delete(self,id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()

            response = {
                "delete-successful":True,
                "message": "restaurant deleted"
            }
            return make_response(jsonify(response),204)
        
        else:
            response = { "error": "restaurant you are trying to delete DOES NOT EXIST" }
            return make_response(response,404)
            




api.add_resource(Restaurants_by_ID, '/restaurants/<int:id>')



