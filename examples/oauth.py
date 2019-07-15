from stravaio import strava_oauth2
import os
import dotenv
dotenv.load_dotenv()

token = strava_oauth2()

print(token)