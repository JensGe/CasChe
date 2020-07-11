import boto3
import os

ec2 = boto3.client("ec2", region_name="eu-central-1")
s3 = boto3.client("s3")

s3_bucket = "fetsim-logs"
logs_folder = "fetsim-logs"


def create_instance(settings):
    response = ec2.run_instances(
        LaunchTemplate={"LaunchTemplateId": "lt-0344130210c1eaca5", "Version": "8"},
        MinCount=settings["parallel_fetcher"],
        MaxCount=settings["parallel_fetcher"],
    )
    ids = [instance["InstanceId"] for instance in response["Instances"]]
    return ids


def terminate_instance(instance_id):
    ec2.terminate_instances(InstanceIds=[instance_id])


def download_file(file_name):
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)

    files = s3.list_objects_v2(Bucket=s3_bucket)

    if files["KeyCount"] == 0:
        return False

    for file in files["Contents"]:
        bucket_file_name = s3_bucket + "/" + file_name

        if file["Key"] == bucket_file_name:
            s3.download_file(
                s3_bucket,
                "{}/{}".format(s3_bucket, file_name),
                logs_folder + "/" + file_name,
            )
            s3.delete_object(
                Bucket=s3_bucket,
                Key="{}/{}".format(s3_bucket, file_name),
            )
            return True

    return False




