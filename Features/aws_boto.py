import subprocess, os
import boto3

client = boto3.client('ec2')

def aws_authentication(access_key, secret_key, region):
    """
    authentication of the user
    """
    access_key = ""
    secret_key = ""
    region = "ap-south-1"

    out1 = os.system("aws configure set aws_access_key_id {}".format(access_key))
    out2 = os.system("aws configure set aws_secret_access_key {}".format(secret_key))
    out3 = os.system("aws configure set default.region {}".format(region))
    if out1[0] == 0 and out2[0] == 0 and out3[0] == 0:
        return 0
    else:
        return 1


def create_key_pair(key_name):
    """
    creating a new key pair
    """
    response = client.create_key_pair(
        KeyName='my-key-pair',
    )   
    return response


def launch_ec2_instance(size, ami_id, key_name, security_grp, instance_type):
    """
    launch a new ec2 instance
    """
    response = client.run_instances(
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/sdh',
                'Ebs': {
                    'VolumeSize': size,
                },
            },
        ],
        ImageId=ami_id,  #'ami-abc12345',
        InstanceType=instance_type ,#'t2.micro',
        KeyName= key_name,  #'my-key-pair',
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            security_grp,
        ],
        SubnetId='subnet-6e7f829e',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Purpose',
                        'Value': 'test',
                    },
                ],
            },
        ],
    )

    return response


def create_security_group(group_name, description):
    """
    create a new aws security group
    """
    response = client.create_security_group(
        Description=description,
        GroupName=group_name,
        #VpcId='vpc-1a2b3c4d',
    )

    return response


def create_volume(AZ, size, vol_type):
    """
    create a new EBS volume
    """
    response = client.create_volume(
        AvailabilityZone=AZ,
        Size=size,
        VolumeType=vol_type,
    )

    return response


def attach_volume(instance_id, volume_id):
    """
    attach a EBS volume to an instance
    """
    response = client.attach_volume(
        Device='/dev/sdf',
        InstanceId = instance_id,
        VolumeId = volume_id,
    )

    return response


def s3_addition(bucket_name, region):
    """
    add a new s3
    """
    client = boto3.client('s3')

    response = client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region,
        },
    )

    return response