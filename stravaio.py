import swagger_client
import maya
import os
import json
import datetime


class StravaIO():

    def __init__(self, access_token=None):
        if access_token is None:
            access_token = os.getenv('STRAVA_ACCESS_TOKEN')
        self.configuration = swagger_client.Configuration()
        self.configuration.access_token = access_token
        self._api_client = swagger_client.ApiClient(self.configuration)
        self.athletes_api = swagger_client.AthletesApi(self._api_client)
        self.activities_api = swagger_client.ActivitiesApi(self._api_client)

    def get_athlete(self):
        """Get logged in athlete"""
        athlete = Athlete(self.athletes_api.get_logged_in_athlete())
        return athlete

    def get_activity_by_id(self, id):
        """Get activity by ID"""
        return self.activities_api.get_activity_by_id(id)


class Athlete():

    def __init__(self, api_response):
        self.api_response = api_response

    def to_dict(self):
        _dict = self.api_response.to_dict()
        _dict['created_at'] = maya.parse(self.api_response.created_at).iso8601()
        _dict['updated_at'] = maya.parse(self.api_response.updated_at).iso8601()
        return _dict

    def store_locally(self):
        home_dir = os.path.expanduser('~')
        strava_dir = os.path.join(home_dir, '.stravadata')
        if not os.path.exists(strava_dir):
            os.mkdir(strava_dir)
        f_name = f"activity_{self.api_response.id}.json"
        with open(os.path.join(strava_dir, f_name), 'w') as fp:
            json.dump(self.to_dict(), fp)


def convert_datetime_to_iso8601(d):
    for k, v in d.items():
        if isinstance(v, dict):
            convert_datetime_to_iso8601(v)
        else:
            if isinstance(v, datetime.datetime):
                d[k] = maya.parse(v).iso8601()
    return d


class Activity():

    def __init__(self, api_response):
        self.api_response = api_response

    def to_dict(self):
        _dict = self.api_response.to_dict()