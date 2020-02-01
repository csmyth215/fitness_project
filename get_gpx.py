import requests
import json
import csv
from http.cookies import SimpleCookie

# view activity description: https://connect.garmin.com/modern/activity/ + activity_id

raw_cookie = ''

cookie = SimpleCookie()
cookie.load(raw_cookie)
cookies = {}
for key, morsel in cookie.items():
    cookies[key] = morsel.value

class Activity:

    def __init__(self, activity_id):
        self.activity_id = activity_id


    def get_activity_gpx(self):
        url = 'https://connect.garmin.com/modern/proxy/download-service/export/gpx/activity/' + str(self.activity_id)
        # headers = {'referer': 'https://connect.garmin.com/modern/activity/' + str(self.activity_id), 'authority': 'connect.garmin.com'}
        response = requests.get(url, cookies=cookies, headers=headers)
        if not response.ok:
            raise Exception("Could not retrieve activity %s: %s" % (self.activity_id, response.status_code))

    def get_activity_id_list():
        url = 'https://connect.garmin.com/modern/proxy/activitylist-service/activities/search/activities?limit=1&start=0'
        response = requests.get(url, cookies=cookies,)
        if not response.ok:
            raise Exception("Could not retrieve activity list: %s" % (response.status_code))
        return response


test_activity = Activity.get_activity_id_list()
activities_list = test_activity.json()
# activity_ids = []
# for activity in activities_list:
#     activity_ids.append(activity['activityId'])
# return(activity_ids)

print(activities_list)
