from django.db.models import Q
from django.http import JsonResponse
from backend.models import *
import json
import pandas as pd
from fuzzywuzzy import fuzz


def login(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    email = content_dict.get('email')
    password = content_dict.get('password')
    info = {}
    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        if user.password == password:
            message = "登录成功"
            info = user.to_dict()
        else:
            message = "密码错误，请重新输入密码"
    else:
        message = "该用户不存在，请先检查邮箱是否正确"
    data = {'message': message, "info": info}
    result = JsonResponse(dict(data))
    return result

def register(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    name = content_dict.get('username')
    email = content_dict.get('email')
    password = content_dict.get('password')
    password2 = content_dict.get('password2')
    if User.objects.filter(email=email).exists():
        message = "该邮箱已注册"
    elif password != password2:
        message = "两次输入密码不一致，请重新输入"
    else:
        message = '注册成功'
        User.objects.create(name=name, email=email, password=password)
    data = {'message':message}
    result = JsonResponse(dict(data))
    return result

def updateUser(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    update_type = content_dict.get('type')
    email = content_dict.get('email')
    update_content = content_dict.get('content')
    user = User.objects.get(email=email)
    if update_type == 'name':
        user.name = update_content
    elif update_type == 'password':
        user.password = update_content
    elif update_type == 'profile':
        user.profile = update_content
    elif update_type == 'gender':
        user.gender = update_content
    elif update_type == 'photo':
        user.photo = update_content
    user.save()
    data = {'messsag': '修改用户信息成功'}
    result = JsonResponse(dict(data))
    return result

def addGameFromFile(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    file_path = content_dict.get('path')
    file = pd.read_csv(file_path)
    for index, row in file.iterrows():
        name = row['name']
        rating = row['rating']
        date = row['date']
        platform = row['platform']
        if not Game.objects.filter(Q(name=name) & Q(date=date) & Q(rating=rating) & Q(platform=platform)):
            Game.objects.create(name=name, date=date, rating=rating, platform=platform)
    data = {'messsage': '成功添加'}
    result = JsonResponse(dict(data))
    return result

def addGame(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    name = content_dict['name']
    rating = content_dict['rating']
    date = content_dict['date']
    platform = content_dict['platform']
    if not Game.objects.filter(Q(name=name) & Q(date=date) & Q(rating=rating) & Q(platform=platform)):
        Game.objects.create(name=name, date=date, rating=rating, platform=platform)
    data = {'messsage': '成功添加'}
    result = JsonResponse(dict(data))
    return result

def getGame(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    developer_id = content_dict.get('developer_id')
    data = []
    if game_id != None:
        game = Game.objects.filter(game_id=game_id).first()
        item = game.to_dict()
        tags = list(Tag.objects.filter(game_id=item['id']))
        item['tag'] = [tag.to_dict() for tag in tags]
        developers = list(Develop.objects.filter(game_id=item['id']))
        item['developer'] = []
        for developer in developers:
            item['developer'].append(developer.to_dict())
        data = [item]
    elif developer_id != None:
        items = list(Develop.objects.filter(developer_id=developer_id))
        data = []
        for item in items:
            game = item.game
            data.append(game.to_dict())
    else:
        data = list(Game.objects.all())
        data = [i.to_dict() for i in data]
    data = {'messsage': '成功导出游戏数据', "data": data}
    result = JsonResponse(dict(data))
    return result

def searchGame(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    keyword = content_dict.get('keyword')
    if Game.objects.filter(name__icontains=keyword).exists():
        games = list(Game.objects.filter(name__icontains=keyword))
    else:
        games = list(Game.objects.all())
        game_dist = {}
        for game in games:
            game_dist[game] = fuzz.partial_ratio(keyword, game.name)
        game_list = game_dist.items()
        game_list.sort(key=lambda x:x[1], reverse=False)
        game_list = game_list[:10]
        games = [i[0] for i in game_list]
    data = [i.to_dict() for i in games]
    data = {'messsage': '成功搜索游戏', "data": data}
    result = JsonResponse(dict(data))
    return result

def getUserFavorites(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    user_id = content_dict.get('user_id')
    items = list(Favorites.objects.filter(user_id=user_id))
    data = []
    for item in items:
        game = item.game
        data.append(game.to_dict())
    data = {'messsage': '成功导出该用户收藏夹', "data": data}
    result = JsonResponse(dict(data))
    return result

def addFavorites(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    user_id = content_dict.get('user_id')
    if Favorites.objects.filter(Q(user_id=user_id) & Q(game_id=game_id)).exists():
        data = {'message': '已在收藏夹中'}
    else:
        Favorites.objects.create(user_id=user_id, game_id=game_id)
        data = {'message': '加入收藏夹成功'}
    result = JsonResponse(dict(data))
    return result

def delFavorites(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    user_id = content_dict.get('user_id')
    if Favorites.objects.filter(Q(user_id=user_id) & Q(game_id=game_id)).exists():
        item = Favorites.objects.filter(Q(user_id=user_id) & Q(game_id=game_id))
        item.delete()
        data = {'message': '已从收藏夹中删除'}
    else:
        data = {'message': '该游戏不在用户收藏夹中'}
    result = JsonResponse(dict(data))
    return result

def getHeat(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    if game_id != None:
        data = list(Heat.objects.filter(game_id=game_id))
    else:
        data = list(Heat.objects.all())
    data = [i.to_dict() for i in data]
    data = {'messsage': '成功导出游戏热度数据', "data": data}
    result = JsonResponse(dict(data))
    return result 

def getDiscount(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    country = content_dict.get('country')
    if country != None:
        data = list(Discount.objects.filter(game_id=game_id, country=country).order_by('country', 'date'))
    elif game_id != None:
        data = list(Discount.objects.filter(game_id=game_id))
    else:
        data = list(Discount.objects.all())
    data = [i.to_dict() for i in data]
    data = {'messsage': '成功导出游戏折扣数据', "data": data}
    result = JsonResponse(dict(data))
    return result 

def getTag(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    if game_id != None:
        data = list(Tag.objects.filter(game_id=game_id))
    else:
        data = list(Tag.objects.all())
    data = [i.to_dict() for i in data]
    data = {'messsage': '成功导出游戏标签', "data": data}
    result = JsonResponse(dict(data))
    return result

def getPrice(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    country = content_dict.get('country')
    if country != None:
        data = list(Price.objects.filter(game_id=game_id, country=country).order_by('country', 'date'))
    else:
        data = list(Price.objects.filter(game_id=game_id).order_by('country', 'date'))
    data = [i.to_dict() for i in data]
    data = {'messsage': '成功导出游戏价格', "data": data}
    result = JsonResponse(dict(data))
    return result

def getGoods(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    buyer_id = content_dict.get('buyer_id')
    seller_id = content_dict.get('seller_id')
    if game_id != None:
        data = list(Goods.objects.filter(game_id=game_id))
    elif buyer_id != None:
        data = list(Goods.objects.filter(buyer_id=buyer_id))
    elif seller_id != None:
        data = list(Goods.objects.filter(seller_id=seller_id))
    data = [i.to_dict() for i in data]
    data = {'messsage': '成功导出商品', "data": data}
    result = JsonResponse(dict(data))
    return result

def addGoods(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    price = content_dict.get('price')
    game_id = content_dict.get('game_id')
    seller_id = content_dict.get('seller_id')
    steam_id = content_dict.get('steam_id')
    status = '已上架'
    Goods.objects.create(seller_id=seller_id, game_id=game_id, price=price, steam_id=steam_id, status=status)
    data = {'message': '上架商品成功'}
    result = JsonResponse(dict(data))
    return result

def delGoods(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    id = content_dict.get('id')
    if Goods.objects.filter(Q(id=id)).exists():
        item = Goods.objects.filter(Q(id=id))
        item.delete()
        data = {'message': '已删除该商品'}
    else:
        data = {'message': '不存在该商品'}
    result = JsonResponse(dict(data))
    return result

def updateGoods(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    id = content_dict.get('id')
    update_type = content_dict.get('type')
    update_content = content_dict.get('content')
    goods = Goods.objects.get(id=id)
    if update_type == 'price':
        goods.price = update_content
    elif update_type == 'status':
        goods.status = update_content
    elif update_type == 'comment':
        goods.comment = update_content
    elif update_type == 'steam_id':
        goods.steam_id = update_content
    goods.save()
    data = {'messsag': '修改商品信息成功'}
    result = JsonResponse(dict(data))
    return result

def buyGoods(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    id = content_dict.get('id')
    buyer_id = content_dict.get('buyer_id')
    goods = Goods.objects.get(id=id)
    goods.buyer_id = buyer_id
    goods.status = '已购买'
    goods.save()
    data = {'messsag': '商品购买成功'}
    result = JsonResponse(dict(data))
    return result

def getDeveloper(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    country = content_dict.get('country')
    if country != None:
        data = list(Price.objects.filter(game_id=game_id, country=country).order_by('country', 'date'))
    else:
        data = list(Price.objects.filter(game_id=game_id).order_by('country', 'date'))
    data = [i.to_dict() for i in data]
    data = {'messsage': '成功导出游戏价格', "data": data}
    result = JsonResponse(dict(data))
    return result

def getComment(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    if game_id != None:
        data = list(Comment.objects.filter(game_id=game_id))
    data = [i.to_dict() for i in data]
    data = {'messsage': '成功导出评论', "data": data}
    result = JsonResponse(dict(data))
    return result

def addComment(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    content = content_dict.get('content')
    game_id = content_dict.get('game_id')
    user_id = content_dict.get('user_id')
    Comment.objects.create(user_id=user_id, game_id=game_id, content=content)
    data = {'message': '评论发布成功'}
    result = JsonResponse(dict(data))
    return result

def delComment(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    id = content_dict.get('id')
    if Comment.objects.filter(Q(id=id)).exists():
        item = Comment.objects.filter(Q(id=id))
        item.delete()
        data = {'message': '已删除该评论'}
    else:
        data = {'message': '不存在该评论'}
    result = JsonResponse(dict(data))
    return result

def updateComment(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    id = content_dict.get('id')
    update_type = content_dict.get('type')
    update_content = content_dict.get('content')
    comment = Comment.objects.get(id=id)
    if update_type == 'like':
        comment.likes += 1
    elif update_type == 'dislike':
        comment.likes -= 1
    elif update_type == 'content':
        comment.content = update_content
    comment.save()
    data = {'messsag': '修改评论成功'}
    result = JsonResponse(dict(data))
    return result

def getSlide(request):
    # content = request.body.decode()
    # content_dict = json.loads(content)
    # print(content_dict)
    data = list(Slide.objects.all())
    data = [i.to_dict() for i in data]
    data = {'messsage': '成功导出所有轮播图', "data": data}
    result = JsonResponse(dict(data))
    return result

def getNews(request):
    # content = request.body.decode()
    # content_dict = json.loads(content)
    # print(content_dict)
    data = list(News.objects.all())
    data = [i.to_dict() for i in data]
    data = {'messsage': '成功导出所有新闻', "data": data}
    result = JsonResponse(dict(data))
    return result