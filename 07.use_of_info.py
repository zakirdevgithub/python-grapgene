import graphene
import json
import uuid
from datetime import datetime

class Post(graphene.ObjectType):
    title=graphene.String()
    content=graphene.String()

class User(graphene.ObjectType):
    id=graphene.ID(default_value=uuid.uuid4())
    username=graphene.String()
    created_at=graphene.DateTime(default_value=datetime.now())
    image_url=graphene.String()

    def resolve_image_url(self,info):
        return f"https://gumanisoft.com/{self.username}/{self.id}"

class Query(graphene.ObjectType):
    hello=graphene.String()
    users=graphene.List(User)

    def resolve_hello(self,info):
        return "World"

class CreateUser(graphene.Mutation):
    user=graphene.Field(User)
    class Arguments:
        username=graphene.String()
    def mutate(self,info,username):
        user=User(username=username)
        return CreateUser(user=user)

class CreatePost(graphene.Mutation):
    post=graphene.Field(Post)
    class Arguments:
        title=graphene.String()
        content=graphene.String()
    def mutate(self, info, title, content):
        #Use of info
        if info.context.get("is_anonymous"):
            raise Exception("anonymous not allowed")
        post=Post(title=title, content=content)
        return CreatePost(post=post)

class Mutation(graphene.ObjectType):
    create_user=CreateUser.Field()
    create_post=CreatePost.Field()

schema=graphene.Schema(query=Query, mutation=Mutation)

result=schema.execute(
    '''
        # mutation($title:String, $content:String){
        #     createPost(title: $title, content: $content){
        #         post{
        #             title
        #             content
        #         }
        #     }
        # }

        mutation{
            createPost(title: "Zakir Hossain", content: "He is a Programmer"){
                post{
                    title
                    content
                }
            }
        }
    ''',
    context={"is_anonymous":True}
    # variable_values={"title":"Zakir Hossain","content":"He is a programmer"}
)

dictResult=dict(result.data.items())
print(json.dumps(dictResult, indent=2))