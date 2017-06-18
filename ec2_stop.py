import sys
import boto3
from botocore.exceptions import ClientError

instance_id = 'YOUR AWS INSTANCE ID'

ec2 = boto3.client('ec2')

try:
	ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
except ClientError as e:
	if 'DryRunOperation' not in str(e):
		raise


try: 
	response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
	print(response)
except:
	print(e)

















