import graphene
import json
from datetime import datetime
import uuid

class User(graphene.ObjectType):
    id=graphene.ID(default_value=str(uuid.uuid4()))
    username=graphene.String()
    created_at=graphene.DateTime(default_value=datetime.now())

class Query(graphene.ObjectType):
    users=graphene.List(User)
    hello=graphene.String()

    def resolve_hello(self, info):
        return "World"

    # def resolve_users(self, info, limit=None):
    #     return [
    #         User(id="1", username="Zakir", created_at=datetime.now()),
    #         User(id="2", username="Zahid", created_at=datetime.now()),
    #         User(id="3", username="Rakib", created_at=datetime.now())
    #     ][:limit]

class CreateUser(graphene.Mutation):
    user=graphene.Field(User)
    class Arguments:
        username=graphene.String()
    
    def mutate(self,info, username):
        user=User(username=username)
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user=CreateUser.Field()

schema=graphene.Schema(query=Query, mutation=Mutation)

result=schema.execute(
    '''

    mutation{
        createUser(username:"Zakir"){
            user{
                id
                username
                createdAt
            }
        }
    }
    '''
)

dictResult=dict(result.data.items())
print(json.dumps(dictResult, indent=2))
