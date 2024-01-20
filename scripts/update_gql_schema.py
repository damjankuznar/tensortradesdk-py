import httpx


url = "https://graphql.api.apollographql.com/api/graphql"
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json",
}
json_data = {
    "operationName": "Studio__IntrospectionQuery",
    "variables": {"serviceId": "Tensor-Trade-API", "schemaTag": "current"},
    "extensions": {
        "persistedQuery": {
            "version": 1,
            "sha256Hash": "15a8d6ef9a8e696f1afda1fa917b6d374036fa13893a4286634041fbf2330e8f",
        }
    },
}


def run():
    response = httpx.post(url, headers=headers, json=json_data)
    with open("resources/schema.graphql", "w") as schema_file:
        schema_file.write(response.json()["data"]["service"]["schema"]["document"])
