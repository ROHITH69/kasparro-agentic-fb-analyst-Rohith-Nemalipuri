# src/run.py
import argparse
import yaml
import random
import os
from orchestrator import Orchestrator

def load_config(path="config/config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="Natural language command (e.g. 'Analyze ROAS drop')")
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()

    cfg = load_config(args.config)
    random.seed(cfg.get("random_seed", 42))

    orchestrator = Orchestrator(cfg)
    orchestrator.run(args.query)

if __name__ == "__main__":
    main()

