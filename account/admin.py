from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EmsysUser

class EmsysUserAdmin(UserAdmin):
    model = EmsysUser

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name', 'department', 'student_number', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'department', 'student_number', 'gender', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'name', 'department', 'student_number', 'gender', 'is_staff', 'is_superuser')
    
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    filter_horizontal = ()

    search_fields = ('username', 'name', 'department', 'student_number')

admin.site.register(EmsysUser, EmsysUserAdmin)