"""Helper functions for interacting with AWS's S3 service"""
from typing import Union, Dict
import json
from uuid import uuid4

import boto3
from loguru import logger as log

from settings import app
from settings import aws


def get_s3_client(name: str) -> boto3.session.Session.client:
    """Gets s3 client

    Args:
        name: Client's name

    Returns: S3 representation of a client
    """
    if app.ENVIRONMENT in ['local', 'docker']:
        client = boto3.client(
            name,
            aws_access_key_id=aws.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=aws.AWS_SECRET_ACCESS_KEY,
            region_name=aws.AWS_REGION,
        )
    else:
        client = boto3.client(
            name,
            region_name=aws.AWS_REGION,
        )

    return client


def get_s3_resource() -> object:
    """Gets s3 resource

    Returns:
        Object representing s3 resource
    """
    if app.ENVIRONMENT in ['local', 'docker']:
        s3_resource = boto3.resource(
            's3',
            aws_access_key_id=aws.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=aws.AWS_SECRET_ACCESS_KEY,
            region_name=aws.AWS_REGION,
        )
    else:
        s3_resource = boto3.resource(
            's3',
            region_name=aws.AWS_REGION,
        )

    return s3_resource


def upload_file_to_s3(
    data: object = None,
    bucket_name: str = None,
    object_key: str = None
) -> str:
    """Uploads file to s3

    Args:
        data: Data to upload
        bucket_name: Bucket name to upload to
        object_key: optional param to set the object key. New UUID used if not provided

    Returns:
        S3 object_key of newly created object
    """
    if not object_key:
        object_key = str(uuid4())

    s3 = get_s3_resource()
    s3.meta.client.put_object(Body=data, Bucket=bucket_name, Key=object_key)

    return object_key


def download_s3_object(bucket_name: str, object_key: Union[str, uuid4], decode: bool = True) -> str:
    """Downloads s3 object

    Args:
        bucket_name: Bucket name to upload to
        object_key: optional param to set the object key
        decode: True or False if object should be decoded

    Returns:
        String containing s3 object
    """
    s3 = get_s3_resource()
    content_object = s3.Object(bucket_name, object_key)

    return (
        content_object.get()['Body'].read().decode('utf-8')
        if decode else content_object.get()['Body'].read()
    )


def download_s3_json_object(uri: str = None) -> Dict:
    """Downloads an s3 object containing JSON

    Args:
        uri: S3 object to download

    Returns:
        JSON representation of s3 object
    """
    file_content = download_s3_object(uri)
    return json.loads(file_content)


# def create_new_public_private_key_pair() -> tuple:
#     """Creates a new public and private key using RSA

#     Returns:
#         The tuple containing the object keys for the newly created private and public keys in S3
#     """
#     log.debug('Generating new public private key pair and storing in S3.')
#     private_key = RSA.generate(1024)
#     with open("private.pem", "wb") as tmp_private_pem_file:
#         tmp_private_pem_file.write(private_key.exportKey('PEM'))
#         private_pem_object_key = upload_file_to_s3(
#             data=tmp_private_pem_file,
#             bucket_name=aws.AUTHENTICATION_BUCKET_NAME,
#         )

#     pubkey = private_key.publickey()
#     with open("public.pem", "wb") as tmp_public_pem_file:
#         tmp_public_pem_file.write(pubkey.exportKey('OpenSSH'))
#         public_pem_object_key = upload_file_to_s3(
#             data=tmp_public_pem_file,
#             bucket_name=aws.AUTHENTICATION_BUCKET_NAME,
#         )

#     log.debug('Successfully created new public private key pair in S3.')
#     return private_pem_object_key, public_pem_object_key
