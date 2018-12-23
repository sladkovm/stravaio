from stravaio import StravaIO
import maya
import json

client = StravaIO()

athlete = client.get_athlete()

athlete.to_dict()
