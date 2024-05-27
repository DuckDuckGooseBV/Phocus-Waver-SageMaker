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
        """
        Performs a request to call Waver in SageMaker.

        :param data: The request data.
        :return: The output of the Waver SageMaker request
        """
        print("Processing request for deployment waver-sagemaker")

        # Convert the input to the SageMaker deployment to JSON format
        audio_file_path = get_path(data["file_url"])

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


def get_path(file_path_url):
    """
    Extracts the path from the url.

    :param file_path_url: The url to the audio file.
    :return: The real path to the file.
    """
    audio_file_path = urlparse(
        file_path_url
    ).path

    if len(audio_file_path) < 1:
        return ''

    # Remove first '/'
    audio_file_path = audio_file_path[1:]
    return audio_file_path