import boto3

s3 = boto3.client('s3')

try:
    response = s3.get_object_tagging(
        Bucket='zoelas-bucket',  # Input your actual bucket name
        Key='images/cat.jpeg'
    )
    tag_values = [tag['Value'] for tag in response['TagSet']]
    output = ', '.join(tag_values)
    print(output)
except Exception as e:
    print(f"An error occurred: {e}")

 
