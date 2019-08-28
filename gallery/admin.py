from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Photo, Category, Location


# class PhotoInline(admin.TabularInline):
#     fieldsets = [
#         ('Basic Info', {'fields': ['description']}),
#         ('Upload Image', {'fields': ['image']})
#     ]
#     model = Photo
#     extra = 3
#
#
# class TopicAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['name']}),
#     ]
#     inlines = [PhotoInline]


admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Location)