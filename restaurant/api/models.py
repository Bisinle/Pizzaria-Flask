from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


    # relationship
    rest_pizza_association = db.relationship('RestaurantPizza', back_populates ='restaurant')
    pizzas = association_proxy('rest_pizza_association', 'pizza')


    def __repr__(self):
        return f'(id: {self.id}, name: {self.name})'


class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__='restaurant_pizzas'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    pizza_id = db.Column('pizza_id',db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column('restaurant_id',db.Integer, db.ForeignKey('restaurants.id'))
    

    pizza = db.relationship('Pizza',back_populates='rest_pizza_association')
    restaurant = db.relationship('Restaurant',back_populates='rest_pizza_association')
    

    def __repr__(self):
        return f'(id: {self.id}, name: {self.price}, pizza_id: {self.pizza_id}, restaurant_id: {self.restaurant_id})'



class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationship
    rest_pizza_association = db.relationship('RestaurantPizza', back_populates ='pizza')
    restaurants = association_proxy('rest_pizza_association', 'restaurant')
    


    def __repr__(self):
        return f'(id: {self.id}, name: {self.name}, pizza_id: {self.ingredients}, restaurant_id: {self.created_at})'


