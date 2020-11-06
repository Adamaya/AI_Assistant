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
    :param drive: example "/dev/sda"
    :return: output variable that contains exit code and output string in tuple datatype.
    """
    cmd = "pvcreate {}"
    output = sp.getstatusoutput(cmd.format(drive))
    return output


def create_volume_group(vgname, drives):
    """
    this function creates the volume group for creating logical volume
    :param vgname: name of volume group
    :param drives: path of attached ddrive example "/dev/sda /dev/sdb"
    :return: output variable that contains exit code and output string in tuple datatype
    """
    cmd = "vgcreate {} {}"
    output = sp.getstatusoutput(cmd.format(vgname, drives))
    return output


def display_volume_group():
    """
    this function display the available volume group
    :return: output variable that contains exit code and output string in tuple datatype
    """
    cmd = "vgdisplay"
    output = sp.getstatusoutput(cmd)
    return output


def create_logical_volume(vgname, lvname, size):
    """
    this function creates the logical volume in volume group
    :return: output variable that contains exit code and output string in tuple datatype
    :param vgname: name of volume group
    :param lvname: name of logical volume
    """
    cmd = "lvcreate --size +{}G --name {} {}"
    output = sp.getstatusoutput(cmd.format(size, lvname, vgname))
    return output


def mount_logical_volume(mountDirPath, lvPath):
    """
    this function mounts the logical volume to the newly created directory.
    :param mountDirPath: path to mount directory
    :param lvPath: logical volume path
    :return: output variable that contains exit code and output string in tuple datatype
    """
    cmd = "mount {} {}"
    output = sp.getstatusoutput(cmd.format(lvPath, mountDirPath))
    return output
