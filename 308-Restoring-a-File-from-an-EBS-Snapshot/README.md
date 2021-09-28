# Restoring a File from an EBS Snapshot
## Preparation
This recipe requires some “prep work” which deploys resources that you’ll build the solution on. You will use the AWS CDK to deploy these resources 

### In the root of this chapter’s repo cd to the “308-Restoring-a-File-from-an-EBS-Snapshot/cdk-AWS-Cookbook-308” directory and follow the subsequent steps:
```
cd 308-Restoring-a-File-from-an-EBS-Snapshot/cdk-AWS-Cookbook-308/
test -d .venv || python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cdk deploy
```

### Wait for the cdk deploy command to complete. 

### We created a helper.py script to let you easily create and export environment variables to make subsequent commands easier. Run the script, and copy the output to your terminal to export variables:

`python helper.py`



## Clean up 
### Delete the snapshot:

`aws ec2 delete-snapshot --snapshot-id $SNAPSHOT_ID`

### Unattach the EBS volume that you created:

`aws ec2 detach-volume --volume-id $SNAP_VOLUME_ID`

### Delete the EBS volume that you created:

`aws ec2 delete-volume --volume-id $SNAP_VOLUME_ID`

### Unset the environment variables that you created manually:
```
unset SNAP_VOLUME_ID
unset ORIG_VOLUME_ID
unset SNAPSHOT_ID
```

### Use the AWS CDK to destroy the resources, deactivate your Python virtual environment, and go to the root of the chapter:

`cdk destroy && deactivate && rm -r .venv/ && cd ../..`
