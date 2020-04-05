"""GraphQLDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, reverse
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

#Unlike a RESTful API, there is only a single URL from which GraphQL is accessed.
#Requests to this URL are handled by Graphene’s GraphQLView view.
#This view will serve as GraphQL endpoint
urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    # url(r'^graphiql', include('django_graphiql.urls')),
]
