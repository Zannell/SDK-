import boto3

s3 = boto3.client('s3')

bucket_name = 'zoelas-bucket' # Input your actual bucket name
file_name = './cat.jpeg'
object_name = 'images/cat.jpeg'

try:
    response = s3.upload_file(file_name, bucket_name, object_name)
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")