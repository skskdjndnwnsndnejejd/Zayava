
from datetime import datetime, timedelta

cooldowns = {}

def check_cd(user_id, hours=24):
    now = datetime.utcnow()
    if user_id not in cooldowns:
        cooldowns[user_id] = now
        return True
    if now - cooldowns[user_id] >= timedelta(hours=hours):
        cooldowns[user_id] = now
        return True
    return False

def remaining(user_id, hours=24):
    now = datetime.utcnow()
    if user_id not in cooldowns:
        return 0
    diff = timedelta(hours=hours) - (now - cooldowns[user_id])
    return int(diff.total_seconds())
