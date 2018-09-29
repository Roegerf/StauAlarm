import json;
import requests;
import time;

url = "https://route.api.here.com/routing/7.2/calculateroute.json?waypoint0=52.5160%2C13.3779&waypoint1=52.5206%2C13.3862&mode=fastest%3Bcar%3Btraffic%3Aenabled&app_id=jX2LqfxDfkxYLGKu96j3&app_code=qJMYXQcewVPT2GN8uk7UoA&departure=now";
response=requests.get(url);
jData = json.loads(response.content);
print(jData["response"]["route"][0]["summary"]["travelTime"]);
time.sleep(120);
print(jData["response"]["route"][0]["summary"]["travelTime"]);
