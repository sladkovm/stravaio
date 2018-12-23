import swagger_client
import os


class StravaIO():

    def __init__(self, access_token=None):

        if access_token is None:
            access_token = os.getenv('STRAVA_ACCESS_TOKEN')

        self.configuration = swagger_client.Configuration()
        self.configuration.access_token = access_token
