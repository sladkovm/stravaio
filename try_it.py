from stravaio import StravaIO
import maya
import json
from pprint import pprint

client = StravaIO()

# ## Athlete
# athlete = client.get_athlete()
# athlete.store_locally()
# pprint(athlete.to_dict())

## Activity
# activity = client.get_activity_by_id(2033203247)
# activity.store_locally()
list_activities = client.get_logged_in_athlete_activities(after='20180101')
pprint(len(list_activities))



## Streams
# streams = client.get_activity_streams(2033203247)
# pprint(streams.athlete_id)
# pprint(streams.activity_id)
# streams.store_locally()
