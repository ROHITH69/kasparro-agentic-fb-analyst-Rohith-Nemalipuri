import argparse
from .orchestrator import run_query

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Agentic Facebook Performance Analyst"
    )
    parser.add_argument("query", type=str, help="Marketer query in natural language")
    args = parser.parse_args()

    run_query(args.query)
    
if __name__ == "__main__":
    main()
