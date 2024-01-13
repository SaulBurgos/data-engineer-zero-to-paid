# description: this file contains a class called "file_client" that is used to write a list of a dictionary into a file

import json
import os
from donnes_pipe.connector_interfaces import ConnectClient


class FileClient(ConnectClient):
    def __init__(self, config: dict):
        self.config = config

    def connect(self):
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def write_file(self, filename: str, extension: str, data: list[dict]):
        folder_path = os.path.dirname(filename)
        os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

        with open(f"{filename}.{extension}", "w") as file:
            file.write(json.dumps(data, indent=4))
