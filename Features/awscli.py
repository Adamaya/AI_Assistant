import subprocess, os


def aws_authentication(access_key, secret_key, region):
    access_key = ""
    secret_key = ""
    region = "ap-south-1"

    os.system("aws configure set aws_access_key_id " + access_key)
    os.system("aws configure set aws_secret_access_key " + secret_key)
    os.system("aws configure set default.region " + region)
    return None


def launch_ec2_instance():
    output = subprocess.getstatusoutput(
        "aws ec2 run-instances --image-id ami-0e306788ff2473ccb --key-name myclikey --security-groups cliInstanceSecurityGroup --instance-type t2.micro")
    return None


def create_security_group():
    output = subprocess.getstatusoutput(
        'aws ec2 create-security-group --group-name "cliInstanceSecurityGroup" --description "this is the security group created for the new instance" --vpc-id vpc-3fe8f557')
    print(output)
    return None


create_security_group()
