from django.contrib import admin
from .models  import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.


# Setting password to  readonly mode
class AccountAdmin (UserAdmin):
    list_display = ('first_name', 'last_name', 'email', 'username', 'date_joined',  'last_login', 'is_active')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(Account, AccountAdmin )