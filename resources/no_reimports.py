# Copied from https://github.com/mirumee/ariadne-codegen/blob/main/ariadne_codegen/contrib/no_reimports.py since it's
# not yet available in the latest release. Remove when available.

import ast

from ariadne_codegen.plugins.base import Plugin


class NoReimportsPlugin(Plugin):
    def generate_init_module(self, module: ast.Module) -> ast.Module:
        module.body = []
        return module
