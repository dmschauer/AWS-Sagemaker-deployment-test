# -*- coding: utf-8 -*-

# Deploy the model
from sagemaker.sklearn.estimator import SKLearn

role = 'SageMakerFullAccess_sklearn_api_test'

# Create the SKLearn Object by directing it to the aws_sklearn_main.py script
aws_sklearn = SKLearn(entry_point='aws_sklearn_main.py',
                      train_instance_type='ml.m4.xlarge',
                      role=role)

# Train the model using by passing the path to the S3 bucket with the training data
aws_sklearn.fit({'train': 's3://replace-with-your-bucket-name/'})

# Deploy model
aws_sklearn_predictor = aws_sklearn.deploy(instance_type='ml.t2.medium', 
                                           initial_instance_count=1)

# Print the endpoint to test in next step
print(aws_sklearn_predictor.endpoint)

# Uncomment and run to terminate the endpoint after you are finished
#predictor.delete_endpoint()