# Utility functions for the AWS module
from botocore.exceptions import ClientError

def handle_s3_error(error: ClientError):
    print(error.response['Error']['Message'])
