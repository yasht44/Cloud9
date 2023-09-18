import boto3 #PythonSDK for AWS

s3 = boto3.client('s3')

response = s3.list_buckets()

buckets=response["Buckets"]

for bucket in buckets:
    print(bucket["Name"])
