import json
import boto3


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
        sound_file = data["file_url"]
        payload = json.dumps({'audio_path': sound_file})

        # Invoke the endpoint
        response = self.sagemaker_runtime.invoke_endpoint(
            EndpointName='waver-endpoint',
            ContentType='application/json',
            Body=payload,
        )
        output = json.loads(response['Body'].next().decode())

        return output
