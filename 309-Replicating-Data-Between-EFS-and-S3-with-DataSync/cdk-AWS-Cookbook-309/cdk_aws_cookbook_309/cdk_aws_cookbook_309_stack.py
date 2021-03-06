from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_efs,
    aws_s3_deployment,
    aws_iam as iam,
    Stack,
    CfnOutput,
    RemovalPolicy,
    Aws
)


class CdkAwsCookbook309Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create s3 bucket
        s3_Bucket = s3.Bucket(
            self,
            "AWS-Cookbook-Recipe-309",
            removal_policy=RemovalPolicy.DESTROY
        )

        aws_s3_deployment.BucketDeployment(
            self,
            'S3Deployment',
            destination_bucket=s3_Bucket,
            sources=[aws_s3_deployment.Source.asset("./s3_content")],
            retain_on_delete=False
        )

        isolated_subnets = ec2.SubnetConfiguration(
            name="ISOLATED",
            subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
            cidr_mask=24
        )

        # create VPC
        vpc = ec2.Vpc(
            self,
            'AWS-Cookbook-VPC-309',
            cidr='10.10.0.0/23',
            subnet_configuration=[isolated_subnets]
        )

        efs_fs = aws_efs.FileSystem(
            self,
            'EFS Filesystem',
            vpc=vpc,
            file_system_name='AWSCookbook309'
        )

        vpc.add_gateway_endpoint(
            's3GateWayEndPoint',
            service=ec2.GatewayVpcEndpointAwsService('s3'),
            subnets=[ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)],
        )

        # -------- Begin EC2 Helper ---------
        vpc.add_interface_endpoint(
            'VPCSSMInterfaceEndpoint',
            service=ec2.InterfaceVpcEndpointAwsService('ssm'),  # Find names with - aws ec2 describe-vpc-endpoint-services | jq '.ServiceNames'
            private_dns_enabled=True,
            subnets=ec2.SubnetSelection(
                one_per_az=False,
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
        )

        vpc.add_interface_endpoint(
            'VPCEC2MessagesInterfaceEndpoint',
            service=ec2.InterfaceVpcEndpointAwsService('ec2messages'),  # Find names with - aws ec2 describe-vpc-endpoint-services | jq '.ServiceNames'
            private_dns_enabled=True,
            subnets=ec2.SubnetSelection(
                one_per_az=False,
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
        )

        vpc.add_interface_endpoint(
            'VPCSSMMessagesInterfaceEndpoint',
            service=ec2.InterfaceVpcEndpointAwsService('ssmmessages'),  # Find names with - aws ec2 describe-vpc-endpoint-services | jq '.ServiceNames'
            private_dns_enabled=True,
            subnets=ec2.SubnetSelection(
                one_per_az=False,
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
        )

        ami = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )
        user_data = ec2.UserData.for_linux()
        user_data.add_commands(
            'sudo yum -y install amazon-efs-utils',
            'sudo mkdir /mnt/efs',
            'sleep 90',
            'sudo mount -t efs -o iam,tls ' + efs_fs.file_system_id + ' /mnt/efs',
        )

        iam_role = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))

        iam_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"))

        instance = ec2.Instance(
            self,
            "Instance",
            instance_type=ec2.InstanceType("t3.nano"),
            machine_image=ami,
            user_data=user_data,
            role=iam_role,
            vpc=vpc,
        )

        # allow connection from ec2 instance to the file_system SG
        efs_fs.connections.allow_from(
            instance.connections, ec2.Port.tcp(2049), "Ingress")

        CfnOutput(
            self,
            'InstanceId',
            value=instance.instance_id
        )
        # -------- End EC2 Helper ---------

        # outputs

        CfnOutput(
            self,
            'EfsId',
            value=efs_fs.file_system_id
        )

        CfnOutput(
            self,
            'BucketArn',
            value=s3_Bucket.bucket_arn
        )

        CfnOutput(
            self,
            'EfsSg',
            value=instance.connections.security_groups[0].security_group_id
        )

        isolated_subnets = vpc.select_subnets(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)

        CfnOutput(
            self,
            'IsolatedSubnet1',
            value=isolated_subnets.subnets[0].subnet_id
        )