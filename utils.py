from datetime import datetime, timedelta


def get_delivery_date():
    return (
        datetime.now() + timedelta(days=1)
    ).strftime("%d.%m.%Y")