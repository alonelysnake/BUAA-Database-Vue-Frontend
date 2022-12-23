from django.db.models import Q, Min, Max
from django.http import JsonResponse
from backend.models import *
import json
import pandas as pd
from fuzzywuzzy import fuzz
import time
import datetime

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
        User.objects.create(name=name, email=email, password=password, photo='/img/head.d31cda9c.jpg')
    data = {'message':message}
    result = JsonResponse(dict(data))
    return result

def getUserInfo(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    id = content_dict.get('id')
    data = User.objects.get(id=id).to_dict()
    data = {'messsagee': '成功获取用户信息', "data": data}
    result = JsonResponse(dict(data))
    return result

def updateUser(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    update_content = content_dict.get('content')
    id = update_content['id']
    user = User.objects.get(id=id)
    user.name = update_content['name']
    user.profile = update_content['profile']
    user.gender = update_content['gender']
    user.email = update_content['email']
    user.likes = update_content['likeValue']
    user.dislikes = update_content['dislikeValue']
    user.photo = update_content['avatarPath']
    user.save()
    data = {'messsagee': '修改用户信息成功'}
    result = JsonResponse(dict(data))
    return result

def changePassword(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    update_content = content_dict.get('password')
    id = update_content['id']
    user = User.objects.get(id=id)
    if user.password == update_content['oldPassword']:
        user.password = update_content['newPassword']
        msg = '密码更新成功'
        data = 0
        user.save()
    else:
        msg = '原密码输入错误'
        data = 1
    data = {'messsage': msg, 'data': data}
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
        cover = content_dict['cover']
        if not Game.objects.filter(Q(name=name) & Q(date=date) & Q(rating=rating) & Q(platform=platform)):
            Game.objects.create(name=name, date=date, rating=rating, platform=platform, cover=cover)
    data = {'messsagee': '成功添加'}
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
    cover = content_dict['cover']
    if not Game.objects.filter(Q(name=name) & Q(date=date) & Q(rating=rating) & Q(platform=platform)):
        Game.objects.create(name=name, date=date, rating=rating, platform=platform, cover=cover)
    data = {'messsagee': '成功添加'}
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
        game = Game.objects.get(id=game_id)
        item = game.to_dict()
        tags = list(Tag.objects.filter(game_id=item['id']))
        item['tag'] = [tag.to_dict() for tag in tags]
        develops = list(Develop.objects.filter(game_id=item['id']))
        item['developer'] = []
        for develop in develops:
            item['developer'].append(develop.developer.to_dict())
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
    data = {'messsagee': '成功导出游戏数据', "data": data}
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
        game_list = list(game_dist.items())
        game_list.sort(key=lambda x:x[1], reverse=False)
        game_list = game_list[:10]
        games = [i[0] for i in game_list]
    data = [i.to_dict() for i in games]
    data = {'messsagee': '成功搜索游戏', "data": data}
    result = JsonResponse(dict(data))
    return result

def filterGame(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    country_id = content_dict.get('country_id')
    developer_id = content_dict.get('developer_id')
    discount_id = content_dict.get('discount_id')
    discount_rate = content_dict.get('discount_rate')
    start_date = content_dict.get('start_date')
    end_date = content_dict.get('end_date')
    data = []
    if discount_id == '0':
        discount_id = Discount.objects.all().order_by('-start_time').first().id
    game_ids = list(Price.objects.filter(country_id=country_id).values('game_id').distinct())
    for game_id in game_ids:
        id = game_id['game_id']
        game = Game.objects.get(id=id)
        # developer_id
        if developer_id != None and not Develop.objects.filter(game_id=id, developer_id=developer_id).exists():
           continue
        # date
        if start_date != None and end_date != None:
            start_date = time.strftime("%Y-%m-%d", time.localtime(start_date/1000))
            end_date = time.strftime("%Y-%m-%d", time.localtime(end_date/1000))
            if not Game.objects.filter(date__range=[start_date, end_date]).exists():
                continue
        # discount_id
        if not GameDiscount.objects.filter(game_id=id, discount_id=discount_id).exists():
            continue
        # discount_rate
        if discount_rate != None and Discount.objects.get(id=discount_id).discount_rate > discount_rate:
            continue
        discount = Discount.objects.get(id=discount_id)
        current_price = Price.objects.filter(game_id=id, country=country_id).order_by('-date').first().current_price
        data_i = {'id': id, 'cover': game.cover, 'name': game.name, 'current_price': current_price, 'discount_rate': discount.discount_rate, 'start_time': discount.start_time, 'end_time': discount.end_time}
        data.append(data_i)
    data = {'messsagee': '成功过滤得到游戏数据', "data": data}
    result = JsonResponse(dict(data))
    return result

def getGamePhoto(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    data = list(GamePhoto.objects.filter(game_id=game_id))
    data = [i.to_dict() for i in data]
    data = {'messsagee': '成功获取游戏图片', "data": data}
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
    data = {'messsagee': '成功导出该用户收藏夹', "data": data}
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

def isFavorites(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    user_id = content_dict.get('user_id')
    if Favorites.objects.filter(Q(user_id=user_id) & Q(game_id=game_id)).exists():
        data = {'data': True}
    else:
        data = {'data': False}
    result = JsonResponse(dict(data))
    return result

def getHeat(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    time = content_dict.get('time')
    if game_id != None:
        now = datetime.datetime.now()
        if time == 'year':
            delta = datetime.timedelta(days=365)
        elif time == 'month':
            delta = datetime.timedelta(days=30)
        elif time == 'week':
            delta = datetime.timedelta(days=7)
        else:
            delta = datetime.timedelta(days=36500)
        start_date = (now - delta).strftime('%Y-%m-%d')
        heats = list(Heat.objects.filter(game_id=game_id, date__gt=start_date).order_by('date'))
        data = []
        for heat in heats:
            data.append({'value': [heat.date, heat.players]})
    else:
        # t = time.localtime()
        # date = datetime.date(t.tm_year, t.tm_mon, t.tm_mday)
        games = list(Heat.objects.all().values('game_id').distinct())
        data = []
        for game in games:
            heat = Heat.objects.filter(game_id=game['game_id']).order_by('-date').first()
            data_i = heat.to_dict()
            data_i['game_name'] = heat.game.name
            data_i['game_cover'] = heat.game.cover
            data_i['max_heat'] = Heat.objects.filter(game_id=heat.game_id).aggregate(res=Max('players'))['res']
            data.append(data_i)
    data = {'messsagee': '成功导出游戏热度数据', "data": data}
    result = JsonResponse(dict(data))
    return result 

def getDiscount(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    country = content_dict.get('country')
    if country != None:
        data = list(GameDiscount.objects.filter(game_id=game_id, country=country))
        data = [i.to_dict() for i in data]
    elif game_id != None:
        data = list(GameDiscount.objects.filter(game_id=game_id))
        data = [i.to_dict() for i in data]
    else:
        discounts = list(Discount.objects.all())
        data = []
        for i in discounts:
            data_i = {}
            data_i['value'] = i.id
            data_i['label'] = i.name
            data.append(data_i)
    data = {'messsagee': '成功导出游戏折扣数据', "data": data}
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
    data = {'messsagee': '成功导出游戏标签', "data": data}
    result = JsonResponse(dict(data))
    return result

def getCountry(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    countries = list(Price.objects.all().values('country_id').distinct())
    data = []
    for i in countries:
        id = i['country_id']
        country = Country.objects.get(id=id)
        data_i = {}
        data_i['value'] = country.id
        data_i['label'] = country.name
        data.append(data_i)
    data = {'messsagee': '成功导出所有国家', "data": data}
    result = JsonResponse(dict(data))
    return result

def getPrice(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    country = content_dict.get('country')
    time = content_dict.get('time')
    if country != None:
        now = datetime.datetime.now()
        if time == 'year':
            delta = datetime.timedelta(days=365)
        elif time == 'month':
            delta = datetime.timedelta(days=30)
        elif time == 'week':
            delta = datetime.timedelta(days=7)
        else:
            delta = datetime.timedelta(days=36500)
        start_date = (now - delta).strftime('%Y-%m-%d')
        prices = list(Price.objects.filter(game_id=game_id, country=country, date__gt=start_date).order_by('date'))
        data = []
        for price in prices:
            data.append({'value': [price.date, price.current_price]})
    else:
        # t = time.localtime()
        # date = datetime.date(t.tm_year, t.tm_mon, t.tm_mday)
        countries = list(Price.objects.filter(game_id=game_id).order_by('country').values('country_id').distinct())
        data = []
        for country in countries:
            price = Price.objects.filter(game_id=game_id, country=country['country_id']).order_by('-date').first()
            data_i = price.to_dict()
            data_i['country_name'] = price.country.name
            data_i['lowest_price'] = Price.objects.filter(game_id=game_id, country=price.country).aggregate(res=Min('current_price'))['res']
            data.append(data_i)
    data = {'messsagee': '成功导出游戏价格', "data": data}
    result = JsonResponse(dict(data))
    return result

def getGoods(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    buyer_id = content_dict.get('buyer_id')
    seller_id = content_dict.get('seller_id')
    status = content_dict.get('status')
    if game_id != None:
        goods = list(Goods.objects.filter(game_id=game_id))
    elif buyer_id != None:
        goods = list(Goods.objects.filter(buyer_id=buyer_id))
    elif seller_id != None:
        if status != None:
            goods = list(Goods.objects.filter(seller_id=seller_id, status=status))
        else:
            goods = list(Goods.objects.filter(seller_id=seller_id))
    data = []
    for i in goods:
        goods_dict = i.to_dict()
        goods_dict['seller_name'] = i.seller.name
        goods_dict['game_name'] = i.game.name
        goods_dict['game_cover'] = i.game.cover
        data.append(goods_dict)
    data = {'messsagee': '成功导出商品', "data": data}
    result = JsonResponse(dict(data))
    return result

def addGoods(request):
    content = request.body.decode()
    content_dict = json.loads(content).get('goods')
    print(content_dict)
    price = content_dict['moneyValue']
    game_id = content_dict['game_id']
    seller_id = content_dict['seller_id']
    steam_id = content_dict['steamValue']
    decription = content_dict['introValue']
    cd_key = content_dict['keyValue']
    status = '已上架'
    Goods.objects.create(seller_id=seller_id, game_id=game_id, price=price, steam_id=steam_id, status=status, decription=decription, cd_key=cd_key)
    data = {'message': '上架商品成功'}
    result = JsonResponse(dict(data))
    return result

def delGoods(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    id = content_dict.get('id')
    if isinstance(id, list):
        for id_i in id:
            if Goods.objects.filter(Q(id=id_i)).exists():
                item = Goods.objects.filter(Q(id=id_i))
                item.delete()
    else:
        if Goods.objects.filter(Q(id=id)).exists():
            item = Goods.objects.filter(Q(id=id))
            item.delete()
    data = {'message': '删除商品成功'}
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
    elif update_type == 'decription':
        goods.decription = update_content
    goods.save()
    data = {'messsage': '修改商品信息成功'}
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
    goods.status = '已付款'
    goods.save()
    data = {'messsage': '商品购买成功'}
    result = JsonResponse(dict(data))
    return result

def rateGoods(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    id = content_dict.get('id')
    rating = content_dict.get('rating')
    comment = content_dict.get('comment')
    goods = Goods.objects.get(id=id)
    seller = goods.seller
    if rating == 'like':
        seller.likes += 1
    else:
        seller.dislikes += 1
    goods.comment = comment
    goods.status = '交易成功'
    goods.rating = rating
    goods.save()
    data = {'messsage': '订单评价成功'}
    result = JsonResponse(dict(data))
    return result

def getDeveloper(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    data = list(Develop.objects.all())
    data = [i.developer.to_dict() for i in data]
    for i in range(len(data)):
        data[i]['value'] = data[i].pop('id')
        data[i]['label'] = data[i].pop('name')
    data = {'messsagee': '成功导出所有发行商', "data": data}
    result = JsonResponse(dict(data))
    return result

def getComment(request):
    content = request.body.decode()
    content_dict = json.loads(content)
    print(content_dict)
    game_id = content_dict.get('game_id')
    user_id = content_dict.get('user_id')
    comments = list(Comment.objects.filter(game_id=game_id).order_by('-time'))
    data = []
    for comment in comments:
        flag = 0
        if user_id != None and Like.objects.filter(comment_id=comment.id, user_id=user_id).exists():
            flag = 1
        data_i = comment.to_dict()
        data_i['likes'] = Like.objects.filter(comment_id=comment.id).count()
        data_i['flag'] = flag
        data_i['user_name'] = comment.user.name
        data_i['user_photo'] = comment.user.photo
        data.append(data_i)
    data = {'messsagee': '成功导出评论', "data": data}
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
    comment_id = content_dict.get('comment_id')
    user_id = content_dict.get('user_id')
    update_type = content_dict.get('type')
    if update_type == 'like':
        Like.objects.create(comment_id=comment_id, user_id=user_id)
    elif update_type == 'dislike':
        item = Like.objects.filter(comment_id=comment_id, user_id=user_id)
        item.delete()
    data = {'messsage': '更新评论成功'}
    result = JsonResponse(dict(data))
    return result

def getSlide(request):
    data = list(Slide.objects.all())
    data = [i.to_dict() for i in data]
    data = {'messsagee': '成功导出所有轮播图', "data": data}
    result = JsonResponse(dict(data))
    return result

def getNews(request):
    data = list(News.objects.all())
    data = [i.to_dict() for i in data]
    data = {'messsagee': '成功导出所有新闻', "data": data}
    result = JsonResponse(dict(data))
    return result