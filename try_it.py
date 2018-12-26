from stravaio import StravaIO
import maya
import json
from pprint import pprint

client = StravaIO()

# Athlete
# athlete = client.get_athlete()
# athlete.store_locally()
# print(athlete.to_dict())

# Activity
activity = client.get_activity_by_id(2033203247)

pprint(activity.to_dict())
