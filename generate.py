#!/usr/bin/env python3

import json
from pathlib import Path

def generate_file(file, prefix = ""):
    with open(file) as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            if isinstance(value, list):
                value = " ".join(value)
            value = value.replace("'", "\\'")
            print(f"  {prefix.upper()}{key.upper()}: '{value}',")

def generate(version = "enduser"):
    generate_file(
        Path(__file__).parent / version / "french.json", prefix = "STRIPE_"
    )
    generate_file(
        Path(__file__).parent / version / "french-declines.json", prefix = "STRIPE_DECLINE_"
    )

if __name__ == "__main__":
    generate()
