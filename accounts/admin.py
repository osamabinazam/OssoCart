from django.contrib import admin
from .models  import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.


# Setting password to  readonly mode
class AccountAdmin (UserAdmin):
    list_display = ('first_name', 'last_name', 'email', 'username', 'date_joined',  'last_login', 'is_active')
    list_display_links =('email',  'username')
    readonly_fields = ('date_joined',  'last_login')
    ordering = ('date_joined', )
   
    
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    # fieldsets = (
    #     (None, {'fields': ('first_name', 'last_name', 'email', 'username', 'password')}),
    #     ('Personal info', {'fields': ('date_joined', 'last_login')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login',)}),
    # )



admin.site.register(Account, AccountAdmin )