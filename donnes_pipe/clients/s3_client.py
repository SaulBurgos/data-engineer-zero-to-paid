import boto3
from botocore import UNSIGNED
from botocore.client import Config
from dataclasses import dataclass
from donnes_pipe.connector_interfaces import ConnectClient
from contextlib import contextmanager


@dataclass
class S3Client(ConnectClient):
    s3_client: boto3.client = None

    @contextmanager
    def connect_to_public(self):
        try:
            self.s3_client = boto3.client(
                "s3", config=Config(signature_version=UNSIGNED)
            )
            self.s3_client.list_objects(Bucket=self.config.get("bucket"))

            self.api = self.Api(
                s3_client=self.s3_client, bucket=self.config.get("bucket")
            )
            yield self
        except Exception as e:
            raise e

    @contextmanager
    def connect(self):
        try:
            self.s3_client = boto3.client(
                "s3",
                aws_access_key_id=self.config.get("aws_access_key_id"),
                aws_secret_access_key=self.config.get("aws_secret_access_key"),
                region_name=self.config.get("region_name"),
            )

            self.api = self.Api(
                s3_client=self.s3_client, bucket=self.config.get("bucket")
            )
            yield self
        except Exception as e:
            raise e

    @dataclass
    class Api:
        s3_client: boto3.client
        bucket: str

        def list_objects(self):
            return self.s3_client.list_objects(Bucket=self.bucket)
