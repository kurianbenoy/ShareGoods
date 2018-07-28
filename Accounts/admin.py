from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


from Accounts.models import Usernames,Rating,Review

class UsersInline(admin.StackedInline):
    model = Usernames
    can_delete = False
    verbose_name_plural = 'users'

class UserAdmin(BaseUserAdmin):
    inlines = (UsersInline, )

#Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User,UserAdmin)

admin.site.register(Rating)
admin.site.register(Review)
