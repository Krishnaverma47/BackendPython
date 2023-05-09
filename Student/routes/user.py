from fastapi import APIRouter
from bson import ObjectId 

from models.user import User
from config.database import connection
from schemas.user import user_entity,users_entity

user = APIRouter()

@user.get('/')
async def find_all_users():
    return users_entity(connection.local.user.find())


@user.post('/createUser')
async def create_user(user:User):
    # print(type(dict(user)))
    # print((dict(connection.local.user.find_one({'email':dict(user)['email']}))))
    # print(users_entity(connection.local.user.find({'email':dict(user)['email']})))
    if len(users_entity(connection.local.user.find({'email':(dict(user))['email']}))) !=0:
        return {'message':'Username already exist.'}
    else:
        connection.local.user.insert_one(dict(user))
    # return users_entity(connection.local.user.find())
        return {'message':'Account has been created successfully.'}


@user.put('/{id}')
async def update_user(id,user:User):
    connection.local.user.find_one_and_update({'_id':ObjectId(id)},{
        "$set":dict(user)
    })
    return user_entity(connection.local.user.find_one({'_id':ObjectId(id)}))



@user.delete('/{id}')
async def delete_user(id):
    connection.local.user.find_one_and_delete({'_id':ObjectId(id)})
    return {'message':'Account has been deleted successfully.'}