import ast
import re
from textwrap import dedent

from ariadne_codegen.plugins.base import Plugin
from graphql import OperationDefinitionNode


class DocstringsPlugin(Plugin):
    def generate_client_method(
        self,
        method_def: ast.FunctionDef | ast.AsyncFunctionDef,
        operation_definition: OperationDefinitionNode,
    ) -> ast.FunctionDef | ast.AsyncFunctionDef:
        docstring = self._extract_gql_query_docstring(
            operation_definition.name.value, operation_definition.loc.source.body
        ) or ""

        docstring += self._generate_arguments_docstring(method_def)
        docstring += "\n"
        method_def.body.insert(0, ast.Expr(value=ast.Str(docstring)))

        return method_def

    def _extract_gql_query_docstring(
        self, query_name: str, query_body: str
    ) -> str | None:
        pattern = re.compile(
            r"^(?:query|mutation) " + query_name + r"\s*\([^{]*{\s*$((?:\s*#.*$)+)(?!#)",
            flags=re.MULTILINE,
        )
        matches = pattern.search(query_body)
        if matches:
            comment = matches.group(1)
            comment = dedent(comment)
            comment = re.sub("^# ?", "", comment, flags=re.MULTILINE).strip()
            return f"\n{comment}\n"
        else:
            return None

    def _generate_arguments_docstring(self, method_def: ast.FunctionDef | ast.AsyncFunctionDef):
        args = []
        for arg in method_def.args.args:
            if arg.arg == 'self':
                continue
            args.append(arg.arg)
        output = ""
        if args:
            output += "Args:\n"
            output += "\n".join(f"    {arg}:" for arg in args)
        if output:
            output = f"\n{output}\n"
        return output