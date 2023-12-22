import ast

from ariadne_codegen.plugins.base import Plugin
from graphql import OperationDefinitionNode, ExecutableDefinitionNode


class DocstringsPlugin(Plugin):
    def generate_client_method(
        self,
        method_def: ast.FunctionDef | ast.AsyncFunctionDef,
        operation_definition: OperationDefinitionNode,
    ) -> ast.FunctionDef | ast.AsyncFunctionDef:
        root_resolver_name = operation_definition.selection_set.selections[0].name.value
        root_resolver_info = self.schema.query_type.fields.get(
            root_resolver_name
        ) or self.schema.subscription_type.fields.get(root_resolver_name)
        if root_resolver_info and (docstring := root_resolver_info.description):
            method_def.body.insert(0, ast.Expr(value=ast.Str(docstring)))
        return method_def
