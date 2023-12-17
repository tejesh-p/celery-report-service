import logging
import os

import boto3
from botocore.exceptions import ClientError

from app.settings import settings


def upload_file_to_s3(file_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client('s3', aws_access_key_id=settings.S3_ACCESS_KEY,
                             aws_secret_access_key=settings.S3_SECRET_KEY
                             )
    try:
        response = s3_client.upload_file(file_name, settings.S3_BUCKET_NAME, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
