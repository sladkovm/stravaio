import swagger_client
from swagger_client.rest import ApiException
import maya
import os
import json
import datetime
import pandas as pd
import glob
import datetime
from loguru import logger
import requests
import urllib
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer


class StravaIO():

    def __init__(self, access_token=None):
        if access_token is None:
            access_token = os.getenv('STRAVA_ACCESS_TOKEN')
        self.configuration = swagger_client.Configuration()
        self.configuration.access_token = access_token
        self._api_client = swagger_client.ApiClient(self.configuration)
        self.athletes_api = swagger_client.AthletesApi(self._api_client)
        self.activities_api = swagger_client.ActivitiesApi(self._api_client)
        self.streams_api = swagger_client.StreamsApi(self._api_client)

    def get_logged_in_athlete(self):
        """Get logged in athlete
        
        Returns
        -------
        athlete: Athlete object
        """

        try:
            rv = Athlete(self.athletes_api.get_logged_in_athlete())
        except ApiException as e:
            logger.error(f""""
            Error in strava_swagger_client.AthletesApi! 
            STRAVA_ACCESS_TOKEN is likely out of date!
            Check the https://github.com/sladkovm/strava-oauth for help.
            Returning None.
            Original Error:
            {e}""")
            rv = None
        return rv 

    def local_athletes(self):
        """List local athletes
        
        Returns
        -------
        athletes: generator of JSON friendly dicts
        """
        for f_name in glob.glob(os.path.join(dir_stravadata(), 'athlete*.json')):
            with open(f_name) as f:
                yield json.load(f)


    def get_activity_by_id(self, id):
        """Get activity by ID
        
        Returns
        -------
        activity: Activity ojbect
        """
        return Activity(self.activities_api.get_activity_by_id(id))

    def get_logged_in_athlete_activities(self, after=0, list_activities=None):
        """List all activities after a given date
        
        Parameters
        ----------
        after: int, str or datetime object
            If integer, the time since epoch is assumed
            If str, the maya.parse() compatible date string is expected e.g. iso8601 or 2018-01-01 or 20180101
            If datetime, the datetime object is expected

        Returns
        -------
        list_activities: list
            List of SummaryActivity objects
        """
        
        list_activities = []
        after = date_to_epoch(after)
        _fetched = self.activities_api.get_logged_in_athlete_activities(after=after)
        if len(_fetched) > 0:
            print(f"Fetched {len(_fetched)}, the latests is on {_fetched[-1].start_date}")
            list_activities.extend(_fetched)
            if len(_fetched) == 30:
                last_after = list_activities[-1].start_date
                return self.get_logged_in_athlete_activities(after=last_after, list_activities=list_activities)
        else:
            print("empty list")
        
        return list_activities
        


    def local_activities(self, athlete_id):
        """List local activities
        
        Parameters
        ----------
        athlete_id: int

        Returns
        -------
        activities: generator of JSON friendly dicts
        """
        dir_activities = os.path.join(dir_stravadata(), f"activities_{athlete_id}")
        for f_name in glob.glob(os.path.join(dir_activities, '*.json')):
            with open(f_name) as f:
                yield json.load(f)


    def local_streams(self, athlete_id):
        """List local streams
        
        Parameters
        ----------
        athlete_id: int

        Returns
        -------
        streams: generator of dataframes
        """
        dir_streams = os.path.join(dir_stravadata(), f"streams_{athlete_id}")
        for f_name in glob.glob(os.path.join(dir_streams, '*.parquet')):
            yield pd.read_parquet(f_name)


    def get_activity_streams(self, id, athlete_id, local=True):
        """Get activity streams by ID
        
        Parameters
        ----------
        id: int
            activity_id
        athlete_id: int
            athlete_id
        local: bool (default=True)
            if the streams is already storred, return the local version

        Returns
        -------
        streams: Streams ojbect (remote) or pd.Dataframe (local)
        """
        if local:
            dir_streams = os.path.join(dir_stravadata(), f"streams_{athlete_id}")
            f_name = f"streams_{id}.parquet"
            f_path = os.path.join(dir_streams, f_name)
            if f_path in glob.glob(f_path):
                return pd.read_parquet(f_path)
        keys = ['time', 'distance', 'latlng', 'altitude', 'velocity_smooth',
        'heartrate', 'cadence', 'watts', 'temp', 'moving', 'grade_smooth']
        api_response = self.streams_api.get_activity_streams(id, keys, key_by_type=True)
        return Streams(api_response, id, athlete_id)


