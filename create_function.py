import boto3

client = boto3.client('lambda')

try:
    with open('lambda_function.zip', 'rb') as f:  # Specify name of .zip file from last section
        file_contents = f.read()

    response = client.create_function(
        FunctionName='detect_image_uploaded_to_s3',
        Runtime='python3.11',
        Role='arn:aws:iam::065141254578:role/LambdaRekognitionRole',  # Correct ARN format
        Handler='lambda_function.handler',
        Code={
            'ZipFile': file_contents
        }
    )

    print(response['FunctionArn'])

except Exception as e:
    print(f"An error occurred: {e}")
