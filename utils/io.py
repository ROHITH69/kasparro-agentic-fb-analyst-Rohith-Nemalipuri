import os
from pathlib import Path
from typing import Any, Dict

import pandas as pd
import yaml

def load_config(path: str = "config/config.yaml") -> Dict[str, Any]:
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config not found at {config_path}")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def load_data(config: Dict[str, Any]) -> pd.DataFrame:
    csv_env = os.getenv("DATA_CSV")
    if csv_env:
        csv_path = Path(csv_env)
    else:
        csv_path = Path(config["data"]["csv_path"])

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at {csv_path}")

    date_col = config["data"].get("date_column", "date")
    df = pd.read_csv(csv_path, parse_dates=[date_col])
    return df