class Athlete():

    def __init__(self, api_response):
        """
        Parameters
        ----------
        api_response: swagger_client.get...() object
            e.g. athletes_api.get_logged_in_athlete()
        """
        self.api_response = api_response
        self.id = self.api_response.id

    def __str__(self):
        return self._stringify()

    def __repr__(self):
        return self._stringify()

    def to_dict(self):
        _dict = self.api_response.to_dict()
        _dict = convert_datetime_to_iso8601(_dict)
        return _dict

    def store_locally(self):
        strava_dir = dir_stravadata()
        f_name = f"athlete_{self.api_response.id}.json"
        with open(os.path.join(strava_dir, f_name), 'w') as fp:
            json.dump(self.to_dict(), fp)

    def _stringify(self):
        return json.dumps(self.to_dict(), indent=2)


class Activity():

    def __init__(self, api_response, client=None):
        self.api_response = api_response
        self.athlete_id = self.api_response.athlete.id
        self.id = self.api_response.id
        if client:
            self.streams_api = client.streams_api
        else:
            client = None

    def __repr__(self):
        return f"Activity: {self.id}, Date: {self.api_response.start_date}, Name: {self.api_response.name}"

    def to_dict(self):
        _dict = self.api_response.to_dict()
        _dict = convert_datetime_to_iso8601(_dict)
        return _dict

    def store_locally(self):
        strava_dir = dir_stravadata()
        athlete_id = self.api_response.athlete.id
        activities_dir = os.path.join(strava_dir, f"activities_{athlete_id}")
        if not os.path.exists(activities_dir):
            os.mkdir(activities_dir)
        f_name = f"activity_{self.api_response.id}.json"
        with open(os.path.join(activities_dir, f_name), 'w') as fp:
            json.dump(self.to_dict(), fp)


class Streams():

    ACCEPTED_KEYS = ['time', 'distance', 'altitude', 'velocity_smooth', 'heartrate', 'cadence', 'watts', 'temp', 'moving', 'grade_smooth', 'lat', 'lng']

    def __init__(self, api_response, activity_id, athlete_id):
        self.api_response = api_response
        self.activity_id = activity_id
        self.athlete_id = athlete_id

    def __repr__(self):
        return f"""Streams for {self.activity_id}\nKeys: {list(self.to_dict().keys())}\nAccess: obj.key or obj.to_dict() to load into a pd.DataFrame()"""

    def to_dict(self):
        _dict = self.api_response.to_dict()
        r = {}
        for k, v in _dict.items():
            if v is not None:
                r.update({k: v['data']})
        if r.get('latlng', None):
            latlng = r.pop('latlng')
            _r = list(zip(*latlng))
            r.update({'lat': list(_r[0])})
            r.update({'lng': list(_r[1])}) 
        return r

    def store_locally(self):
        _df = pd.DataFrame(self.to_dict())
        strava_dir = dir_stravadata()
        streams_dir = os.path.join(strava_dir, f"streams_{self.athlete_id}")
        if not os.path.exists(streams_dir):
            os.mkdir(streams_dir)
        f_name = f"streams_{self.activity_id}.parquet"
        _df.to_parquet(os.path.join(streams_dir, f_name))

    @property
    def time(self):
        return self._get_stream_by_name('time')

    @property
    def distance(self):
        return self._get_stream_by_name('distance')

    @property
    def altitude(self):
        return self._get_stream_by_name('altitude')

    @property
    def velocity_smooth(self):
        return self._get_stream_by_name('velocity_smooth')

    @property
    def heartrate(self):
        return self._get_stream_by_name('heartrate')

    @property
    def cadence(self):
        return self._get_stream_by_name('cadence')

    @property
    def watts(self):
        return self._get_stream_by_name('watts')

    @property
    def grade_smooth(self):
        return self._get_stream_by_name('grade_smooth')

    @property
    def moving(self):
        return self._get_stream_by_name('moving')
    
    @property
    def lat(self):
        return self._get_stream_by_name('lat')

    @property
    def lng(self):
        return self._get_stream_by_name('lng')


    def _get_stream_by_name(self, key):
        
        if key not in self.ACCEPTED_KEYS:
            raise KeyError(f"key must be one of {self.ACCEPTED_KEYS}")
        
        try:
            rv = self.to_dict()[key]
        except KeyError:
            logger.warning(f"Stream does not contain {key}")
            rv = None
        return rv


