import json
from urllib.parse import urlparse

import boto3

from config import S3_BUCKET
from config import SAGEMAKER_ENDPOINT_NAME


class Deployment:

    def __init__(
            self,
            base_directory: str,
            context: dict = None,
    ):
        self.sagemaker_runtime = boto3.client(
            'sagemaker-runtime',
            region_name='eu-central-1',
        )
        print("Initialising deployment waver-sagemaker")

    def request(self, data):
        print("Processing request for deployment waver-sagemaker")

        # Convert the input to the SageMaker deployment to JSON format
        audio_file_path = urlparse(
            data["file_url"]
        ).path

        payload = json.dumps({
            'audio_path': audio_file_path,
            'bucket': S3_BUCKET
        })

        # Invoke the endpoint
        response = self.sagemaker_runtime.invoke_endpoint(
            EndpointName=SAGEMAKER_ENDPOINT_NAME,
            ContentType='application/json',
            Body=payload,
        )
        output = json.loads(response['Body'].next().decode())

        return output

