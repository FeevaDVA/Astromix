import requests
from pymeteosource.api import Meteosource as meteo
from pymeteosource.types import tiers, sections, langs, units

api_key = "28unp1tka59qnjy5uwey2ullitmn2p7etmay1c6d"
tier = tiers.FREE

source = meteo(api_key, tier)

forecast = source.get_point_forecast(
    place_id="Herndon",
    sections=[sections.DAILY, sections.HOURLY],
    lang=langs.ENGLISH,
    units=units.US
)

data = forecast.hourly.data
print(data[0])

for x in data:
    print(x["date"])
    print(x["cloud_cover"]["total"])
data = forecast.daily.data
print(data[0])
for x in data:
    print(x["day"])
    print(x["all_day"]["cloud_cover"]["total"])
