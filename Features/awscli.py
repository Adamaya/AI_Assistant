import subprocess, os


def aws_authentication(access_key, secret_key, region):
    access_key = ""
    secret_key = ""
    region = "ap-south-1"

    out1 = os.system("aws configure set aws_access_key_id {}".format(access_key))
    out2 = os.system("aws configure set aws_secret_access_key {}".format(secret_key))
    out3 = os.system("aws configure set default.region {}".format(region))
    return (out1,out2,out3)


def create_key_pair(key_name):
    output = os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
    return output


def launch_ec2_instance(ami_id, key_name, security_grp, instance_type):
    output = subprocess.getstatusoutput("aws ec2 run-instances --image-id {0} --key-name {1} --security-groups {2} --instance-type {3}".format(ami_id,key_name,security_grp,instance_type))
    return output


def create_security_group(group_name, description):
    output = subprocess.getstatusoutput('aws ec2 create-security-group --group-name "{0}" --description "{1}" '.format(group_name,description))
    return output


def create_volume(AZ, size, vol_type):
    output = subprocess.getstatusoutput("aws ec2 create-volume --availability-zone {0} --size {1} --volume-type {2}".format(AZ,size,vol_type))
    return output


def attach_volume(instance_id, volume_id):
    output = subprocess.getstatusoutput("aws ec2 attach-volume --instance-id {0} --volume-id {1} --device /dev/sdh".format(instance_id,volume_id))
    return output


def s3_addition(bucket_name, region):
    output = subprocess.getstatusoutput("aws s3api create-bucket --bucket {0} --region {1} --create-bucket-configuration LocationConstraint={1}".format(bucket_name,region))
    return output