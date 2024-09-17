import boto3

client = boto3.client('lambda')

try:
    response = client.add_permission(
        FunctionName='detect_image_uploaded_to_s3',
        StatementId="s3invoke",
        Action="lambda:InvokeFunction",
        Principal="s3.amazonaws.com",
        SourceArn="arn:aws:s3:::zoelas-bucket" # Add your bucket name here
    )
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")