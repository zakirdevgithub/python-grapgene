import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id=graphene.ID()
    user_name=graphene.String()
    age=graphene.Int()
    created_at=graphene.DateTime()

class Query(graphene.ObjectType):
    users=graphene.List(User, limit=graphene.Int())
    hello=graphene.String()

    def resolve_users(self,info, limit=None):
        return [
            User(id="1", user_name="Zakir", age=25, created_at=datetime.now()),
            User(id="2", user_name="Zahid", age=35, created_at=datetime.now()),
            User(id="3", user_name="Rakib", age=24, created_at=datetime.now())
        ][:limit]
    def rsolve_hello(self,info):
        return "World"

schema=graphene.Schema(query=Query)

result=schema.execute(
    '''
    {
        users(limit:2){
            id
            userName
            createdAt
        }
        
    }
    '''
)

dictData=dict(result.data.items())
print(json.dumps(dictData, indent=2))
    