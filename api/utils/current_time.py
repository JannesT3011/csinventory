from datetime import datetime
from datetime import timedelta
def current() -> datetime:
    return str(datetime.utcnow()).split(".")[0]