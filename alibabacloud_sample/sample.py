import os
import dotenv

from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109.client import Client
from alibabacloud_alidns20150109 import models


dotenv.load_dotenv()

access_key_id = os.getenv('ACCESS_KEY_ID')
access_key_secret = os.getenv('ACCESS_KEY_SECRET')

if access_key_id is None or access_key_secret is None:
    raise ValueError("ACCESS_KEY_ID and ACCESS_KEY_SECRET must be set in environment variables.")

# step1
# 初始化配置对象 alibabacloud_tea_openapi.Config 。 
# Config 对象存放存放 access_key_id 、access_key_secret 和 endpoint 等配置，Endpoint 如示例中的 alidns.cn-hangzhou.aliyuncs.com 。
# Endpoint 请参考 https://api.aliyun.com/product/Alidns
config = open_api_models.Config(
    access_key_id = access_key_id,
    access_key_secret = access_key_secret,
    endpoint='dns.aliyuncs.com'
)


# step2
# 实例化一个客户端，从 alibabacloud_alidns20150109.Client 类生成对象 client 。 
# 后续 request、response 从 alibabacloud_alidns20150109.models 中获得。
client = Client(config)

# step3
# 创建对应 API 的 Request 。 方法的命名规则为 API 名称加上 Request 。
request = models.DescribeDomainRecordsRequest()


# step4
# 设置请求类 request 的参数。 通过设置 request 类的属性设置参数，即 API 中必须要提供的信息。例如：
request.lang = 'zh'
request.domain_name = '3ncounter.cn'

# step5
# 通过 client 对象获得对应 request 响应 response 。
response = client.describe_domain_records(request)
print(response.body)

# step6
# 使用 try...except... 处理报错。
# from Tea.exceptions import UnretryableException

# try:
#     response = client.add_custom_line(request)
#     print(response)
# except UnretryableException as e:
#     print(e)
# except Exception as e:
#     print(e)
