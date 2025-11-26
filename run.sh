#!/usr/bin/env bash
set -e

if [ -z "$1" ]; then
  echo "Usage: ./run.sh \"Analyze ROAS drop in last 14 days\""
  exit 1
fi

QUERY="$1"

if [ -z "$DATA_CSV" ]; then
  export DATA_CSV="data/synthetic_fb_ads_undergarments.csv"
fi

python src/run.py "$QUERY"
