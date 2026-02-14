# Serverless-URL-Monitor
A small serverless URL monitoring utility built with AWS Lambda and Amazon DynamoDB. The project stores HTTP check results (status code, latency, timestamp) for target URLs and exposes a simple read endpoint via Lambda Function URL to fetch the latest record for a given url query parameter.
