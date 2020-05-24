import boto3
import os

ec2 = boto3.client("ec2")
s3 = boto3.client("s3")

s3_bucket = "fetsim-logs"
logs_folder = "fetsim-logs"


def create_instance():
    response = ec2.run_instances(
        LaunchTemplate={"LaunchTemplateId": "lt-0344130210c1eaca5", "Version": "5"},
        MinCount=1,
        MaxCount=1,
    )
    return response["Instances"][0]["InstanceId"]


def terminate_instance(instance_id):
    ec2.terminate_instances(InstanceIds=[instance_id])


def download_file(file_name):
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)

    files = s3.list_objects_v2(Bucket=s3_bucket)

    if files["KeyCount"] == 0:
        print("*** Log List empty")
        return False

    for file in files["Contents"]:
        bucket_file_name = s3_bucket + "/" + file_name

        if file["Key"] == bucket_file_name:
            s3.download_file(
                s3_bucket,
                "{}/{}".format(s3_bucket, file_name),
                logs_folder + "/" + file_name,
            )
            return True

    return False




