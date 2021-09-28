#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_aws_cookbook_308.cdk_aws_cookbook_308_stack import CdkAwsCookbook308Stack


app = cdk.App()
CdkAwsCookbook308Stack(app, "cdk-aws-cookbook-308",)

app.synth()
