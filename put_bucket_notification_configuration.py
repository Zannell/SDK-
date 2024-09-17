import boto3

s3 = boto3.client('s3')

try:
    response = s3.put_bucket_notification_configuration(
        Bucket='zoelas-bucket', # Add your bucket name here
        NotificationConfiguration={
            "LambdaFunctionConfigurations": [
                {
                    # Input your actual Lambda ARN here:
                    "LambdaFunctionArn": "arn:aws:lambda:eu-west-1:065141254578:function:detect_image_uploaded_to_s3",
                    "Events": [
                        "s3:ObjectCreated:*"
                    ],
                    "Filter": {
                        "Key": {
                            "FilterRules": [
                                {
                                    "Name": "Prefix",
                                    "Value": "images/"
                                }
                            ]
                        }
                    }
                }
            ]
        }
    )
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")