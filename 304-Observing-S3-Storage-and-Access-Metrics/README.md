# Observing S3 Storage and Access Metrics
## Preparation
### Set a unique suffix to use for the S3 bucket name:
```
RANDOM_STRING=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)
```

### Create an S3 bucket:

`aws s3api create-bucket --bucket awscookbook304-$RANDOM_STRING`



## Clean up 
### Delete the Storage Lens Dashboard configuration that you applied.
Instructions [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_console_deleting.html)

### Delete the Source S3 bucket:

`aws s3api delete-bucket --bucket awscookbook304-$RANDOM_STRING`
