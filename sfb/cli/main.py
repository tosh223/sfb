"""
Entry point for the CLI
"""
import json

from sfb.entrypoint import EntryPoint


def cli():
    results = {"Succeeded": [], "Failed": []}
    ep = EntryPoint()
    for response in ep.execute():
        results[response['Status']].append(response['Result'])

    print(json.dumps(results, indent=2))
    exit(0)
