from pathlib import Path

from ariadne_codegen.config import get_config_dict
from ariadne_codegen.main import client


BASE_CONFIGS_PATH = Path("resources/ariadne_client_configs")


def run():
    for config in BASE_CONFIGS_PATH.glob("*.toml"):
        print(f"Processing {config}")
        config_dict = get_config_dict(config)
        client(config_dict)
