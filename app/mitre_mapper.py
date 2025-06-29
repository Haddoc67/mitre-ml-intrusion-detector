# Created by KolbySec, 2025
__author__ = "KolbySec"

def map_to_mitre(label):
    mapping = {
        "neptune": {
            "id": "T1499",
            "technique": "Endpoint Denial of Service",
            "tactic": "Impact",
            "url": "https://attack.mitre.org/techniques/T1499/"
        },
        "satan": {
            "id": "T1046",
            "technique": "Network Service Scanning",
            "tactic": "Discovery",
            "url": "https://attack.mitre.org/techniques/T1046/"
        }
    }
    return mapping.get(label, {})
