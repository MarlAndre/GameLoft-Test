"""
Handles player profile retrieval, campaign fetching, and matching logic.  
"""

from campaign import get_mocked_campaigns
from player import get_mocked_player_profile

def find_player_campaign(player_id):
    """Retrieve the player's profile, match it with active campaigns, and update it if necessary."""

    try:
        player_profile = get_mocked_player_profile(player_id)
    except KeyError:
        raise ValueError(f"Player with ID {player_id} not found in the mock database.")
    
    campaigns = get_mocked_campaigns()

    for campaign in campaigns:
        if not campaign["enabled"]:
            continue

        matchers = campaign["matchers"]

        # check level
        if not (matchers["level"]['min']< player_profile['level']<=matchers["level"]['max']):
            continue

        # check country
        if "country" in matchers["has"] and player_profile["country"] not in matchers["has"]["country"]:
            continue

        # check required items
        if 'items' in matchers["has"]:
            has_required_items = any(item in player_profile["inventory"] for item in matchers["has"]['items'])
            if not has_required_items:
                continue

        # check forbidden items
        if 'items' in matchers["does_not_have"]:
            has_forbidden_items = any(item in player_profile["inventory"] for item in matchers["does_not_have"]['items'])
            if has_forbidden_items:
                continue

        # update players active campaign
        player_profile["active_campaigns"].append(campaign['name'])
    return player_profile