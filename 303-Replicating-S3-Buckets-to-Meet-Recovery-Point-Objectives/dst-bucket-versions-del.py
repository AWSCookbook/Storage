import boto3
import os
session = boto3.Session()
s3 = session.resource(service_name='s3')
bucket = s3.Bucket('awscookbook303-dst-' + os.environ["EXPORTED_RANDOM_STRING"])
bucket.object_versions.delete()
bucket.delete()
