import unittest,json
from flask import Flask
from api import app,api  # Replace 'your_app_module' with the actual module name
from api.models import db, Restaurant  # Import the necessary models

class TestRestaurantsRoute():
  
    
    def test_bakeries_route(self):
        '''does the resource exist  at "/restaurants".'''
        response = app.test_client().get('/restaurants')
        assert(response.status_code == 200)

    def test_bakeries_route_returns_json(self):
        '''provides a response content type of application/json at "/restaurants"'''
        response = app.test_client().get('/restaurants')
        assert response.content_type == 'application/json'

    def test_restaurant_route_returns_list_of_restaurant_objsects(self):
        '''restaurant route returns a list of restaurant objects'''
#         # Add some test data to the database
        with app.app_context():
            restaurant1 = Restaurant(name='Restaurant 1', address='Address 1')
            restaurant2 = Restaurant(name='Restaurant 2', address='Address 2')
            db.session.add_all([restaurant1,restaurant2])
            db.session.commit()
            response = app.test_client().get('/restaurants')
            data = json.loads(response.data.decode())
            assert(type(data)==list)


    def test_restaurant_by_id_route(self):
        '''has resource available at /restaurants/1'''
        response = app.test_client().get('/restaurants/1')
        assert(response.status_code ==200)

    def test_restaurant_by_id_route_returns_json(self):
        '''the route return a json object in the  response body'''
        response = app.test_client().get('/restaurants/1')
        assert response.content_type=='application/json'

    def test_restaurant_by_id_route_response_contains_pizza_list(self):
        '''    pizzas exists in the response and is a type of list'''
        response = app.test_client().get('/restaurants/1')
        data = json.loads(response.data.decode())
        assert "pizzas" in data and isinstance(data["pizzas"], list)

    # def test_restaurant_model_has_validates_decorator(sefl):
    #     '''the Restaurant model has a name validator'''
    #     assert hasattr(Restaurant, 'name_validation,repr')

    # def test_restaurant_model_has_correct_columns(sefl):
    #     '''the Restaurant model has a name validator'''
    #     assert hasattr(Restaurant, 'name_validation,repr')








#     def test_get_restaurants(self):
#         # Test the GET request to retrieve all restaurants
#         response = self.client.get('/restaurants')
        
#         # Check if the response status code is 200 (OK)
#         self.assertEqual(response.status_code, 200)
        
#         # Check if the response contains the expected data
#         expected_data = [
#             {"id": 1, "name": "Restaurant 1", "address": "Address 1"},
#             {"id": 2, "name": "Restaurant 2", "address": "Address 2"},
#         ]
#         self.assertEqual(response.get_json(), expected_data)

#     def test_get_restaurant_by_id(self):
#         # Test the GET request to retrieve a specific restaurant by ID
#         response = self.client.get('/restaurants/1')
        
#         # Check if the response status code is 200 (OK)
#         self.assertEqual(response.status_code, 200)
        
#         # Check if the response contains the expected data for Restaurant 1
#         expected_data = {"id": 1, "name": "Restaurant 1", "address": "Address 1"}
#         self.assertEqual(response.get_json(), expected_data)

#     def test_get_nonexistent_restaurant_by_id(self):
#         # Test the GET request for a non-existent restaurant by ID
#         response = self.client.get('/restaurants/100')  # Assuming there is no restaurant with ID 100
        
#         # Check if the response status code is 404 (Not Found)
#         self.assertEqual(response.status_code, 404)
        
#         # Check if the response contains an error message
#         expected_data = {"error": "Restaurant not found"}
#         self.assertEqual(response.get_json(), expected_data)

# if __name__ == '__main__':
#     unittest.main()
