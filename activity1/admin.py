from django.contrib import admin
from django.contrib import messages
from .models import Profile
from .models import User

class ProfileAdmin(admin.ModelAdmin):
    list_display =('get_first_name', 'get_last_name', 'description', 'is_active')
    
    def get_first_name(self,obj):
        return obj.user_profile.first_name
    get_first_name.short_description = 'FirstName'
    
    def get_last_name(self,obj):
        return obj.user_profile.last_name
    get_last_name.short_description = 'LastName'
    
    def active(self, obj):
        return obj.is_active ==1
  
    active.boolean =True
  
    def make_active(modeladmin, request, queryset):
        queryset.update(is_active =1)
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!")
  
    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active =0)
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")
  
    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")
  
    def has_delete_permission(self, request, obj =None):
        return False 
    
    # Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(User)
admin.site.site_header = "Karl's Admin Page" 