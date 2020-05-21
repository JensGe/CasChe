import boto3

ec2 = boto3.client("ec2")
s3 = boto3.client("s3")

s3_bucket = "fetsim-logs"
logs_folder = s3_bucket


def create_instance():
    response = ec2.run_instances(
        LaunchTemplate={"LaunchTemplateId": "lt-0344130210c1eaca5", "Version": "4",},
        MinCount=1,
        MaxCount=1,
    )
    return response["Instances"][0]["InstanceId"]


def terminate_instance(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])


def download_file(file_name):
    files = s3.list_objects_v2(Bucket=s3_bucket)

    if files["KeyCount"] == 0:
        return False

    for file in files["Contents"]:
        if file["Key"] == s3_bucket + "/" + file_name:
            s3.download_file(
                s3_bucket,
                "{}/{}".format(s3_bucket, file_name),
                logs_folder + "/" + file_name,
            )
            return True

    return False


# print(download_file("x"))


