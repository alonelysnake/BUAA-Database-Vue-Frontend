from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([User, Game, Goods, Heat, Tag, GamePhoto, Favorites, Developer, Develop, Country, Price, Discount, GameDiscount, Comment, News, Slide])