# AWS Sagemaker API test

I did a simple test to see how deploying a machine learning model on AWS Sagemaker and thus turning it into an API works.
Since scikit-learn models require less dependencies than e.g. TensorFlow models I went with them for this test.
To do so I used a tutorial.

Though not explicitly mentioned in the text, this tutorial assumes that you have AWS CLI setup on your local machine.
Keep this in mind if you run into ValueError: Must setup local AWS configuration with a region supported by SageMaker.

The steps termed '(optional)' in the tutorial aren't optional at all. Rather in the context of this tutorial they are crucial for things to function.

Also as of writing this, your training script must be a Python 2.7 or 3.6 compatible source file for the sagemaker library Version 1.66 to work.

### My environment used during the test:
- Windows 10 64-Bit
- Python 3.7.7
- (Spyder 4.1.3)
- (Anaconda 4.8.3)

### Dependencies:
- boto3=1.14.12=pypi_0
- botocore=1.17.12=pypi_0
- numpy=1.18.5=pypi_0
- pandas=1.0.5=pypi_0
- sagemaker=1.66.0=pypi_0
- scikit-learn=0.23.1=pypi_0
see also requirements.txt

### Tutorial link:
https://towardsdatascience.com/deploying-a-scikit-learn-model-on-aws-using-sklearn-estimators-local-jupyter-notebooks-and-the-d94396589498
