# Configuring Application Specific Access to S3
## Preparation
This recipe requires some “prep work” which deploys resources that you’ll build the solution on. You will use the AWS CDK to deploy these resources 

### In the root of this chapter’s repo, cd to the “305-Configuring-Application-Specific-Access-to-S3/cdk-AWS-Cookbook-305” directory and follow the subsequent steps:
```
cd 305-Configuring-Application-Specific-Access-to-S3/cdk-AWS-Cookbook-305/
test -d .venv || python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cdk deploy
```

## Wait for the cdk deploy command to complete. 

### We created a helper.py script to let you easily create and export environment variables to make subsequent commands easier. Run the script, and copy the output to your terminal to export variables:

`python helper.py`

### Navigate up to the main directory for this recipe (out of the “cdk-AWS-Cookbook-305” directory)

`cd ..`



## Clean up 
### Delete the access points:
```
aws s3control delete-access-point \
    --account-id $AWS_ACCOUNT_ID \
    --name cookbook305-app-1

aws s3control delete-access-point \
    --account-id $AWS_ACCOUNT_ID \
    --name cookbook305-app-2
```

### Delete the file that you uploaded:

`aws s3 rm s3://$BUCKET_NAME/motd.txt`

### Go to the cdk-AWS-Cookbook-305 directory:

`cd cdk-AWS-Cookbook-305/`

### To clean up the environment variables, run the helper.py script in this recipe’s cdk- directory with the --unset flag, and copy the output to your terminal to export variables:

`python helper.py --unset`


### Use the AWS CDK to destroy the resources, deactivate your Python virtual environment, and go to the root of the chapter:

`cdk destroy && deactivate && rm -r .venv/ && cd ../..`
