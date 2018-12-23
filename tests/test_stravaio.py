from stravaio import StravaIO
import swagger_client
import pytest
import vcr
import os


@pytest.fixture
def client():
    yield StravaIO()


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

    def test_get_athlete(self, client):
        athlete = client.get_athlete()
        assert athlete is not None

    def test_get_activity_by_id(self, client):
        activity_id = 2029804583
        activity = client.get_activity_by_id(activity_id)
        assert activity is not None
