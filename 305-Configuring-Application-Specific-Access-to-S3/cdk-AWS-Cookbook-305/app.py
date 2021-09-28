#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_aws_cookbook_305.cdk_aws_cookbook_305_stack import CdkAwsCookbook305Stack


app = cdk.App()
CdkAwsCookbook305Stack(app, "cdk-aws-cookbook-305",
    )

app.synth()
