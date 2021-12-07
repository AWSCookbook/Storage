# Using Amazon S3 Bucket Keys with KMS
## Preparation
### Set a unique suffix to use for the S3 bucket name:
```
RANDOM_STRING=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)
```

### Create an S3 bucket 
```
aws s3api create-bucket --bucket awscookbook306-$RANDOM_STRING
```

## Clean up 
### Delete the file you copied to your S3 bucket:

`aws s3 rm s3://awscookbook306-$RANDOM_STRING/book_cover.png`

### Delete the S3 bucket:

`aws s3api delete-bucket --bucket awscookbook306-$RANDOM_STRING`

### Disable the KMS Key: 

`aws kms disable-key --key-id $KEY_ID`

### Scheduled the KMS Key for deletion:
```
aws kms schedule-key-deletion \
--key-id $KEY_ID \
--pending-window-in-days 7
```

### Delete the Key Alias: 

`aws kms delete-alias --alias-name alias/awscookbook306`
