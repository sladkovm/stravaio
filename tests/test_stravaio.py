from stravaio import StravaIO
import os


class TestStravaIO():

    def test_init_stravaio(self):

        client = StravaIO(access_token='very_secret_token')
        assert client.configuration.access_token == 'very_secret_token'

    def test_init_stravaio_env(self):
        os.environ['STRAVA_ACCESS_TOKEN'] = 'env_secret_token'
        client = StravaIO()
        assert client.configuration.access_token == 'env_secret_token'

    def test_init_stravaio_env_none(self):
        os.environ.pop('STRAVA_ACCESS_TOKEN', None)
        client = StravaIO()
        assert client.configuration.access_token is None
