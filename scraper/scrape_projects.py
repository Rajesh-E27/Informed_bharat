import json
from db.redis_client import get_redis_connection
from scraper.utils import extract_pincode

# Sample data (in real app, scrape from websites)
sample_projects = [
    {
        "title": "Metro Line Construction Phase 2",
        "description": "Ongoing construction near MG Road, improving connectivity.",
        "location": "MG Road, Bengaluru - 560001"
    },
    {
        "title": "Flyover Work at Hebbal",
        "description": "Flyover being built to reduce traffic.",
        "location": "Hebbal Junction, Bengaluru - 560024"
    },
    {
        "title": "Smart Street Lights Installation",
        "description": "Replacing street lights with energy-efficient LEDs in Whitefield.",
        "location": "Whitefield, Bengaluru - 560066"
    }
]

def save_to_redis():
    r = get_redis_connection()
    for project in sample_projects:
        pincode = extract_pincode(project["location"])
        if pincode:
            key = f"projects:{pincode}"
            existing = r.get(key)
            projects = json.loads(existing) if existing else []
            projects.append(project)
            r.set(key, json.dumps(projects))
            print(f"Saved project to Redis under {key}")

if __name__ == "__main__":
    save_to_redis()