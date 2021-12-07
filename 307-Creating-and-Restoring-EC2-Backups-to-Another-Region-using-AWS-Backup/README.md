# Configuring Automated Backups with AWS Backup
## Preparation
This recipe requires some “prep work” which deploys resources that you’ll build the solution on. You will use the AWS CDK to deploy these resources. 

### In the root of this chapter’s repo, cd to the “307-Creating-and-Restoring-EC2-Backups-to-Another-Region-using-AWS-Backup/cdk-AWS-Cookbook-307” directory and follow the subsequent steps:
```
cd 307-Creating-and-Restoring-EC2-Backups-to-Another-Region-using-AWS-Backup/cdk-AWS-Cookbook-307/
test -d .venv || python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cdk deploy
```

### Wait for the cdk deploy command to complete. 

### We created a helper.py script (available in this Chapter’s repo) to let you easily create and export environment variables to make subsequent commands easier. Run the script, and copy the output to your terminal to export variables:

`python helper.py`


## Clean up 
###  Delete the recovery point in the backup vault within your destination region.

### Terminate the EC2 instance you restored in the destination region.

### Delete the recovery point in the backup vault within your source region.

### To clean up the environment variables, run the helper.py script in this recipe’s cdk- directory with the --unset flag, and copy the output to your terminal to export variables:

`python helper.py --unset`

### Unset the environment variable that you created manually:
```

```

### Use the AWS CDK to destroy the resources, deactivate your Python virtual environment, and go to the root of the chapter:

`cdk destroy && deactivate && rm -r .venv/ && cd ../..`
