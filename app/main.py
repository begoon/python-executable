import json
from typing import Dict
import requests

import docker

print(requests.get("https://google.com"))

client = docker.from_env()


def fields(container: docker.models.containers.Container) -> Dict[str, str]:
    names = ["short_id", "name", "status"]
    return {name: getattr(container, name) for name in names}


containers = [
    fields(container) for container in client.containers.list(all=True)
]

print(json.dumps(containers, indent=2))
