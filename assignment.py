import boto3
import uuid

s3client = boto3.client(
    's3',
    aws_access_key_id="AKIAQNEB3BIKII76ZR42",
    aws_secret_access_key="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"
)
#create bucket
bucket_name = 'assignment-utp1-{}'.format(uuid.uuid4())
print('Creating new bucket with name: {}'.format(bucket_name))
s3client.create_bucket(Bucket=bucket_name)

list_buckets_resp = s3client.list_buckets()
for bucket in list_buckets_resp['Buckets']:
    if bucket['Name'] == bucket_name:
        print('(Just created) --> {} - there since {}'.format(
            bucket['Name'], bucket['CreationDate']))


#create object

object_key = 'assignment.txt'

print('Uploading some data to {} with key: {}'.format(
    bucket_name, object_key))
s3client.put_object(Bucket=bucket_name, Key=object_key, Body=b'Yumaren&Jeevan!')

#retrieve uploaded bucket
url = s3client.generate_presigned_url(
    'get_object', {'Bucket': bucket_name, 'Key': object_key})
print('\nTry this URL in your browser to download the object:')
print(url)

try:
    input = raw_input
except NameError:
    pass
input("\nPress enter to continue...")

#list buckets
print('\nNow using Resource API')
s3resource = boto3.resource('s3',
                               aws_access_key_id="AKIAQNEB3BIKII76ZR42",
    aws_secret_access_key="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")
# Now, the bucket object
bucket = s3resource.Bucket(bucket_name)
# Then, the object object
obj = bucket.Object(object_key)
print('Bucket name: {}'.format(bucket.name))
print('Object key: {}'.format(obj.key))
print('Object content length: {}'.format(obj.content_length))
print('Object body: {}'.format(obj.get()['Body'].read()))
print('Object last modified: {}'.format(obj.last_modified))

#delete object
print('\nDeleting all objects in bucket {}.'.format(bucket_name))
delete_responses = bucket.objects.delete()
for delete_response in delete_responses:
    for deleted in delete_response['Deleted']:
        print('\t Deleted: {}'.format(deleted['Key']))

print('\nDeleting the bucket.')
bucket.delete()

#create dynamodb table
dynamodb = boto3.resource('dynamodb', aws_access_key_id="AKIAQNEB3BIKII76ZR42",
    aws_secret_access_key="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",
                               region_name='ap-southeast-1')

table = dynamodb.create_table(
    TableName='Smartphones1',
    KeySchema=[
        {
            'AttributeName': 'smartphone_name',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'year',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'smartphone_name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

#insert data
print(table.item_count)

dynamodb = boto3.resource('dynamodb', aws_access_key_id="AKIAQNEB3BIKII76ZR42",
    aws_secret_access_key="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",
                               region_name='ap-southeast-1')

table = dynamodb.Table('Smartphone')

table.put_item(
   Item={
        'smartphone_name': "Samsung",
        'year': 2018,
        'user' : "Yumaren"
    }
)

#query data
dynamodb = boto3.resource('dynamodb', aws_access_key_id="AKIAQNEB3BIKII76ZR42",
    aws_secret_access_key="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",
                               region_name='ap-southeast-1')
table = dynamodb.Table('Smartphone')

response = table.get_item(
    Key={
        'smartphone_name': "Samsung",
        'year': 2018
    }
)
item = response['Item']
print(item)

print(table.item_count)