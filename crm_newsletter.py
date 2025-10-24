import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")


contacts = [
    {"email": "alice@startup.com", "persona": "Founder"},
    {"email": "bob@designlab.com", "persona": "Creative Professional"},
    {"email": "carol@opsflow.com", "persona": "Operations Manager"}
]


newsletters = {
    "Founder": "🚀 This week’s blog on AI efficiency — how to boost ROI with automation.",
    "Creative Professional": "🎨 Explore AI tools that spark creativity and save time!",
    "Operations Manager": "⚙️ How AI improves workflow reliability and team coordination."
}


def sync_contacts():
    url = "https://api.hubapi.com/crm/v3/objects/contacts"
    headers = {"Authorization": f"Bearer {HUBSPOT_API_KEY}", "Content-Type": "application/json"}

    for contact in contacts:
        payload = {
            "properties": {
                "email": contact["email"],
                "persona": contact["persona"]
            }
        }
        response = requests.post(url, headers=headers, json=payload)
        print(f"Created/Updated contact: {contact['email']} - Status {response.status_code}")


def send_newsletters():
    print("\n=== Sending newsletters ===")
    for contact in contacts:
        persona = contact["persona"]
        message = newsletters.get(persona, "Default newsletter content")
        print(f"Sent to {contact['email']} ({persona}): {message[:50]}...")


def log_campaign():
    log_data = {
        "campaign_title": "AI in Creative Automation",
        "send_date": "2025-10-20",
        "recipients": [c["email"] for c in contacts]
    }
    with open("campaign_log.json", "w") as f:
        json.dump(log_data, f, indent=2)
    print("\n✅ Campaign logged successfully!")


if __name__ == "__main__":
    sync_contacts()
    send_newsletters()
    log_campaign()

