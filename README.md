# Phocus-Waver-SageMaker

This project defines a UbiOps deployment that will call Waver in AWS SageMaker to perform audio analysis.


### Environment variables

| Key                     | Description                                    |
|-------------------------|------------------------------------------------|
| SAGEMAKER_ENDPOINT_NAME | The name of the Waver endpoint in SageMaker    |
| S3_BUCKET               | The S3 bucket in which the file is saved       |
| AWS_ACCESS_KEY_ID       | The AWS key which has access to your S3 bucket |
| AWS_SECRET_ACCESS_KEY   | The AWS secret key to access your S3 bucket    |