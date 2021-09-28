# Replicating Data Between EFS and S3 with DataSync
## Preparation
This recipe requires some “prep work” which deploys resources that you’ll build the solution on. You will use the AWS CDK to deploy these resources 

### In the root of this chapter’s repo cd to the “309-Replicating-Data-Between-EFS-and-S3-with-DataSynccdk-AWS-Cookbook-309” directory and follow the subsequent steps:
```
cd 309-Replicating-Data-Between-EFS-and-S3-with-DataSync/cdk-AWS-Cookbook-309/
test -d .venv || python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cdk deploy
```

### Wait for the cdk deploy command to complete. 

### We created a helper.py script to let you easily create and export environment variables to make subsequent commands easier. Run the script, and copy the output to your terminal to export variables:

`python helper.py`

### Navigate up to the main directory for this recipe (out of the “cdk-AWS-Cookbook-309” directory):

`cd ..`


## Clean up 
### Delete the DataSync task:
```
aws datasync delete-task \
--task-arn $TASK_ARN
```

### Detach the AmazonS3ReadOnlyAccess policy from the role:
```
aws iam detach-role-policy --role-name AWSCookbookS3LocationRole \
--policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

### Delete the IAM Role:

`aws iam delete-role --role-name AWSCookbookS3LocationRole`

### Detach the AmazonElasticFileSystemClientReadWriteAccess policy from the role:
```
aws iam detach-role-policy --role-name AWSCookbookEFSLocationRole \
--policy-arn arn:aws:iam::aws:policy/AmazonElasticFileSystemClientFullAccess
```

### Delete the IAM Role:

`aws iam delete-role --role-name AWSCookbookEFSLocationRole`

### Go to the cdk-AWS-Cookbook-309 directory

`cd cdk-AWS-Cookbook-309/`

### To clean up the environment variables, run the helper.py script in this recipe’s cdk- directory with the --unset flag, and copy the output to your terminal to export variables:

`python helper.py --unset`

### Unset the environment variable that you created manually:
```
unset TASK_ARN
unset S3_LOCATION_ARN
unset EFS_LOCATION_ARN
unset S3_ROLE_ARN
unset EFS_ROLE_ARN
unset EFS_FILE_SYSTEM_ARN
unset SUBNET_ARN
unset SG_ARN
```

### Use the AWS CDK to destroy the resources, deactivate your Python virtual environment, and go to the root of the chapter:

`cdk destroy && deactivate && rm -r .venv/ && cd ../..`
