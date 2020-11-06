import subprocess as sp


def check_available_images():
    cmd = 'sudo docker images'
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print('Available Docker Images are -\n {}'.format(out[1]))
    else:
        print('Some ERROR : {}'.format(out[1]))


def launch_container(osname, image):
    cmd = 'sudo docker run -d -t -i --name {0} {1}'.format(osname, image)
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print("Container Launched with OS {0} named {1}.".format(image, osname))
    else:
        print('Some ERROR : {}'.format(out[1]))


def stop_running_container(osname):
    cmd = 'sudo docker stop {}'.format(osname)
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print("Container named {} is now stopped.".format(osname))
    else:
        print("Some ERROR : {}".format(out[1]))


def run_prelaunched_container(osname):
    cmd = 'sudo docker start {}'.format(osname)
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print("Container named {} is now active.".format(osname))
    else:
        print("Some ERROR : {}".format(out[1]))


def show_currently_running_containers():
    cmd = 'sudo docker ps'
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print("Currently running docker containers are -\n{}".format(out[1]))
    else:
        print("Some ERROR : {}".format(out[1]))


def delete_all_containers():
    cmd = 'sudo docker rm `docker ps -a -q`'
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print("All containers are deleted.")
    else:
        print("Some ERROR : {}".format(out[1]))
