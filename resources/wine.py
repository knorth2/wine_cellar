
import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

wine = Blueprint('wine', 'wine')

#index route
@wine.route('/', methods=["GET"])
def wine_index():
    result = models.Wine.select()
    print('result of wine select')
    print(result)

    wine_dicts = [model_to_dict(wine) for wine in result]

    return jsonify({
        'data': wine_dicts,
        'message': f"Successfully found {len(wine_dicts)} wine",
        'status': 200
    }), 200

#create route
@wine.route('/', methods=["POST"])
def create_wine():
    payload = request.get_json()
    print(payload)
    new_wine = models.Wine.create(name=payload['name'], img=payload['img'], vintage=payload['vintage'], region=payload['region'], rating=payload['rating'], price=payload['price'], quantity=payload['quantity'], notes=payload['notes'])
    print(new_wine)
    wine_dict = model_to_dict(new_wine)
    return jsonify(
        data=wine_dict, 
        message= "Successfully created wine",
        status= 201 
        ), 201


# SHOW ROUTE
@wine.route('/<id>', methods=['GET'])
def get_one_wine(id):
    wine = models.Wine.get_by_id(id)
    print(wine)
    return jsonify(
        data = model_to_dict(wine),
        message = 'Success!!! 🍷',
        status = 200
    ), 200


# UPDATE ROUTE
# PUT api/v1/wine/<wine_id>
@wine.route('/<id>', methods=["PUT"])
def update_wine(id):
    payload = request.get_json()
    query = models.Wine.update(**payload).where(models.Wine.id == id)
    query.execute()
    return jsonify(
        data = model_to_dict(models.Wine.get_by_id(id)),
        status=200,
        message='wine updated successfully'
    ), 200


# DELETE ROUTE
# DELETE api/v1/wine/<wine_id>
@wine.route('/<id>', methods=['DELETE'])
def delete_wine(id):
    query = models.Wine.delete().where(models.Wine.id == id)
    query.execute()
    return jsonify(
        data= model_to_dict(models.Wine.get_by_id(id)),
        message='wine successfully deleted',
        status=200
    ), 200
