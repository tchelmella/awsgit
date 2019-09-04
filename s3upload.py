import boto3
s3 = boto3.resource('s3')
s3.create_bucket(Bucket= 'tulsidas-web')
s3.Object('tulsidas-web','webdata.csv').upload_file(Filename='/home/ubuntu/pandas/webscraping/webdata.csv')
