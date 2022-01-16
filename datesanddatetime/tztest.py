import pytz
import datetime

country = 'Asia/kuala_lumpur'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

for x in sorted(pytz.country_names):
    print("{}: {}:".format(x, pytz.country_names[x]), end=': ')