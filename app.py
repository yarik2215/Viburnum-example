
#!/usr/bin/env python3
import aws_cdk as cdk
from viburnum.deployer import AppStack
from viburnum.application import Application, Sqs, S3

# [Imports]
from functions.workers.test_receive.handler import test_receive
from functions.workers.test_worker.handler import test_worker
from functions.jobs.test_job.handler import test_job
from functions.api.hello.handler import hello

app = Application("AppTest")
# [Handlers]
app.add_handler(test_receive)
app.add_handler(test_worker)
app.add_handler(test_job)
app.add_handler(hello)
app.add_resource(Sqs("test_sqs"))
app.add_resource(S3("test_bucket"))


cdk_app = cdk.App()
AppStack(cdk_app, app
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

cdk_app.synth()
