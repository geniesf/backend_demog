
import boto
import boto.s3
import sys
from boto.s3.key import Key
import boto3

AWS_ACCESS_KEY_ID = 'AKIAIFTHF27VIG4SXW7Q'
AWS_SECRET_ACCESS_KEY = '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'
bucket_name = 'genie1'

conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)

bucket = conn.get_bucket(bucket_name)

client=boto3.client('rekognition')

photo = "niketest.jpg"
  
response=client.detect_text(Image={'S3Object':{'Bucket':bucket_name,'Name':photo}})
                    
textDetections=response['TextDetections']
print ('Detected text')
for text in textDetections:
        print ('Detected text:' + text['DetectedText'])
        print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        print ('Id: {}'.format(text['Id']))
        if 'ParentId' in text:
            print ('Parent Id: {}'.format(text['ParentId']))
        print ('Type:' + text['Type'])
        print

