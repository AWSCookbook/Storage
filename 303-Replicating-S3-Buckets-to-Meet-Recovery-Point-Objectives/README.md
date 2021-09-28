# Replicating S3 Buckets to Meet Recovery Point Objectives
## Preparation
### Set a unique suffix to use for the S3 bucket name:
```
RANDOM_STRING=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)
```

### Create Source S3 bucket:

`aws s3api create-bucket --bucket awscookbook303-src-$RANDOM_STRING`

### Enable Versioning for the Source S3 bucket:
```
aws s3api put-bucket-versioning \
--bucket awscookbook303-src-$RANDOM_STRING \
--versioning-configuration Status=Enabled
```



## Clean up 
### Delete the all versions of the files in your S3 buckets using some helper Python scripts provided in the code repository for this chapter:
```
export EXPORTED_RANDOM_STRING=$RANDOM_STRING
test -d .venv || python3 -m venv .venv
source .venv/bin/activate
pip install boto3
python src-bucket-versions-del.py
python dst-bucket-versions-del.py
deactivate
rm -rf .venv
unset EXPORTED_RANDOM_STRING
```

### Delete the Source S3 bucket:

`aws s3api delete-bucket --bucket awscookbook303-src-$RANDOM_STRING`

### Delete the Destination S3 bucket:

`aws s3api delete-bucket --bucket awscookbook303-dst-$RANDOM_STRING`

### Delete the IAM Policy from the role:
```
aws iam delete-role-policy \
--role-name AWSCookbook303S3Role --policy-name S3ReplicationPolicy
```

### Delete the IAM Role:

`aws iam delete-role --role-name AWSCookbook303S3Role`

### Unset the environment variable that you created manually:
```
unset RANDOM_STRING
unset ROLE_ARN
unset VERSION_ID
```
