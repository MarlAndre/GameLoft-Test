from typing import Dict, Any

def get_mocked_player_profile(player_id: str) -> Dict[str, Any]:
    """
    Mock function to retrieve and return player's profile.
    Args:
        player_id (str): ID of the player.
    
    Returns:
        Dict[str, Any]: Player's profile data.
    """
    return {
        "player_id": player_id,
        "credential": "apple_credential",
        "created": "2021-01-10 13:37:17Z",
        "modified": "2021-01-23 13:37:17Z",
        "last_session": "2021-01-23 13:37:17Z",
        "total_spent": 400,
        "total_refund": 0,
        "total_transactions": 5,
        "last_purchase": "2021-01-22 13:37:17Z",
        "active_campaigns": [],
        "devices": [
            {
                "id": 1,
                "model": "apple iphone 11",
                "carrier": "vodafone",
                "firmware": "123"
            }
        ],
        "level": 3,
        "xp": 1000,
        "total_playtime": 144,
        "country": "CA",
        "language": "fr",
        "birthdate": "2000-01-10 13:37:17Z",
        "gender": "male",
        "inventory": {
            "cash": 123,
            "coins": 123,
            "item_1": 1,
            "item_34": 3,
            "item_55": 2
        },
        "clan": {
            "id": "123456",
            "name": "Hello world clan"
        },
        "_customfield": "mycustom"
    }
