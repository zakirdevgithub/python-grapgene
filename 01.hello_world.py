import graphene 
#We need this graphene module to work with graphene
import json

#Now we need a table with data. here Query is a class and
#it inherit grahene.ObjectType
#I will make it a table with the help of Schema
class Query(graphene.ObjectType):
    hello=graphene.String() #here hello is a data of Query Table

    #Now we need resolve this hello. I mean, which data hello will return
    def resolve_hello(self,info):
        return "World"

#Now I turn Query class into Query Table with the help of Schema
schema=graphene.Schema(query=Query)

#Now I will execute schema and store value in result
result=schema.execute(
    '''
    {
        hello
    }
    '''
)

#Now I printing data of table
print(result.data.items()) #It will print a List of dictionary

#We can convert it into JSON format
dictForJson=dict(result.data.items())
print(json.dumps(dictForJson, indent=2)) #We indent it for beautiful output




