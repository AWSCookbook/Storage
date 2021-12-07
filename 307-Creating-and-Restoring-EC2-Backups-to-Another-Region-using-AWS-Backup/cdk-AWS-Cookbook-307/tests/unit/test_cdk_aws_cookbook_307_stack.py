import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_aws_cookbook_307.cdk_aws_cookbook_307_stack import CdkAwsCookbook307Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_aws_cookbook_307/cdk_aws_cookbook_307_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkAwsCookbook307Stack(app, "cdk-aws-cookbook-307")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
