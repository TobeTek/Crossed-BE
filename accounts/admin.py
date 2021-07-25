from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
	fieldsets= ((None,{'fields':('username', 'email', 'first_name', 'last_name','user_type')}),
				('Permissions',{'fields':("is_staff",'is_active',)}),	
		)

admin.site.register(CustomUser, CustomUserAdmin)