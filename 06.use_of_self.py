import graphene
import json
import uuid
from datetime import datetime


class User(graphene.ObjectType):
    id=graphene.ID(default_value=uuid.uuid4())
    username=graphene.String()
    created_at=graphene.DateTime(default_value=datetime.now())
    image_url=graphene.String()
    
    #Here use of Self
    def resolve_image_url(self,info):
        return f"https://gumanisoft.com/{self.username}/{self.id}"

class Query(graphene.ObjectType):
    hello=graphene.String()
    users=graphene.List(User)

    def resolve_hello(self,info):
        return "World"
    
    def resolve_users(self,info):
        return [
            User(username="Zakir"),
            User(username="Zahid"),
            User(username="Rakib")
        ]

schema=graphene.Schema(query=Query)
result=schema.execute(
    '''
    {
        users{
            id
            username
            createdAt
            imageUrl
        }
    }
    '''
)

dictResult=dict(result.data.items())
print(json.dumps(dictResult, indent=2))