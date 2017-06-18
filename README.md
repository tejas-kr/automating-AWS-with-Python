# automating-AWS-with-Python
automating AWS with Python using boto3 library

# You have to add credentials and config files in the .aws directory. Just paste the following code
Create the credentials file. By default, its location is at ~/.aws/credentials:
<pre>
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
</pre>

You may also want to set a default region. This can be done in the configuration file. By default, its location is at ~/.aws/config:
<pre>
[default]
region=us-east-1
</pre>

## Note
You can automate this script using crontab in linux. I don't know about windows and mac but you can surely google it.


