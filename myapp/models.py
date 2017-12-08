from __future__ import unicode_literals
from django.contrib import admin
import six
from django.db import models

# Create your models here.

class BaseContentBase(models.base.ModelBase):

    def __iter__(self):
        return self.objects.all().__iter__()

    @staticmethod
    def register(mdl):
        if (not hasattr(mdl, 'Meta')) or getattr(
                getattr(mdl, '_meta', None),
                'abstract', True
        ):
            return mdl

        class MdlAdmin(admin.ModelAdmin):
            list_display = ['__str__'] + [i.name for i in mdl._meta.fields
                                          if i.name not in ('active', 'created', 'modified')]
            filter_horizontal = [i.name for i in mdl._meta.many_to_many]

        if hasattr(mdl, 'Admin'):
            class NewMdlAdmin(mdl.Admin, MdlAdmin):
                pass
            admin.site.register(mdl, NewMdlAdmin)

        else:
            admin.site.register(mdl, MdlAdmin)

    def __new__(cls, name, bases, attrs):
        mdl = super(BaseContentBase, cls).__new__(cls, name, bases, attrs)
        if attrs.get('auto_admin', True):
            BaseContentBase.register(mdl)
        return mdl
        
#### BaseContent models here
class BaseContent(six.with_metaclass(BaseContentBase, models.Model)):
    # ---------comments-----------------------------------------------------#
    # BaseContent is the abstract base model for all
    # the models in the project
    # This contains created and modified to track the
    # history of a row in any table
    # This also contains switch method to deactivate one row if it is active
    # and vice versa
    # ------------------------ends here---------------------------------------------#
    ACTIVE_CHOICES = ((0, 'Inactive'), (2, 'Active'),)
    active = models.PositiveIntegerField(choices=ACTIVE_CHOICES,
                                     default=2)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        abstract = True
        
    #                                        BaseContent
    def switch(self):
        # Deactivate a model if it is active
        # Activate a model if it is inactive
        self.active = {2: 0, 0: 2}[self.active]
        self.save()

    #                                        BaseContent
    def copy(self, commit=True):
        # Create a copy of given item and save in database
        obj = self
        obj.pk = None
        if commit:
            obj.save()
        return obj
        
# Contact us tables
class Contactus(BaseContent):
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)
    
    def __unicode__(self):
        return self.first_name
        
# Role model here
class Role(BaseContent):
   name = models.CharField(max_length=225,blank=True,null=True)
   slug_field = models.SlugField(max_length=500,blank=True,null=True)
   
   def __unicode__(self):
       return self.name
       
   class Admin:
        prepopulated_fields = {"slug_field":("name",)}
