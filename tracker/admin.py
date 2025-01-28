from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Import your CustomUser model

# Create a custom admin interface for the CustomUser model
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Optionally, customize what fields are displayed in the admin panel
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

# Register the CustomUser model and its admin interface
admin.site.register(CustomUser, CustomUserAdmin)
