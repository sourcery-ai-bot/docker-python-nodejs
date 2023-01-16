import json


TRIGGER_SCHEDULED = "scheduled"


def job_with_name(job, name):
    return isinstance(job, dict) and name in job


def generate_matrix(new_or_updated: list, trigger: str):
    if not new_or_updated and trigger == TRIGGER_SCHEDULED:
        print("\n# Scheduled run with no new or updated versions. Doing nothing.")
        return

    print(f"::set-output name=matrix::{json.dumps(new_or_updated)}")
    print("\n# New or updated versions:")
    print("Nothing" if not new_or_updated else "\n".join(version["key"] for version in new_or_updated))
