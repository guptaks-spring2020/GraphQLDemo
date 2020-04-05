import graphene
import events.schema

# Query for getting the data from the server.
class Query(events.schema.Query, graphene.ObjectType):
    pass


class Mutation(events.schema.Mutation, graphene.ObjectType):
    pass

# Create schema

#A GraphQL Schema defines the types and relationship between Fields in the API.

#The graphene.Schema object describes the data model and provides a GraphQL server
# with an associated set of resolve methods that know how to fetch data.
schema = graphene.Schema(query=Query, mutation=Mutation)