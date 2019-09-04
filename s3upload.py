# Import boto3 library for Python.
import boto3

# Calling the s3 service.
s3 = boto3.resource('s3')

# Create a s3 bucket.
s3.create_bucket(Bucket= 'tulsidas-web')

# Create a object to upload a file.
s3.Object('tulsidas-web','webdata.csv').upload_file(Filename='/home/ubuntu/pandas/webscraping/webdata.csv')
