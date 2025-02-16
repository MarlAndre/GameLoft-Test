from typing import Dict, List, Any

def get_mocked_campaigns() -> List[Dict[str, Any]]:
    """
    Mock function to retrieve list of campaigns.
    Returns:
        List[Dict[str, Any]]: A list of active campaigns.
    """
    return [
        {
            "game": "mygame",
            "name": "mycampaign",
            "priority": 10.5,
            "matchers": {
                "level": {"min": 1, "max": 3},
                "has": {"country": ["US", "RO", "CA"], "items": ["item_1"]},
                "does_not_have": {"items": ["item_4"]}
            },
            "start_date": "2022-01-25 00:00:00Z",
            "end_date": "2022-02-25 00:00:00Z",
            "enabled": True,
            "last_updated": "2021-07-13 11:46:58Z"
        }
    ]