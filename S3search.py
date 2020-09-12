#Script to Search S3 Buckets using Boto3
import boto3

resource=boto3.resource("s3")
print(resource)
bucket_list=list(resource.buckets.all())
len(bucket_list)
for bucket in resource.buckets.all()):
    print(bucket.name)


