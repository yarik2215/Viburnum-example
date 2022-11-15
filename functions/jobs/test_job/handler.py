
from viburnum.application import JobEvent, job


@job("rate(1 hour)")
def test_job(event: JobEvent):
    print("Hello world")
