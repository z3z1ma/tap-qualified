"""Infers schemas from a tap's output.

Usage:
    tap-<whatever> | python schema_inferrer.py
    tap-<whatever> | head -500 | python schema_inferrer.py
"""

import json
import sys

import genson

if __name__ == "__main__":
    schemas: dict[str, genson.Schema] = {}
    schema = genson.Schema()
    for line in sys.stdin:
        try:
            message = json.loads(line)
        except json.JSONDecodeError:
            continue
        if message["type"] == "SCHEMA":
            # Use the first schema message as a starting point
            # this will probably be fairly generic if we are using
            # a schema inferrer, something like {"type": "object"}
            schemas[message["stream"]] = genson.Schema(message["schema"])
        elif message["type"] == "RECORD":
            schemas[message["stream"]].add_object(message["record"])
    for stream, schema in schemas.items():
        print(stream)
        print(schema.to_json(indent=2))
        print()
