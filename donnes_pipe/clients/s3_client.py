from dataclasses import dataclass
from donnes_pipe.connector_interfaces import ConnectClient
from contextlib import contextmanager


@dataclass
class S3Client(ConnectClient):
    def connect(self):
        pass

    @contextmanager
    def connect(self):
        try:
            yield self
        except Exception as e:
            raise e

    @dataclass
    class Api:
        bucket: str = "poc-s3-dev-static-site-platzi"
