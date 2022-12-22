from django.db import models
from django.db.models.signals import pre_save, post_delete, pre_delete
from django.dispatch import receiver

# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=11)
    password = models.CharField(max_length=15)
"""
1. 修改头像
2. 个人简介 DONE
3. 性别 DONE
4. 成交量+评分 DONE
"""
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=11)
    email = models.EmailField(default='')
    gender = models.CharField(max_length=11, default='')
    password = models.CharField(max_length=128)
    profile = models.CharField(max_length=300, default='')
    sales = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    photo = models.CharField(max_length=2560, default='')
    def to_dict(self):
        return {'id': self.id, 'email': self.email, 'username': self.name, 'password': self.password, 'gender': self.gender, 'profile': self.profile, 'sales': self.sales, 'likes': self.likes, 'dislikes': self.dislikes, 'photo': self.photo}

"""
1. 热度 新建实体 DONE
2. 查询所有游戏人数信息 DONE
3. 查询给定id的人数信息 DONE
"""
class Heat(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    date = models.DateField(default='2000-01-01')
    players = models.IntegerField(default=0)
    def to_dict(self):
        return {'game_id': self.game_id, 'date': self.date, 'players': self.players}

"""
1. 标签 新建实体 DONE
"""
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=11)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    def to_dict(self):
        return {'game_id': self.game_id, 'tag': self.name}

"""
1. 游戏截图 新建实体
"""
class GamePhoto(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=2560)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    def to_dict(self):
        return {'game_id': self.game_id, 'url': self.url} 
"""
1. 查询游戏的所有信息 DONE
2. 查询游戏所有价格（国家+时间） DONE
3. 查询给定id和国家的游戏的人数信息+价格信息 DONE ??? 
"""
class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=11)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)
    date = models.DateField(default='2000-01-01')
    platform = models.CharField(max_length=11, default='')
    cover = models.CharField(max_length=2560, default='')
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'rating': self.rating, 'platform': self.platform, 'date': self.date, 'cover': self.cover}

class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)

"""
1. 依据游戏查询所有商品信息 DONE
2. 依据卖家/卖家id查询商品信息 DONE
3. 购买操作：修改商品状态 DONE
4. 卖家修改商品信息 DONE
"""
class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    seller = models.ForeignKey("User", on_delete=models.CASCADE, related_name='seller')
    buyer = models.ForeignKey("User", on_delete=models.CASCADE, null=True, related_name='buyer')
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    decription = models.CharField(max_length=2560, default='')
    cd_key = models.CharField(max_length=256, default='')
    steam_id = models.CharField(max_length=256, default='')
    rating = models.CharField(max_length=11, default='')
    comment = models.CharField(max_length=30, default='')
    status = models.CharField(max_length=11, default='已上架')
    def to_dict(self):
        return {'id': self.id, 'price': self.price, 'seller_id': self.seller_id, 'buyer_id': self.buyer_id, 'game_id': self.game_id, 'steam_id': self.steam_id, 'cd_key': self.cd_key, 'decription': self.decription, 'comment': self.comment, 'status': self.status, 'rating': self.rating}

"""
合并合并合并 DONE
依据用户id查订单 DONE
"""
# class Order(models.Model):
#     id = models.AutoField(primary_key=True)
#     time = models.DateTimeField(default=None)
#     price
#     buyer
#     seller
#     steam_id
#     comment = models.CharField(max_length=300)
#     status = models.CharField(max_length=11)
#     def to_dict(self):
#         return {'id': self.id, 'time': self.time, 'comment': self.comment, 'status': self.status}
    
# class Business(models.Model):
#     goods = models.ForeignKey("Goods", default=1, on_delete=models.CASCADE)
#     buyer = models.ForeignKey("User", default=1, on_delete=models.CASCADE)
#     order = models.ForeignKey("Order", default=1, on_delete=models.CASCADE)
#     def to_dict(self):
#         return {'goods_id': self.goods_id, 'buyer_id': self.buyer_id, 'order_id': self.order_id}

"""
1. 依据游戏查开发商 DONE
2. 依据开发商查游戏 DONE
"""
class Developer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=11)
    def to_dict(self):
        return {'id': self.id, 'name': self.name}

class Develop(models.Model):
    developer = models.ForeignKey("Developer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=11)
    def to_dict(self):
        return {'id': self.id, 'name': self.name}

class Price(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    date = models.DateField(default='2000-01-01')
    original_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    current_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    def to_dict(self):
        return {'game_id': self.game_id, 'country_id': self.country_id, 'date': self.date, 'original_price': self.original_price, 'current_price': self.current_price}

class Discount(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='')
    start_time = models.DateField(default=None)
    end_time = models.DateField(default=None)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, default=100.0)
    def to_dict(self):
        return {'id': self.id, 'start_time': self.start_time, 'end_time': self.end_time, 'discount_rate': self.discount_rate}

class GameDiscount(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    discount = models.ForeignKey("Discount", on_delete=models.CASCADE)
    def to_dict(self):
        return {'discount_id': self.discount_id, 'country_id': self.country_id, 'game_id': self.game_id}

"""
1. 发表删除评论 DONE
2. 根据游戏查询评论 DONE
"""
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=300, default='')
    likes = models.IntegerField(default=0)
    def to_dict(self):
        return {'id': self.id, 'user_id': self.user_id, 'game_id': self.game_id, 'time': self.time, 'content': self.content, 'likes': self.likes}

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    def to_dict(self):
        return {'id': self.id, 'user_id': self.user_id, 'comment_id': self.comment_id}

@receiver(pre_save, sender=Like)
def pre_save_like(sender, instance, **kwargs):
    comment = instance.comment
    comment.likes += 1
    comment.save()

@receiver(pre_delete, sender=Like)
def pre_delete_like(sender, instance, **kwargs):
    comment = instance.comment
    comment.likes -= 1
    comment.save()

class News(models.Model):
    id = models.AutoField(primary_key=True)
    target = models.CharField(max_length=256, default='')
    title = models.CharField(max_length=256, default='')
    url = models.CharField(max_length=2560, default='')
    test = models.CharField(max_length=256, default='')
    def to_dict(self):
        return {'id': self.id, 'target': self.target, 'title': self.title, 'url': self.url, 'test': self.test}

class Slide(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey("Game", on_delete=models.CASCADE) 
    url = models.CharField(max_length=2560, default='')
    def to_dict(self):
        return {'id': self.id, 'game_id': self.game_id, 'url': self.url}

"""
1. 给筛选界面写高级筛选函数：国家、发行商、发售时间、优惠比例
2. 模糊搜索 DONE
3. 批量上架
"""