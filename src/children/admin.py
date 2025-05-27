from django.contrib import admin
from .models import Children, ChildGroup

@admin.register(Children)
class ChildrenAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'parent', 'group')

@admin.register(ChildGroup)
class ChildGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)