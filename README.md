

## Development

### Update GraphQL schema
Download the schema from: 
https://studio.apollographql.com/public/Tensor-Trade-API/variant/current/schema/sdl

> Currently not allowed to introspect schema so unable to automate the following.

To update the schema from Tensor.trade GraphQL API run the following command:
```bash
poetry run update_gql_schema
```

This currenlty errors with:
```json
{
  "errors": [
    {
      "message": "GraphQL introspection is not allowed by Apollo Server, but the query contained __schema or __type. To enable introspection, pass introspection: true to ApolloServer in production",
      "extensions": {
        "code": "GRAPHQL_VALIDATION_FAILED"
      }
    }
  ]
}
```


### Autogenerate clients
To autogenerate clients from GrapgQL queries run the following command:
```bash
poetry run generate_gql_clients
```