def strava_oauth2(client_id=None, client_secret=None):
    """Run strava authorization flow. This function will open a default system
    browser alongside starting a local webserver. The authorization procedure will be completed in the browser.

    The access token will be returned in the browser in the format ready to copy to the .env file.
    
    Parameters:
    -----------
    client_id: int, if not provided will be retrieved from the STRAVA_CLIENT_ID env viriable
    client_secret: str, if not provided will be retrieved from the STRAVA_CLIENT_SECRET env viriable
    """
    if client_id is None:
        client_id = os.getenv('STRAVA_CLIENT_ID', None)
        if client_id is None:
            raise ValueError('client_id is None')
    if client_secret is None:
        client_secret = os.getenv('STRAVA_CLIENT_SECRET', None)
        if client_secret is None:
            raise ValueError('client_secret is None')
    
    _request_strava_authorize(client_id)

    PORT = 8000

    with Server(("localhost", PORT), HTTPRequestHandler) as httpd:
        logger.info(f"serving at port {PORT}")
        httpd.serve_forever(client_id, client_secret)


def _request_strava_authorize(client_id):
    params_oauth = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": "http://localhost:8000/authorization_successful",
        "scope": "read,profile:read_all,activity:read",
        "state": 'https://github.com/sladkovm/strava-http',
        "approval_prompt": "force"
    }
    values_url = urllib.parse.urlencode(params_oauth)
    base_url = 'https://www.strava.com/oauth/authorize'
    rv = base_url + '?' + values_url
    webbrowser.get().open(rv)
    return None


class Server(HTTPServer):
    def serve_forever(self, client_id, client_secret):
        self.RequestHandlerClass.client_id = client_id
        self.RequestHandlerClass.client_secret = client_secret
        HTTPServer.serve_forever(self)


class HTTPRequestHandler(BaseHTTPRequestHandler):
    client_id = None
    client_secret = None

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        logger.debug(f"path: {url.path}")
        qs = urllib.parse.parse_qs(url.query)
        logger.debug(f"query strings: {qs}")

        if url.path == "/authorization_successful":
            code = qs.get('code')[0]
            logger.debug(f"code: {code}")
            params = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "code": code,
                "grant_type": "authorization_code"
            }
            r = requests.post("https://www.strava.com/oauth/token", params)
            d = json.loads(r.text)
            logger.debug(f"Authorized athlete: {d.get('access_token', 'Oeps something went wrong!')}")
            rv = f"STRAVA_ACCESS_TOKEN={d.get('access_token', 'Oeps something went wrong!')}".encode()
        else:
            rv = url.path.encode()

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(rv)


def convert_datetime_to_iso8601(d):
    for k, v in d.items():
        if isinstance(v, dict):
            convert_datetime_to_iso8601(v)
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    convert_datetime_to_iso8601(i)
        else:
            if isinstance(v, datetime.datetime):
                d[k] = maya.parse(v).iso8601()
    return d


def dir_stravadata():
    home_dir = os.path.expanduser('~')
    strava_dir = os.path.join(home_dir, '.stravadata')
    if not os.path.exists(strava_dir):
        os.mkdir(strava_dir)
    return strava_dir


def date_to_epoch(date):
    """Convert a date to epoch representation"""
    rv = None
    if isinstance(date, int):
        rv = date
    if isinstance(date, datetime.datetime):
        _ = maya.parse(date)
        rv = _.epoch
    if isinstance(date, str):
        _ = maya.when(date)
        rv = _.epoch
    if rv is None:
        raise TypeError('date must be epoch int, datetime obj or the string')
    return rv