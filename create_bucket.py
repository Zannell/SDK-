import boto3

client=boto3.client('s3')

try:
    response=client.create_bucket(
        Bucket="zoelas-bucket",
        CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'}
    )
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")


    
