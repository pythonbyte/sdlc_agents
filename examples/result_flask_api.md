CODE:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'})
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email})

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append({'id': user.id, 'name': user.name, 'email': user.email})
    return jsonify(result)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'})
    data = request.get_json()
    user.name = data['name']
    user.email = data['email']
    user.password = data['password']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
```

TESTS:

```python
import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase

from app import app, db, User

class UserTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.init_app(app)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        response = self.client.post('/users', json={'name': 'John Doe', 'email': 'john@example.com', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'User created successfully'})

    def test_get_user(self):
        user = User(name='John Doe', email='john@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        response = self.client.get(f'/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'id': user.id, 'name': user.name, 'email': user.email})

    def test_get_all_users(self):
        user1 = User(name='John Doe', email='john@example.com', password='password')
        user2 = User(name='Jane Smith', email='jane@example.com', password='password')
        db.session.add_all([user1, user2])
        db.session.commit()

        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{'id': user1.id, 'name': user1.name, 'email': user1.email}, {'id': user2.id, 'name': user2.name, 'email': user2.email}])

    def test_update_user(self):
        user = User(name='John Doe', email='john@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        response = self.client.put(f'/users/{user.id}', json={'name': 'John Smith', 'email': 'john@example.com', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'User updated successfully'})
        self.assertEqual(user.name, 'John Smith')
        self.assertEqual(user.password, 'newpassword')

    def test_delete_user(self):
        user = User(name='John Doe', email='john@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        response = self.client.delete(f'/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'User deleted successfully'})
        self.assertIsNone(User.query.get(user.id))

if __name__ == '__main__':
    unittest.main()
```

DOCUMENTATION:

API Documentation for Flask API with Flask-SQLAlchemy/Flask-Migrate and Postgres to do CRUD operations on USER

1. Create a new user

   - URL: /users
   - Method: POST
   - Request Body: { "name": "John Doe", "email": "john@example.com", "password": "password" }
   - Response Body: { "message": "User created successfully" }

2. Get a user by ID

   - URL: /users/{user_id}
   - Method: GET
   - Response Body: { "id": 1, "name": "John Doe", "email": "john@example.com" }

3. Get all users

   - URL: /users
   - Method: GET
   - Response Body: [ { "id": 1, "name": "John Doe", "email": "john@example.com" }, { "id": 2, "name": "Jane Smith", "email": "jane@example.com" } ]

4. Update a user

   - URL: /users/{user_id}
   - Method: PUT
   - Request Body: { "name": "John Smith", "email": "john@example.com", "password": "newpassword" }
   - Response Body: { "message": "User updated successfully" }

5. Delete a user

   - URL: /users/{user_id}
   - Method: DELETE
   - Response Body: { "message": "User deleted successfully" }

These endpoints allow you to perform CRUD operations on the USER entity in the database.