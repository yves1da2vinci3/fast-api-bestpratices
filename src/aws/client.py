# Client for AWS interactions
import boto3

def get_s3_client():
    return boto3.client('s3')
