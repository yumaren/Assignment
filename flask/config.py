import boto3


def create_bucket(bucket_name):
    """
    Function to create bucket

    """
    name_bucket = bucket_name
    bucket = name_bucket-{}.format(uuid.uuid4())
    s3client = boto3.client(
    's3',
    aws_access_key_id="AKIAQNEB3BIKII76ZR42",
    aws_secret_access_key="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"
)
    # return ('Creating new bucket with name: {}'.format(bucket))
    response = s3client.create_bucket(bucket)
    
    return response


def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name
    s3client = boto3.client(
        's3',
        aws_access_key_id="AKIAQNEB3BIKII76ZR42",
        aws_secret_access_key="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"
    )
    response = s3client.upload_file(file_name, bucket, object_name)

    return response


def download_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3 = boto3.resource('s3',
        aws_access_key_id="AKIAQNEB3BIKII76ZR42",
        aws_secret_access_key="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")
    output = f"downloads/{file_name}"
    s3.Bucket(bucket).download_file(file_name, output)

    return output


def list_files(bucket):
    """
    Function to list files in a given S3 bucket
    """
    s3 = boto3.client('s3',
        aws_access_key_id="AKIAQNEB3BIKII76ZR42",
        aws_secret_access_key="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")
    contents = []
    try:
        for item in s3.list_objects(Bucket=bucket)['Contents']:
            print(item)
            contents.append(item)
    except Exception as e:
        pass

    return contents
