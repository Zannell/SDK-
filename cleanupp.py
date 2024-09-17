import boto3

# Create clients for IAM, Lambda, and S3
iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda')
s3_client = boto3.client('s3')

bucket_name = 'zoelas-bucket' # Your actual bucket name created in Step 1
role_name = 'LambdaRekognitionRole' # Your actual role name created in Step 2

try:
    # Delete IAM role policy and role
    iam_client.delete_role_policy(
        RoleName=role_name,
        PolicyName='RekognitionDetectLabelsPolicy'
    )
    print("IAM role policy deleted.")

    iam_client.delete_role(
        RoleName=role_name
    )
    print("IAM role deleted.")

    # Delete Lambda function
    lambda_client.delete_function(
        FunctionName='detect_image_uploaded_to_s3'
    )
    print("Lambda function deleted.")

    # Delete S3 object and bucket
    s3_client.delete_object(
        Bucket=bucket_name,
        Key='images/cat.jpeg'
    )
    print("S3 object deleted.")

    s3_client.delete_bucket(
        Bucket=bucket_name
    )
    print("S3 bucket deleted.")

except Exception as e:
    print(f"An error occurred: {e}")