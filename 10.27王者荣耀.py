import requests,re,json
from lxml import html

def get_hero():
    # 请求地址
    url = 'https://pvp.qq.com/web201605/herolist.shtml'
    #请求头
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    #请求网页
    response = requests.get(url,headers = header)
    response.encoding = 'gbk'
    print(response.text)
    #转化对象
    page = html.etree.HTML(response.text)
    #使用xpath
    hero_li = page.xpath('//ul[@class="herolist clearfix"]/li')
    num = 0
    for hero in hero_li:
        name = hero.xpath('.//img/@alt')[0]
        img = hero.xpath('.//img/@src')[0]
        print(name,'https:'+img)
        num+=1
    print(num)
# get_hero()

def get_hero2():
    #小头像
    s_img = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/{}/{}.jpg'
    #皮肤
    b_img = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-2.jpg'
    url = 'https://pvp.qq.com/web201605/js/herolist.json'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.get(url,headers = header)
    # print(response.text)
    info = json.loads(response.text)
    for item in info:
        ename = item['ename']
        cname = item['cname']
        s_pic = s_img.format(ename,ename)
        skin = b_img.format(ename,ename)
        # print(ename,cname,s_pic,skin)
    pass
get_hero2()