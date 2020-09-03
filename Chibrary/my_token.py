import json
import os
import traceback
from Chibrary.server import my_app, db
from Chibrary.utils import *
from sts.sts import *

config = {
    'url': 'https://sts.tencentcloudapi.com/',
    'domain': 'sts.tencentcloudapi.com',
    # 临时密钥有效时长，单位是秒
    'duration_seconds': 7200,  # 12分钟
    'secret_id': config.config.cos_secret.secret_id,
    # 固定密钥
    'secret_key': config.config.cos_secret.secret_key,
    # 设置网络代理
    # 'proxy': {
    #     'http': 'xx',
    #     'https': 'xx'
    # },
    # 换成你的 bucket
    'bucket': config.config.cos_secret.bucket,
    # 换成 bucket 所在地区
    'region': config.config.cos_secret.region,
    # 这里改成允许的路径前缀，可以根据自己网站的用户登录态判断允许上传的具体路径
    # 例子： a.jpg 或者 a/* 或者 * (使用通配符*存在重大安全风险, 请谨慎评估使用)
    'allow_prefix': config.config.cos_secret.path,
    # 密钥的权限列表。简单上传和分片需要以下的权限，其他权限列表请看 https://cloud.tencent.com/document/product/436/31923
    'allow_actions': [
        # 简单上传
        'name/cos:PutObject',
        'name/cos:PostObject',
        # 分片上传
        'name/cos:InitiateMultipartUpload',
        'name/cos:ListMultipartUploads',
        'name/cos:ListParts',
        'name/cos:UploadPart',
        'name/cos:CompleteMultipartUpload'
    ],
}


def get_cos_token():
    try:
        sts = Sts(config)
        response = sts.get_credential()
        # print('get data : ' + json.dumps(dict(response), indent=4))
        return dict(response)
    except Exception as e:
        traceback.print_exc()
        logger.warning('Met errors: %s' % str(e))
        return None


# 获取cos上传鉴权
@my_app.route('/api/v1/cos/getToken')
@login_check
def get_cos_token_web():
    token_data = get_cos_token()
    return make_result(0, data={
        'cosToken': token_data
    })
