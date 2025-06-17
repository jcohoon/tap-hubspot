import unittest
import datetime
from unittest.mock import patch
import tap_hubspot

class TestAuthMethod(unittest.TestCase):
    def test_pat_headers(self):
        tap_hubspot.CONFIG.update({
            "auth_method": "pat",
            "access_token": "pat-123",
            "hapikey": None,
        })
        params, headers = tap_hubspot.get_params_and_headers({})
        self.assertEqual(headers.get("Authorization"), "Bearer pat-123")

    @patch('tap_hubspot.acquire_access_token_from_refresh_token')
    def test_oauth_header_refresh(self, mock_refresh):
        def _set_token():
            tap_hubspot.CONFIG['access_token'] = 'newtoken'
            tap_hubspot.CONFIG['token_expires'] = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        mock_refresh.side_effect = _set_token
        tap_hubspot.CONFIG.update({
            "auth_method": "oauth",
            "access_token": "old",
            "token_expires": datetime.datetime.utcnow() - datetime.timedelta(seconds=1),
            "hapikey": None,
        })
        params, headers = tap_hubspot.get_params_and_headers({})
        mock_refresh.assert_called_once()
        self.assertEqual(headers.get("Authorization"), f"Bearer {tap_hubspot.CONFIG['access_token']}")


