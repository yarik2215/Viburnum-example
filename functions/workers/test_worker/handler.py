
from viburnum.application import sqs_handler, SqsEventsSequence


@sqs_handler("test_sqs")
def test_worker(events: SqsEventsSequence):
    for e in events:
        print(e.message_id)
        print(e.body)
    e.delete()
