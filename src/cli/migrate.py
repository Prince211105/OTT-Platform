"""Alembic migration runner for the OTT Platform schema.
This script assumes an Alembic environment is configured under `src/migrations`.
It can be invoked via:
    python -m src.cli.migrate
"""

import os
import subprocess
import sys

def main():
    # Determine the absolute path to the Alembic config file
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    alembic_cfg = os.path.join(os.path.dirname(base_dir), "alembic.ini")
    if not os.path.isfile(alembic_cfg):
        print("Alembic configuration not found at:", alembic_cfg)
        sys.exit(1)
    # Run alembic upgrade head using python -m for Windows compatibility
    cmd = [sys.executable, "-m", "alembic", "-c", alembic_cfg, "upgrade", "head"]
    subprocess.check_call(cmd)

if __name__ == "__main__":
    main()
