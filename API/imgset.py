import json


def lambda_handler(event, context):

    imgname = event['params']['querystring']['name']

    return {
        'statusCode': 200,
        'body': json.dumps({"name": imgname})



    }
