from stravaio import StravaIO, convert_datetime_to_iso8601, date_to_epoch
from stravaio import strava_oauth2
import swagger_client
import pytest
import os
import maya
import datetime


class TestStravaIO():

    def test_init_stravaio(self):
        client = StravaIO(access_token='very_secret_token')
        assert client.configuration.access_token == 'very_secret_token'
        assert isinstance(client._api_client, swagger_client.ApiClient)
        assert isinstance(client.athletes_api, swagger_client.AthletesApi)
        assert isinstance(client.activities_api, swagger_client.ActivitiesApi)
        assert isinstance(client.streams_api, swagger_client.StreamsApi)

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


def test_date_to_epoch_int():
    assert date_to_epoch(1) == 1


def test_date_to_epoch_date_str():
    assert date_to_epoch('2018-01-01') == 1514764800


def test_date_to_epoch_slang_date():
    assert isinstance(date_to_epoch('last week'), int)


def test_date_to_epoch_datetime():
    assert isinstance(date_to_epoch(datetime.datetime(2019, 1, 1)), int)


def test_convert_datetime_to_iso8601():
    _d = {
        'key1': {
            'key11': {
                'key21': maya.parse('2018-02-01').datetime()
                },
            'key12': maya.parse('2018-01-02').datetime()
            },
        'key2': [
            {'key111': maya.parse('2018-01-03').datetime()},
            {'key112': maya.parse('2018-01-04').datetime()}
        ]}
    res = {
        'key1': 
            {
            'key11': {
                'key21': '2018-02-01T00:00:00Z'
                },
            'key12': '2018-01-02T00:00:00Z'
            },
        'key2': [
            {'key111': '2018-01-03T00:00:00Z'},
            {'key112': '2018-01-04T00:00:00Z'}
        ]}
    assert convert_datetime_to_iso8601(_d) == res