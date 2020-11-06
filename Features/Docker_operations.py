import subprocess as sp

<<<<<<< HEAD
"""
    this shows all the docker container images that are currently downloaded
"""
=======

>>>>>>> 5cac67895acd5d4f2bfe63c71cd112496c8aaba5
def check_available_images():
    cmd = 'sudo docker images'
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print('Available Docker Images are -\n {}'.format(out[1]))
    else:
        print('Some ERROR : {}'.format(out[1]))

<<<<<<< HEAD
"""
    this launches a docker container with the given OS-name and OS-image
"""
=======

>>>>>>> 5cac67895acd5d4f2bfe63c71cd112496c8aaba5
def launch_container(osname, image):
    cmd = 'sudo docker run -d -t -i --name {0} {1}'.format(osname, image)
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print("Container Launched with OS {0} named {1}.".format(image, osname))
    else:
        print('Some ERROR : {}'.format(out[1]))


<<<<<<< HEAD
"""
    this stops a container that is currently running with given os-name
"""
=======
>>>>>>> 5cac67895acd5d4f2bfe63c71cd112496c8aaba5
def stop_running_container(osname):
    cmd = 'sudo docker stop {}'.format(osname)
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print("Container named {} is now stopped.".format(osname))
    else:
        print("Some ERROR : {}".format(out[1]))


<<<<<<< HEAD
"""
    runs a container that had been launched previously & stopped
"""
=======
>>>>>>> 5cac67895acd5d4f2bfe63c71cd112496c8aaba5
def run_prelaunched_container(osname):
    cmd = 'sudo docker start {}'.format(osname)
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print("Container named {} is now active.".format(osname))
    else:
        print("Some ERROR : {}".format(out[1]))


<<<<<<< HEAD
"""
    shows all the containers that are running
"""
=======
>>>>>>> 5cac67895acd5d4f2bfe63c71cd112496c8aaba5
def show_currently_running_containers():
    cmd = 'sudo docker ps'
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print("Currently running docker containers are -\n{}".format(out[1]))
    else:
        print("Some ERROR : {}".format(out[1]))


<<<<<<< HEAD
"""
    deletes all containers that are alive
"""
=======
>>>>>>> 5cac67895acd5d4f2bfe63c71cd112496c8aaba5
def delete_all_containers():
    cmd = 'sudo docker rm `docker ps -a -q`'
    out = sp.getstatusoutput(cmd)
    if out[0] == 0:
        print("All containers are deleted.")
    else:
        print("Some ERROR : {}".format(out[1]))
