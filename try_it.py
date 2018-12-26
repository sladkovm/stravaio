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
activity = client.get_activity_by_id(2033203247)
# pprint(activity.api_response.to_dict())
activity.store_locally()
# pprint(activity.to_dict())
