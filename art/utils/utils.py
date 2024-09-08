import boto3
from dotenv import load_dotenv
import os


def upload_image(file):
    if file._name == '':
        return False, 'No selected file'
    try:
        load_dotenv()
        s3_client = boto3.client(
            's3',
            region_name=os.getenv('S3_REGION'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
        )
        s3_client.upload_fileobj(
            file.file,
            os.getenv('S3_BUCKET'),
            file._name,
        )
        file_url = f"https://{os.getenv('S3_BUCKET')}.s3.{os.getenv('S3_REGION')}.amazonaws.com/{file._name}"
        return True, file_url
    except Exception as e:
        return False, str(e)