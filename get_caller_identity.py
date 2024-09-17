import boto3

try:
    client = boto3.client('sts')
    response = client.get_caller_identity()
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")