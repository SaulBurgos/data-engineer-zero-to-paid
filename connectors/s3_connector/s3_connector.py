from dataclasses import dataclass
from donnes_pipe.connector_interfaces import ConnectorELT, ConnectClient


@dataclass
class S3Connector(ConnectorELT):
    def extract_data(self, source_client: ConnectClient) -> dict:
        print("extracting")

    def transform_data(self, raw_data):
        print("transforming")

    def load_data(self, data, destination_client: ConnectClient):
        print("loading")

    def run(
        self,
        source_client: ConnectClient,
        destination_client: ConnectClient,
    ):
        print("running")
        data = self.extract_data(source_client={})
        transform_data = self.transform_data(data)
        self.load_data({}, destination_client={})
