
import boto
import boto.s3
import sys
from boto.s3.key import Key
import boto3

# AWS_ACCESS_KEY_ID = 'AKIAIFTHF27VIG4SXW7Q'
# AWS_SECRET_ACCESS_KEY = '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'
# bucket_name = 'genie1'

# conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
#         AWS_SECRET_ACCESS_KEY)



# testfile = "testnike.jpg"

# print ('Uploading %s to Amazon S3 bucket %s'%(testfile, bucket_name))

# def percent_cb(complete, total):
#     sys.stdout.write('.')
#     sys.stdout.flush()

client = boto3.client('s3', region_name='us-east-1')        

client.upload_file('images/image_0.jpg', 'mybucket', 'image_0.jpg')