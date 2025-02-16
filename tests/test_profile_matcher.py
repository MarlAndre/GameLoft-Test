import pytest
from unittest.mock import patch

from profile_matcher import find_player_campaign
# def get_mocked_player_profile(player_id):
#     return {
#         "player_id": player_id,
#         "level": 3,
#         "country": "CA",
#         "inventory": {"item_1": 1, "item_34": 3},
#         "active_campaigns": []
#     }
def test_find_player_campaign_success():
    player_id = "97983be2-98b7-11e7-90cf-082e5f28d836"
    updated_profile = find_player_campaign(player_id)
    
    assert "active_campaigns" in updated_profile
    assert "mycampaign" in updated_profile["active_campaigns"]

def test_find_player_campaign_disabled_error():
    # Mock disabled campaign and player
    with patch('profile_matcher.get_mocked_player_profile') as mock_player, \
         patch('profile_matcher.get_mocked_campaigns') as mock_campaigns:

        mock_player.return_value = {
            "level": 2,
            "country": "CA",
            "inventory": {"item_1": 1},
            "active_campaigns": []
        }

        mock_campaigns.return_value = [{
            "name": "mycampaign",
            "enabled": False, 
            "matchers": {}
        }]
    
        player_id = "97983be2-98b7-11e7-90cf-082e5f28d836"
        updated_profile = find_player_campaign(player_id)

        assert "active_campaigns" in updated_profile
        assert len(updated_profile["active_campaigns"]) == 0

def test_find_player_campaign_level_error():
    with patch('profile_matcher.get_mocked_player_profile') as mock_player, \
         patch('profile_matcher.get_mocked_campaigns') as mock_campaigns:

        mock_player.return_value = {
            "level": 3,
            "country": "CA",
            "inventory": {"item_1": 1},
            "active_campaigns": []
        }

        mock_campaigns.return_value = [{
            "name": "mycampaign",
            "enabled": True, 
            "matchers": {
                "level": {"min": 1, "max": 2},
            }
        }]
    
        player_id = "97983be2-98b7-11e7-90cf-082e5f28d836"
        updated_profile = find_player_campaign(player_id)

        assert "active_campaigns" in updated_profile
        assert len(updated_profile["active_campaigns"]) == 0

def test_find_player_campaign_country_error():
    with patch('profile_matcher.get_mocked_player_profile') as mock_player, \
         patch('profile_matcher.get_mocked_campaigns') as mock_campaigns:

        mock_player.return_value = {
            "level": 3,
            "country": "FR",
            "inventory": {"item_1": 1},
            "active_campaigns": []
        }

        mock_campaigns.return_value = [{
            "name": "mycampaign",
            "enabled": True, 
            "matchers": {
                "level": {"min": 1, "max": 3},
                "has": {"country": ["US", "RO", "CA"]},
            }
        }]
    
        player_id = "97983be2-98b7-11e7-90cf-082e5f28d836"
        updated_profile = find_player_campaign(player_id)

        assert "active_campaigns" in updated_profile
        assert len(updated_profile["active_campaigns"]) == 0

def test_find_player_campaign_missing_item_error():
    with patch('profile_matcher.get_mocked_player_profile') as mock_player, \
         patch('profile_matcher.get_mocked_campaigns') as mock_campaigns:

        mock_player.return_value = {
            "level": 3,
            "country": "CA",
            "inventory": {"item_2": 1},
            "active_campaigns": []
        }

        mock_campaigns.return_value = [{
            "name": "mycampaign",
            "enabled": True, 
            "matchers": {
                "level": {"min": 1, "max": 3},
                "has": {"country": ["US", "RO", "CA"], "items": ["item_1"]},
                "does_not_have": {"items": ["item_4"]}
            }
        }]
    
        player_id = "97983be2-98b7-11e7-90cf-082e5f28d836"
        updated_profile = find_player_campaign(player_id)

        assert "active_campaigns" in updated_profile
        assert len(updated_profile["active_campaigns"]) == 0

def test_find_player_campaign_forbidden_item_error():
    with patch('profile_matcher.get_mocked_player_profile') as mock_player, \
         patch('profile_matcher.get_mocked_campaigns') as mock_campaigns:

        mock_player.return_value = {
            "level": 3,
            "country": "CA",
            "inventory": {"item_1": 1, "item_4": 2},
            "active_campaigns": []
        }

        mock_campaigns.return_value = [{
            "name": "mycampaign",
            "enabled": True, 
            "matchers": {
                "level": {"min": 1, "max": 3},
                "has": {"country": ["US", "RO", "CA"], "items": ["item_1"]},
                "does_not_have": {"items": ["item_4"]}
            }
        }]
    
        player_id = "97983be2-98b7-11e7-90cf-082e5f28d836"
        updated_profile = find_player_campaign(player_id)

        assert "active_campaigns" in updated_profile
        assert len(updated_profile["active_campaigns"]) == 0

def test_find_player_campaign_player_not_found_error():
    with patch('profile_matcher.get_mocked_player_profile', side_effect=KeyError):
        player_id = "nonexistent_id"
        
        with pytest.raises(ValueError, match=f"Player with ID {player_id} not found in the mock database."):
            find_player_campaign(player_id)