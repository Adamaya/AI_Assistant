import subprocess as sp


def attached_drive_report():
    """
    this function runs the fdisk -l command to show the attached drives to os
    :return: attached drive report
    """
    cmd = "sudo fdisk -l"
    output = sp.getstatusoutput(cmd)
    return output[0]
