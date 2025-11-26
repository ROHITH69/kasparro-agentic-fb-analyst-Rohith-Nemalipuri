# requirements: Python 3.10+
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# sample run (uses sample data by default)
python src/run.py "Analyze ROAS drop"

# use config to switch to full data (see config/config.yaml)

