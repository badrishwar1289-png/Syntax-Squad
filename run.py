#!/usr/bin/env python3
"""Run the EchoMind backend from repository root.

This script forwards execution to `server/run.py` so you can run
`python run.py` from the workspace root (A:\\EchoMind).

It uses runpy.run_path to execute the server script as __main__.
"""
import os
import runpy

ROOT = os.path.dirname(__file__)
SERVER_RUN = os.path.join(ROOT, 'server', 'run.py')

if __name__ == '__main__':
    if not os.path.exists(SERVER_RUN):
        raise FileNotFoundError(f"Server run script not found: {SERVER_RUN}")
    # Execute the server runner as if it were run directly
    runpy.run_path(SERVER_RUN, run_name='__main__')
