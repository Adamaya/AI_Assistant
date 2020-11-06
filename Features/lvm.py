import subprocess as sp


def attached_drive_report():
    """
    this function runs the fdisk -l command to show the attached drives to os
    :return: attached drive report with exit code
    """
    cmd = "sudo fdisk -l"
    output = sp.getstatusoutput(cmd)
    return output


def create_physical_volume(drive):
    """
    this function creates a physical volume of selected harddrive
    :param drive: example "/dev/sda" with exit code
    :return:
    """
    cmd = "pvcreate {}"
    output = sp.getstatusoutput(cmd.format(drive))
    return output
