import pytest
from profile_matcher import find_player_campaign
# def get_mocked_player_profile(player_id):
#     return {
#         "player_id": player_id,
#         "level": 3,
#         "country": "CA",
#         "inventory": {"item_1": 1, "item_34": 3},
#         "active_campaigns": []
#     }
def test_process_player_profile():
    player_id = "97983be2-98b7-11e7-90cf-082e5f28d836"
    updated_profile = find_player_campaign(player_id)
    
    assert "active_campaigns" in updated_profile
    assert "mycampaign" in updated_profile["active_campaigns"]