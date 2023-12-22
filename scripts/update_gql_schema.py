import json

import dotenv
import os
from graphql import get_introspection_query, build_client_schema, print_schema

from tensortradesdk.sync.base_client import BaseClient

dotenv.load_dotenv(".env")
api_key = os.environ["TENSOR_API_KEY"]


def run():
    client = BaseClient(api_key)
    query = get_introspection_query(descriptions=True)
    response = client.execute(query).json()
    if errors := response.get("errors"):
        raise RuntimeError(json.dumps(errors, indent="  "))

    client_schema = build_client_schema(response.get("data", None))
    sdl = print_schema(client_schema)
    with open("resources/schema.graphql", "w") as schema_file:
        schema_file.write(sdl)
