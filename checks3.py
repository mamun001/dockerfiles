from boto3.session import Session

ACCESS_KEY='foo'
SECRET_KEY='bar'


session = Session(aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')
your_bucket = s3.Bucket('foo-bucket')

#This works too
#for s3_file in your_bucket.objects.all():
    #print(s3_file.key)


if your_bucket.creation_date:
   print("OK")  # bucket exists
else:
   print("NOT OK")  # bucket does not exist or no access or not reachable


