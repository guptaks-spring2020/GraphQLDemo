#Schema with defined object types
#GraphQL presents the objects to the world as a graph structure.


import graphene
from graphene_django import DjangoObjectType
from .models import Event
from django.db.models import Q

# Graphene needs to know about each type of object which will appear in the graph.
#for each of our models, we are going to create a type, subclassing DjangoObjectType
class EventType(DjangoObjectType):
    class Meta:
        model = Event

#This graph also has a root type through which all access begins. This is the Query class below.
# Query to get data from the server


# A Graphene ObjectType is the building block used to define the relationship between Fields in your Schema and how their data is retrieved.
#
# The basics:
#
# Each ObjectType is a Python class that inherits from graphene.ObjectType.
# Each attribute of the ObjectType represents a Field.
# Each Field has a resolver method to fetch data (or Default Resolver).
class Query(graphene.ObjectType):

    #we will list those types as fields in the Query class.
    events = graphene.List(EventType,
                           search=graphene.String(),
                           first=graphene.Int(),
                           skip=graphene.Int(),
                           last=graphene.Int(),
                           )

    #A Resolver is a method that helps us answer Queries by fetching data for a Field in our Schema.
    #Each field on an ObjectType in Graphene should have a corresponding resolver method to fetch data.
    # This resolver method should match the field name. For example, in the Query type above,
    # the events field is resolved by the method resolve_events.

    #info for query and schema meta information
    def resolve_events(self, info, search=None, first=None, skip=None, last=None, **kwargs):
        qs = Event.objects.all()

        # Search records which partially matches name and url
        if search:
            filter = (
                Q(url__icontains=search) |
                Q(name__icontains=search)
            )
            qs = qs.filter(filter)

        # Skip n records
        if skip:
            qs = qs[skip::]

        # Get the first n records
        if first:
            qs = qs[:first]

        # Get the last n records
        if last:
            last_n = qs.order_by('-id')[:last]
            qs = reversed(last_n)
        return qs


# Create new Event
class CreateEvent(graphene.Mutation):
    # The class attributes define the response of the mutation
    id = graphene.Int()
    name = graphene.String()
    url = graphene.String()

    class Arguments:
        ## The input arguments for this mutation
        url = graphene.String()
        name = graphene.String()

    # info for query and schema meta information
    def mutate(self, info, name, url):

        event = Event(url=url, name=name)
        event.save()

        # Notice we return an instance of this mutation
        return CreateEvent(
            id=event.id,
            name=event.name,
            url=event.url,
        )


# Create event to the server
class Mutation(graphene.ObjectType):
    # import pdb;
    # pdb.set_trace()
    create_event = CreateEvent.Field()