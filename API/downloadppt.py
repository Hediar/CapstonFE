import json
import boto3
import base64
from botocore.config import Config

s3_client_config = Config(
    region_name='ap-northeast-2',
    signature_version='s3v4',
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    }
)


def lambda_handler(event, context):

    s3 = boto3.client("s3", config=s3_client_config)

    bucket_name = event['params']['path']['bucket']
    file_name = event['params']['querystring']['file']

    print(bucket_name, file_name)
    URL = s3.generate_presigned_url(
        'get_object', Params={'Bucket': bucket_name, 'Key': file_name}, ExpiresIn=10000)

    return {

        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': {"URL": URL}
    }
