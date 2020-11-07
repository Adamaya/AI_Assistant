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


def launch_ec2_instance():
    output = subprocess.getstatusoutput(
        "aws ec2 run-instances --image-id ami-0e306788ff2473ccb --key-name myclikey --security-groups cliInstanceSecurityGroup --instance-type t2.micro"
    )
    return output


def create_security_group():
    output = subprocess.getstatusoutput(
        'aws ec2 create-security-group --group-name "cliInstanceSecurityGroup" --description "this is the security group created for the new instance" --vpc-id vpc-3fe8f557'
    )
    return output


def create_volume():
    output = subprocess.getstatusoutput()
