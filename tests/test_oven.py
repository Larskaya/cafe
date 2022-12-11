from app.Oven import Oven
from datetime import datetime
import time
import pytest


oven = Oven()


def get_remaining_time(seconds) -> int:
    start_time = datetime.now()
    for i in range(seconds):
        time.sleep(1)
    time_now = datetime.now()
    difference = time_now - start_time
    return difference.seconds


@pytest.mark.parametrize('seconds, expected', [(5, get_remaining_time(5)),
                                               (3, get_remaining_time(3))])
def test_timer(seconds, expected):
    assert seconds == expected

