import sys
import boto3
from botocore.exceptions import ClientError

instance_id = 'YOUR AWS INSTATNCE ID'

ec2 = boto3.client('ec2')

try:
	ec2.start_instances(InstanceIds = [instance_id], DryRun=True)
except ClientError as e:
	if 'DryRunOperation' not in str(e):
		raise

try:
	response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
	print(response)
except ClientError as e:
	print(e)




















	


