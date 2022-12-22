from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
from django.contrib.admin.models import LogEntry

class GameResource(resources.ModelResource):
    class Meta:
        model = Game

class GoodsResource(resources.ModelResource):
    class Meta:
        model = Goods
 
class GameAdmin(ImportExportModelAdmin):
    resource_classes = [GameResource]

class GoodsAdmin(ImportExportModelAdmin):
    resource_classes = [GoodsResource]

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'action_flag', 'content_type', 'object_id', 'object_repr', 'change_message']
    date_hierarchy = "action_time"
    list_filter = ['action_time', 'content_type', 'user']
    list_per_page = 15

# Register your models here.
admin.site.register(Game, GameAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register([User, Heat, Tag, GamePhoto, Favorites, Developer, Develop, Country, Price, Discount, GameDiscount, Comment, Like, News, Slide])
