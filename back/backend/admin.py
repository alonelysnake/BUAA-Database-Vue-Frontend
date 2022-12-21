from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

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

admin.site.register([Game, Goods])
# Register your models here.
# admin.site.register([User, Game, GameAdmin, Goods, Heat, Tag, GamePhoto, Favorites, Developer, Develop, Country, Price, Discount, GameDiscount, Comment, News, Slide])
