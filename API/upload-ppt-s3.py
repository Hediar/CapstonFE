import boto3
import json
import base64
import hashlib
from datetime import datetime, timedelta
from requests_toolbelt.multipart import decoder

BUCKET_NAME = 'hknu-pptimage'

response = {
    'statusCode': 200,
    'headers': {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    },
    'body': ''
}


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    hash_salt = str(datetime.utcnow())
    file_path = 'ppt/'
    file_salt = hashlib.sha224(hash_salt.encode()).hexdigest()
    file_name = f'000{file_salt[:10].upper()}-{file_salt[10:15].upper()}-{file_salt[15:20].upper()}-{file_salt[20:25].upper()}'
    full_name = file_path + file_name + '.pptx'
    res_data = ''
    content = ''
    headers = ''

    body = base64.b64decode(event['body-json'])

    if 'content-type' in event['params']['header']:
        content_type = event['params']['header']['content-type']
    else:
        content_type = event['params']['header']['Content-Type']

    decode = decoder.MultipartDecoder(body, content_type)

    for part in decode.parts:
        content = part.content
        headers = part.headers
        print(part.__dict__)
    print(content)
    print(headers)

    try:

        s3_response = s3.put_object(
            Bucket=BUCKET_NAME, Key=full_name, Body=content)

    except Exception as e:
        raise IOError(e)

    response['body'] = json.dumps(
        {'url': f'{"https://s3.ap-northeast-2.amazonaws.com/hknu-pptimage"}/{file_path}{file_name}.pptx'})
    return response
