# Deployment Walkthrough

## Step 1 - Deploy Lambda Function
- Open AWS Lambda console
- Create new function `url-monitor-get-latest`
- Runtime: Python 3.12
- Paste code from `lambda/url-monitor-handler.py`
- Click **Deploy**

![Lambda Deploy](https://github.com/dixshakamble-aws/Serverless-URL-Monitor/blob/main/images/lamcodepass.png)

## Step 2 - Create DynamoDB Table
- Open DynamoDB console
- Create table `UrlMonitor`
- Partition key: `url` (String)
- No sort key needed
- Click **Create table**

![DynamoDB Table](https://github.com/dixshakamble-aws/Serverless-URL-Monitor/blob/main/images/DBtablerun.png)

## Step 3 - Enable Function URL
- In Lambda → Configuration → Function URL
- Click **Create function URL**
- Auth type: **NONE**
- CORS: Default
- Click **Save**

![Function URL](https://github.com/dixshakamble-aws/Serverless-URL-Monitor/blob/main/images/lambdacode.png)

## Step 4 - Test API
https://<your-function-url>/?url=https://aws.amazon.com

text

Expected response:
```json
{
  "url": "https://aws.amazon.com",
  "timestamp": "2026-02-13T...",
  "statusCode": 200,
  "latencyMs": 245
}
API Response
```
##Cleanup
- Delete Lambda function

- Delete DynamoDB table UrlMonitor






