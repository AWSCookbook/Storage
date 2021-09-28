#!/usr/bin/env python3
import os


import aws_cdk as cdk

from cdk_aws_cookbook_309.cdk_aws_cookbook_309_stack import CdkAwsCookbook309Stack


app = cdk.App()
CdkAwsCookbook309Stack(app, "cdk-aws-cookbook-309")

app.synth()
