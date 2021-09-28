#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_aws_cookbook_310.cdk_aws_cookbook_310_stack import CdkAwsCookbook310Stack


app = cdk.App()
CdkAwsCookbook310Stack(app, "cdk-aws-cookbook-310"),

app.synth()
