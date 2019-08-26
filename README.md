# stravaio
Python client for Strava API with a focus on fluent data handling

[![PyPI version](https://badge.fury.io/py/stravaio.svg)](https://badge.fury.io/py/stravaio)
[![Build Status](https://travis-ci.org/sladkovm/stravaio.svg?branch=master)](https://travis-ci.org/sladkovm/stravaio)

## Example

Build your own *Year in Strava* poster [Jupyter notebook](https://github.com/sladkovm/stravaio/blob/master/examples/Year%20in%20Strava%202018.ipynb)

## Install
```bash
pipenv install stravaio
```

or

```bash
pip install stravaio
```

Latest dev version could be installed as:
```bash
pipenv install git+https://github.com/sladkovm/stravaio.git#egg=stravaio
```

## Before use
You need `STRAVA_ACCESS_TOKEN` with activity level permissions to make use of this package. 

The easiest way to get the token is to use the *stravaio* library itself:

```python
from stravaio import strava_oauth2

strava_oauth2(client_id=STRAVA_CLIENT_ID, client_secret=STRAVA_CLIENT_SECRET)
```

You will be redirected to the default system browser, where the authorization flow must be completed. In the background the local webserver will be running and listening to the data returned by Strava.

Both `STRAVA_CLIENT_ID` and `STRAVA_CLIENT_SECRET` are optional arguments if they are set as the environment variables.

Another way is to head to the [strava-oauth](https://github.com/sladkovm/strava-oauth) library for help. There you will find a link to the public webserver that can be used for completing the Strava authorizatio flow.

When the token is fetched it is handy to store it as an environment variable. Otherwise it should be passed explicitely to the StravaIO constructor.

```bash
export STRAVA_ACCESS_TOKEN=<strava_access_token>
```

## Use

```python
from stravaio import StravaIO

# If the token is stored as an environment varible it is not neccessary
# to pass it as an input parameters
client = StravaIO(access_token=STRAVA_ACCESS_TOKEN)
```

### Athlete
```python
# Get logged in athlete (e.g. the owner of the token)
# Returns a stravaio.Athlete object that wraps the
# [Strava DetailedAthlete](https://developers.strava.com/docs/reference/#api-models-DetailedAthlete)
# with few added data-handling methods
athlete = client.get_logged_in_athlete()

# Dump athlete into a JSON friendly dict (e.g. all datetimes are converted into iso8601)
athlete_dict = athlete.to_dict()

# Store athlete infor as a JSON locally (~/.stravadata/athlete_<id>.json)
athlete.store_locally()

# Get locally stored athletes (returns a generator of dicts)
local_athletes = client.local_athletes()
```



### Activities
```python
# Returns a stravaio.Activity object that wraps the 
# [Strava DetailedActivity](https://developers.strava.com/docs/reference/#api-models-DetailedActivity)
activity = client.get_activity_by_id(2033203247)

# Dump activity into a JSON friendly dict
activity_dict = activity.to_dict()

# Store activity locally (~/.stravadata/activities_<athlete_id>/activity_<id>.json)
activity.store_locally()

# Get list of athletes activities since a given date (after) given in a human friendly format.
# Kudos to [Maya: Datetimes for Humans(TM)](https://github.com/kennethreitz/maya)
# Returns a list of [Strava SummaryActivity](https://developers.strava.com/docs/reference/#api-models-SummaryActivity) objects
list_activities = client.get_logged_in_athlete_activities(after='last week')

# Obvious use - store all activities locally
for a in list_activities:
    activity = client.get_activity_by_id(a.id)
    activity.store_locally()

# List local activities (returns a generator of JSON friendly dicts)
activities = client.local_activities(athlete_id=1202065)
```

### Streams
```python
# Returns a stravaio.Streams object that wraps the 
# [Strava StreamSet](https://developers.strava.com/docs/reference/#api-models-StreamSet)
streams = client.get_activity_streams(2033203247)

# Access streams using the dot notation
watts = streams.watts

# Dump streams into a JSON friendly dict
streams_dict = streams.to_dict()

# Store streams locally (~/.stravadata/streams_<athlete_id>/streams_<id>.parquet) as a .parquet file, that can be loaded later using the
# pandas.read_parquet()
streams.store_locally()

```

## Contributors

[Aart Goossens](https://github.com/AartGoossens)
