import json
import os
from pathlib import Path

CI_EVENT_SCHEDULED = "scheduled"


def _github_action_set_output(key: str, value: str):
    """Write
    https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
    """
    with Path(os.getenv("GITHUB_OUTPUT")).open("a") as fp:
        fp.write(f"{key}={value}")


def generate_matrix(new_or_updated: list, ci_event: str):
    print("🔥", ci_event)
    if not new_or_updated and ci_event == CI_EVENT_SCHEDULED:
        print("\n# Scheduled run with no new or updated versions. Doing nothing.")
        return

    _github_action_set_output("MATRIX", json.dumps({"include": new_or_updated}))
    print("\n# New or updated versions:")
    print("Nothing" if not new_or_updated else "\n".join(version["key"] for version in new_or_updated))
