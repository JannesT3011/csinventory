from datetime import datetime
from datetime import timedelta
def current() -> datetime:
    return str(datetime.utcnow()).split(".")[0]

def check_delta():
    #print(datetime.now())
    #print(datetime.utcnow())
    delta = datetime.strptime(current(), "%Y-%m-%d %H:%M:%S") - datetime.strptime("2020-06-19 08:31:44", "%Y-%m-%d %H:%M:%S")
    print(type(str(delta)))
    if "day," in str(delta).split(" "):
        print(True)
    print(str(delta).split(" "))

check_delta()