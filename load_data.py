import json
from db.redis_client import get_redis_connection

def load_sample_projects_to_redis(file_path):
    redis_conn = get_redis_connection()
    with open(file_path, "r", encoding="utf-8") as f:
        projects = json.load(f)

    # Group projects by pincode
    projects_by_pincode = {}
    for project in projects:
        pincode = project.get("pincode")
        if pincode:
            projects_by_pincode.setdefault(pincode, []).append(project)

    # Save grouped projects to Redis as JSON strings
    for pincode, projects_list in projects_by_pincode.items():
        key = f"projects:{pincode}"
        redis_conn.set(key, json.dumps(projects_list))
        print(f"Saved {len(projects_list)} projects under key {key}")

if __name__ == "__main__":
    load_sample_projects_to_redis("data/sample_output.json")
