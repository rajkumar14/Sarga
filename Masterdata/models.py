from __future__ import unicode_literals
from myapp.models import *
from django.db import models



class Country(BaseContent):

    # Similar to country in real world
    name = models.CharField(max_length=100,null=True,blank=True)


class State(BaseContent):
    # Similar to state in real world
    name = models.CharField(max_length=100,null=True,blank=True)
    country = models.ForeignKey(Country)

    
class District(BaseContent):
    # Similar to district in real world
    name = models.CharField(max_length=100,null=True,blank=True)
    state = models.ForeignKey(State)

class Taluk(BaseContent):
    # Similar to taluk in real world
    name = models.CharField(max_length=100,null=True,blank=True)
    district = models.ForeignKey(District)

class Mandal(BaseContent):
    # Similar to mandal in real world
    name = models.CharField(max_length=100,null=True,blank=True)
    taluk = models.ForeignKey(Taluk)

class Address(BaseContent):
    name = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=300,null=True,blank=True)
    address1 = models.CharField(max_length=100,null=True,blank=True)
    country = models.ForeignKey(Country, blank=True)
    state = models.ForeignKey(State, blank=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    pincode = models.CharField(max_length=100,blank=True,null=True)
    
