import pandas as pd

def detect_anomaly(df_minute, thresholds=None):
    """
    Receives a DataFrame with transaction counts per status per minute.
    Returns a dictionary with alert flags.
    """
    if thresholds is None:
        thresholds = {
            'failed': 5,
            'denied': 3,
            'reversed': 4
        }

    alerts = {}
    for status in ['failed', 'denied', 'reversed']:
        count = df_minute.get(status, 0)
        if count > thresholds[status]:
            alerts[status] = 'alert'
        else:
            alerts[status] = 'ok'
    return alerts