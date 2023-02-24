from flask import Flask, jsonify, request
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('C:/Users/HP/Desktop/tinydb1.json')

@app.route('/items', methods=['GET'])
def get_items():
    items = db.all()
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = db.get(Query().id == item_id)
    if not item:
        return '', 404
    return jsonify(item)

@app.route('/items', methods=['POST'])
def create_item():
    item = request.json
    item_id = db.insert(item)
    item['id'] = item_id
    return jsonify(item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = request.json
    db.update(item, Query().id == item_id)
    return '', 204

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    db.remove(Query().id == item_id)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
