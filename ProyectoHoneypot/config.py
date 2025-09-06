import yaml 
from pathlib import Path

def load_config(path="config.yml"):
    config_file = Path(path)
    if not config_file.exists():
        raise FileNotFoundError(f"config file {path} not found")


    with open(config_file,"r") as f:
        return yaml.safe_load(f)
