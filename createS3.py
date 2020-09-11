import boto3

aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("bazzasbucket1976")
response = bucket.create(
ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1'
    },
)

print(response)
