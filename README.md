# GraphQLDemo

## Graphene Django Project
This example project demonstrate an integration between Graphene and Django. You'll build an Event Model to access event objects through GraphQL.

First you'll need to get the source of the project. Do this by cloning the repository:

## Install dependencies
pip install -r requirements.txt

## Create database table
python manage.py makemigrations
python manage.py migrate

## Create mock data
$ python manage.py shell
>>> from events.models import Event
>>> Event.objects.create(name='ADBI', url='https://www.ADBI.com/')
>>> Event.objects.create(name='graphql', url='https://www.graphql.com/')

## Start the application
python manage.py runserver

## Queries:

1. Fetch Data

        query{
            events{
                id
                name
                url
            }
        }


2. Mutation:

        mutation{
            createEvent(
                name:"GraphQL class"
                url:"www.graphql.com"
                ){
                    id
                    name
                    url
                }
        }
        
        3. Filter data:
        
        By Last:
        
        query{
            events(last:1){
                id
                name
                url
            }
        }
        
        Search by String:
        
        query{
            events(search:"ADBI"){
                id
                name
                url
            }
        }
        
        Search and filter:
        
        query{
            events(first:1, search:"ADBI"){
                id
                name
                url
            }
        }
