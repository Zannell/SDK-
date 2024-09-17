import boto3
import json

iam = boto3.client('iam')

trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

rekognition_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObjectTagging",
            ],
            "Resource": [
                "arn:aws:s3:::zoelas-bucket/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "rekognition:DetectLabels",
            ],
            "Resource": "*"
        }
    ]
}

try:
    response = iam.create_role(
        RoleName='LambdaRekognitionRole',
        AssumeRolePolicyDocument=json.dumps(trust_policy)
    )
    role = response['Role']

    iam.put_role_policy(
        RoleName=role['RoleName'],
        PolicyName='RekognitionDetectLabelsPolicy',
        PolicyDocument=json.dumps(rekognition_policy)
    )

    print(role['Arn'])

except Exception as e:
    print(f"An error occurred: {e}")