import boto3

ec2 = boto3.client("ec2")


def create_instance():
    response = ec2.run_instances(
        LaunchTemplate={
            "LaunchTemplateId": "lt-0344130210c1eaca5",
            "Version": "4",
        },
        MinCount=1,
        MaxCount=1,
    )
    return response["Instances"][0]["InstanceId"]


def terminate_instance(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])

