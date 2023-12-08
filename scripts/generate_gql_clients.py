from pathlib import Path

from ariadne_codegen.config import get_config_dict
from ariadne_codegen import main


BASE_CONFIGS_PATH = Path("resources/ariadne_client_configs")
EXCEPTIONS_PATH = str(Path(main.__file__).parent / "client_generators" / "dependencies" / "exceptions.py")

def run():

    for config in BASE_CONFIGS_PATH.glob("*.toml"):
        print(f"Processing {config}")
        config_dict = get_config_dict(str(config))
        files_to_include = config_dict["tool"]["ariadne-codegen"].get("files_to_include", [])
        files_to_include.append(EXCEPTIONS_PATH)
        config_dict["tool"]["ariadne-codegen"]["files_to_include"] = files_to_include
        main.client(config_dict)
