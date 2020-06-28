# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv('data/iris.data', 
                   names=['sepal length', 'sepal width', 
                          'petal length', 'petal width', 
                          'label'])

# Shuffle the data to make deploy_test samples random
# Ignore ML conventions regarding train/test split etc. as this is about AWS
data = data.sample(frac=1).reset_index(drop=True)
train = data[:-3]
deploy_test = data[-3:]
train.to_csv('train.csv')
deploy_test.to_csv('deploy_test.csv')

# Create an S3 bucket and upload data
import boto3
bucket = 'replace-with-your-bucket-name'
region = 'us-east-1'
s3_session = boto3.Session().resource('s3')
s3_session.create_bucket(Bucket=bucket
                         #, this location constraint is needed for all regions
                         # except for us-east-1
			 # uncomment if you are using e.g. eu-west-2 
                         #CreateBucketConfiguration=
                         #{'LocationConstraint': region}
                         )
s3_session.Bucket(bucket).Object('train.csv').upload_file('train.csv')