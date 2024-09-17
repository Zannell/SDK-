import boto3

session = boto3.session.Session()

rekognition = session.client('rekognition')
s3 = session.client('s3')

def handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}}
    )

    labels = []
    for label in response['Labels']:
        if label['Confidence'] > 80:
            labels.append(label['Name']) 

    labels = labels[:5]

    tag_set = []
    for i, label in enumerate(labels):
        tag_set.append({'Key': 'label'+str(i+1), 'Value': label})

    # Add tags to image 
    s3.put_object_tagging(
        Bucket=bucket,
        Key=key,
        Tagging={'TagSet': tag_set} 
    )