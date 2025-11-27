import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

LOG_PATH = Path("logs/run_logs.json")

def log_event(step: str, payload: Dict[str, Any]) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    event = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "step": step,
        "payload": payload,
    }

    # Append as newline-delimited JSON
    if LOG_PATH.exists():
        with open(LOG_PATH, "a") as f:
            f.write(json.dumps(event) + "\n")
    else:
        with open(LOG_PATH, "w") as f:
            f.write(json.dumps(event) + "\n")
