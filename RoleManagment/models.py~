from __future__ import unicode_literals

from django.db import models

# Create your models here.from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from Masterdata.models import *
from myapp.models import *
from myapp.models import Role


##### MenuHeadline models here
class MenuHeadline(BaseContent):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name


##### Menu models here
class Menu(BaseContent):
    name = models.CharField(max_length=100, null=True, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    menuheadline = models.ForeignKey(MenuHeadline, blank=True, null=True)
    link = models.CharField('Link Url', max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_submenu(self):
        return Menu.objects.filter(parent=self)
        

####MenuRoleRelationship models here
class MenuRoleRelationship(BaseContent):
    role = models.ForeignKey(Role)
    menus = models.ManyToManyField(Menu)

#########UserRolePermission models here
class UserRolePermission(BaseContent):
    user = models.ForeignKey(User)
    role = models.ManyToManyField(Role)
    
    
