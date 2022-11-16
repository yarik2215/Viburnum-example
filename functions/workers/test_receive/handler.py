from viburnum.application import s3_handler, S3EventSequence, s3, S3Permission

@s3("test_bucket", S3Permission.full_access)
@s3_handler("test_bucket")
def test_receive(events: S3EventSequence, test_bucket):
    for e in events:
        print(e.object.key)
        test_bucket.delete_objects(
            Delete={
                'Objects': [
                    {
                        'Key': e.object.key,
                    },
                ],
            }
        )
