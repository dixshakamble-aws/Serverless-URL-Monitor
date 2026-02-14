import boto3
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("UrlMonitor")

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}

    if "url" not in params:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "url query parameter is required"})
        }

    url_value = params["url"]

    resp = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key("url").eq(url_value),
        ScanIndexForward=False,
        Limit=1
    )

    items = resp.get("Items", [])
    if not items:
        return {
            "statusCode": 404,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "no data found for this url"})
        }

    latest = items[0]

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(latest)
    }
