# stravaio
Python client for Strava API with a focus on fluent data handling

## Install
```bash
git clone https://github.com/sladkovm/stravaio.git
```

## Before use
You need `STRAVA_ACCESS_TOKEN` with activity level permissions to make use of this package. Head to the [strava-oauth](https://github.com/sladkovm/strava-oauth) library for help.

When the token is fetched it is handy to store it as a environment variable

```bash
export STRAVA_ACCESS_TOKEN=<strava_access_token>
```

## Use

```python
from stravaio import StravaIO

# If the token is stored as an environment varible it is not neccessary
# to pass it as an input parameters
client = StravaIO(access_token=STRAVA_ACCESS_TOKEN)

# Get logged in athlete (e.g. the owner of the token)
# Returns a stravaio.Athlete object that wraps the
# [Strava DetailedAthlete](https://developers.strava.com/docs/reference/#api-models-DetailedAthlete)
# with few added data-handling methods
athlete = client.get_logged_in_athlete()

# Dump athlete into a JSON friendly dict (e.g. all datetimes are converted into iso8601)
athlete_dict = athlete.to_dict()

# Store athlete infor as a JSON locally (~/.stravadata/athlete_<id>.json)
athlete.store_locally()
```
