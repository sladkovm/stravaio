from stravaio import StravaIO, convert_datetime_to_iso8601
import swagger_client
import pytest
import vcr
import os
import maya


class TestStravaIO():

    def test_init_stravaio(self):
        client = StravaIO(access_token='very_secret_token')
        assert client.configuration.access_token == 'very_secret_token'
        assert isinstance(client.athletes_api, swagger_client.AthletesApi)
        assert isinstance(client.activities_api, swagger_client.ActivitiesApi)

    def test_init_stravaio_env(self):
        client = StravaIO()
        access_token = os.getenv('STRAVA_ACCESS_TOKEN', None)
        assert client.configuration.access_token == access_token

    @pytest.mark.skip("Skip testing calls to Strava API")
    def test_get_athlete(self, client):
        athlete = client.get_athlete()
        assert athlete is not None

    @pytest.mark.skip("Skip testing calls to Strava API")
    def test_get_activity_by_id(self, client):
        activity_id = 2029804583
        activity = client.get_activity_by_id(activity_id)
        assert activity is not None


def test_convert_datetime_to_iso8601():
    _d = {
        'key1': {
            'key11': {
                'key21': maya.parse('2018-02-01').datetime()
                },
            'key12': maya.parse('2018-01-02').datetime()
            }
        }
    
    res = {
        'key1': 
            {
            'key11': {
                'key21': '2018-02-01T00:00:00Z'
                },
            'key12': '2018-01-02T00:00:00Z'
            }
        }

    assert convert_datetime_to_iso8601(_d) == res