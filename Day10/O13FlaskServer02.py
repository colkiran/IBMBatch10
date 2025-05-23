
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'pepsi': {'item': '2 ltr Bottle', 'price': 120, 'qty': 200},
    'coke': {'item': '500 ml Bottle', 'price': 65, 'qty': 350},
    'Thumbs_up': {'item': '300 ml can', 'price': 50, 'qty':150}
}

class Product(Resource):

    def get(self, product):
        return {product :products[product]}

api.add_resource(Product, "/getproduct/<product>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)



