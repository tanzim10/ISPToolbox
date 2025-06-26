# (c) Meta Platforms, Inc. and affiliates. Copyright
# Utility function to get secrets from AWS Secret Manager

import boto3
import base64
from botocore.exceptions import ClientError

#--local--#

import os
import json

def get_secret(secret_name):
    """
    Return secrets from AWS if PROD is true,
    else return dummy data for local development.
    """
    if os.environ.get("PROD", "false").lower() == "true":
        import boto3
        import botocore

        client = boto3.client("secretsmanager")
        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
            return get_secret_value_response["SecretString"]
        except botocore.exceptions.ClientError as e:
            raise e
    else:
        # LOCAL FALLBACK - return dummy or empty values
        dummy_data = {
            "fb_sdk_isptoolbox_app_key": "dev-key",
            "fb_sdk_isptoolbox_app_secret": "dev-secret",
            "fb_isptoolbox_page_id": "123456789",
            "asn_fb_curl": "dummy-secret",
            "MAPBOX_ACCESS_TOKEN_BACKEND": "pk.test.token",
            "MAPBOX_ACCOUNT_PASSWORD": "test-password",
            "MAPBOX_ACCOUNT_EMAIL": "test@example.com",
            "MAPBOX_PUBLIC_ACCESS_TOKEN_ALLOW_ALL_URL": "pk.public.allow.url",
            "MAPBOX_PUBLIC_ACCESS_TOKEN_FB_ISPTOOLBOX_URL": "pk.public.fb.url",
            "TILESET_LAMBDA_EDGE_SECRET": "tileset-secret",
            "cloud_rf_uid": "cloudrf-uid",
            "cloud_rf_key": "cloudrf-key",
            "ENDPOINT_ELASTICSEARCH": "http://localhost:9200",
            "ADMIN_ELASTICSEARCH": "elastic",
            "PASSWORD_ELASTICSEARCH": "changeme",
            "name": "django_test",
            "username": "postgres",
            "password": "password",
            "host": "localhost",
            "port": "5432",
            "GOOGLE_ELEVATION_API_KEY": "dummy-elevation-key",
            "msft_earth_ai_key_primary": "ai-key-1",
            "msft_earth_ai_key_secondary": "ai-key-2",
        }
        return json.dumps(dummy_data)


#----#


# def get_secret(secret_name, **kwargs):

#     region_name = "us-west-1"

#     # Create a Secrets Manager client
#     session = boto3.session.Session(**kwargs)
#     client = session.client(
#         service_name='secretsmanager',
#         region_name=region_name
#     )

#     try:
#         get_secret_value_response = client.get_secret_value(
#             SecretId=secret_name
#         )
#     except ClientError as e:
#         if e.response['Error']['Code'] == 'DecryptionFailureException':
#             # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
#             # Deal with the exception here, and/or rethrow at your discretion.
#             raise e
#         elif e.response['Error']['Code'] == 'InternalServiceErrorException':
#             # An error occurred on the server side.
#             # Deal with the exception here, and/or rethrow at your discretion.
#             raise e
#         elif e.response['Error']['Code'] == 'InvalidParameterException':
#             # You provided an invalid value for a parameter.
#             # Deal with the exception here, and/or rethrow at your discretion.
#             raise e
#         elif e.response['Error']['Code'] == 'InvalidRequestException':
#             # You provided a parameter value that is not valid for the current state of the resource.
#             # Deal with the exception here, and/or rethrow at your discretion.
#             raise e
#         elif e.response['Error']['Code'] == 'ResourceNotFoundException':
#             # We can't find the resource that you asked for.
#             # Deal with the exception here, and/or rethrow at your discretion.
#             raise e
#     else:
#         # Decrypts secret using the associated KMS CMK.
#         # Depending on whether the secret is a string or binary, one of these fields will be populated.
#         if 'SecretString' in get_secret_value_response:
#             secret = get_secret_value_response['SecretString']
#             return secret
#         else:
#             decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
#             return decoded_binary_secret
