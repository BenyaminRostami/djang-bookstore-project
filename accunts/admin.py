from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
class CustomUserAdmin (UserAdmin):
    add_form =CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets +((None ,
                                       {'fields' : ('age' , ) }   ),
    )
    add_fieldsets = UserAdmin.add_fieldsets +((None ,
                                       {'fields' : ('age' , ) }   ),)
# Register your models here.

admin.site.register(CustomUser,CustomUserAdmin)