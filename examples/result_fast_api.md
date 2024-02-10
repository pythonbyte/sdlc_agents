Here is the code for the backend application written in Python and FastAPI that does CRUD operations on users, along with the test cases for endpoint testing:

main.py:
```python
from fastapi import FastAPI
from fastapi import HTTPException
from models import User
from crud import create_user, get_user, update_user, delete_user

app = FastAPI()

@app.post("/users")
def create_user_handler(user: User):
    return create_user(user)

@app.get("/users/{user_id}")
def get_user_handler(user_id: int):
    user = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
def update_user_handler(user_id: int, user: User):
    updated_user = update_user(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}")
def delete_user_handler(user_id: int):
    deleted_user = delete_user(user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user
```

models.py:
```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    # Add other fields as per the requirements
```

crud.py:
```python
from typing import List, Optional
from models import User

users_db = []

def create_user(user: User) -> User:
    users_db.append(user)
    return user

def get_user(user_id: int) -> Optional[User]:
    for user in users_db:
        if user.id == user_id:
            return user
    return None

def update_user(user_id: int, user: User) -> Optional[User]:
    for i, u in enumerate(users_db):
        if u.id == user_id:
            users_db[i] = user
            return user
    return None

def delete_user(user_id: int) -> Optional[User]:
    for i, user in enumerate(users_db):
        if user.id == user_id:
            deleted_user = users_db.pop(i)
            return deleted_user
    return None
```

tests.py:
```python
import requests

BASE_URL = "http://localhost:8000"

def test_create_user():
    user_data = {"id": 1, "name": "John Doe", "email": "johndoe@example.com"}
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    assert response.status_code == 200
    assert response.json() == user_data

def test_get_user():
    user_id = 1
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "johndoe@example.com"}

def test_update_user():
    user_id = 1
    updated_user_data = {"id": 1, "name": "John Doe", "email": "updatedemail@example.com"}
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_user_data)
    assert response.status_code == 200
    assert response.json() == updated_user_data

def test_delete_user():
    user_id = 1
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "updatedemail@example.com"}
```

Please note that the above code is a simplified example and may require additional modifications and error handling based on the specific requirements and design choices.