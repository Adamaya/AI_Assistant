import subprocess as sp



def check_available_images():
    """
    this shows all the docker container images that are currently downloaded
    """
    cmd = 'sudo docker images'
    out = sp.getstatusoutput(cmd)
    return out


def launch_container(osname, image):
    """
    this launches a docker container with the given OS-name and OS-image
    :param osname: os image name for docker container
    :param image: container image
    :return:
    """

    cmd = 'sudo docker run -d -t -i --name {0} {1}'.format(osname, image)
    out = sp.getstatusoutput(cmd)
    return out


def stop_running_container(osname):
    """
        this stops a container that is currently running with given os-name
    """

    cmd = 'sudo docker stop {}'.format(osname)
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print("Container named {} is now stopped.".format(osname))
    else:
        print("Some ERROR : {}".format(out[1]))


def run_prelaunched_container(osname):
    """
        runs a container that had been launched previously & stopped
    """

    cmd = 'sudo docker start {}'.format(osname)
    out = sp.getstatusoutput(cmd)
    return out


def show_currently_running_containers():
    """
        shows all the containers that are running
    """

    cmd = 'sudo docker ps'
    out = sp.getstatusoutput(cmd)
    return out


def delete_all_containers():
    """
        deletes all containers that are alive
    """
    cmd = 'sudo docker rm `docker ps -a -q`'
    out = sp.getstatusoutput(cmd)
    return out
