import os
import subprocess as sp


def namenode_configuration(namenode_ip, namenode_directory, namenode_password, host):
    """
    this function configures the namenode on local host and remote system
    if host = 0 --> local configure
    if host = 1 --> remote configure

    :param namenode_ip: string ip of namenode
    :param namenode_directory: string path to namenode directory
    :param namenode_password: string namenode password
    :param host: integer value (0 or 1)
    :return:
    """

    if host == 0:
        os.system("sudo mkdir /{}".format(namenode_directory))
        f1 = open("/etc/hadoop/hdfs-site.xml", "w")
        f1.write(
            '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> \n\n\n<!-- Put site-specific property overrides in this file. -->\n\n\n<configuration>\n\n<property>\n<name>dfs.name.dir</name>\n<value>/{}</value>\n</property>\n\n</configuration>'.format(
                namenode_directory))
        f1.close()
        f2 = open("/etc/hadoop/core-site.xml", "w")
        f2.write(
            '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n\n</configuration>'.format(
                namenode_ip))
        f2.close()
        os.system("sudo echo Y | hadoop namenode -format")
    else:
        os.system('sshpass -p "{}" sudo ssh root@{} "sudo mkdir /root/{}"'.format(namenode_password, namenode_ip,
                                                                             namenode_directory))
        os.system("sudo touch /root/hdfs-site.xml")
        f1 = open("/root/hdfs-site.xml", "w")
        f1.write(
            '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> \n\n\n<!-- Put site-specific property overrides in this file. -->\n\n\n<configuration>\n\n<property>\n<name>dfs.name.dir</name>\n<value>/{}</value>\n</property>\n\n</configuration>'.format(
                namenode_directory))
        f1.close()
        os.system("sudo touch /root/core-site.xml")
        f2 = open("/root/core-site.xml", "w")
        f2.write(
            '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n\n</configuration>'.format(
                namenode_ip))
        f2.close()
        os.system('sshpass -p "{}" sudo scp /root/hdfs-site.xml {}:/etc/hadoop'.format(namenode_password, namenode_ip))
        os.system('sshpass -p "{}" sudo scp /root/core-site.xml {}:/etc/hadoop'.format(namenode_password, namenode_ip))
        os.system(
            "sshpass -p '{}' sudo ssh root@{} sudo hadoop namenode -format -y".format(namenode_password, namenode_ip))


def datanode_configuration(namenode_ip, datanode_ip, datanode_directory, datanode_password, host):
    """
    this function configures the datanode on local host and remote system
    if host = 0 --> local configure
    if host = 1 --> remote configure

    :param namenode_ip: string datatype namenode ip
    :param datanode_ip: string datatype datanode ip
    :param datanode_directory: string datatype datanode directory path
    :param datanode_password: string password of datanode system
    :param host: integer value (0 or 1)
    :return:
    """
    if host == 0:
        os.system("sudo mkdir /{}".format(datanode_directory))
        f1 = open("/etc/hadoop/hdfs-site.xml", "w")
        f1.write(
            '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> \n\n\n<!-- Put site-specific property overrides in this file. -->\n\n\n<configuration>\n\n<property>\n<name>dfs.data.dir</name>\n<value>/{}</value>\n</property>\n\n</configuration>'.format(
                datanode_directory))
        f1.close()
        f2 = open("/etc/hadoop/core-site.xml", "w")
        f2.write(
            '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n\n</configuration>'.format(
                namenode_ip))
        f2.close()

    else:
        os.system('sshpass -p "{}" sudo ssh root@{} "sudo mkdir /{}"'.format(datanode_password, datanode_ip,
                                                                             datanode_directory))
        os.system("sudo touch /root/hdfs-site.xml")
        f1 = open("/root/hdfs-site.xml", "w")
        f1.write(
            '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> \n\n\n<!-- Put site-specific property overrides in this file. -->\n\n\n<configuration>\n\n<property>\n<name>dfs.data.dir</name>\n<value>/{}</value>\n</property>\n\n</configuration>'.format(
                datanode_directory))
        f1.close()
        os.system("sudo touch /root/core-site.xml")
        f2 = open("/root/core-site.xml", "w")
        f2.write(
            '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n\n</configuration>'.format(
                namenode_ip))
        f2.close()
        os.system('sshpass -p "{}" sudo scp hdfs-site.xml {}:/etc/hadoop'.format(datanode_password, datanode_ip))
        os.system('sshpass -p "{}" sudo scp core-site.xml {}:/etc/hadoop'.format(datanode_password, datanode_ip))


def namenode_start(namenode_ip, namenode_password, host):
    """
    this function starts the namenode
    if host = 0 --> local start
    if host = 1 --> remote start
    :param namenode_ip: string datatype namenode ip
    :param namenode_password: string datatype namenode password
    :param host: integer value (0 or 1)
    :return: output tuple variable
    """
    if host == 0:
        output = sp.getstatusoutput("sudo hadoop-daemon.sh start namenode")
        return output
    else:
        output = sp.getstatusoutput(
            'sshpass -p "{}" sudo ssh root@{} "sudo hadoop-daemon.sh start namenode"'.format(namenode_password,
                                                                                             namenode_ip))
        return output


def datanode_start(datanode_ip, datanode_password, host):
    """
    this function starts the datanode
    :param datanode_ip: string datatype datanode ip
    :param datanode_password: string datatype datanode ip
    :param host: integer value (0 or 1)
    :return: output tuple datatype variable
    """
    if host == 0:
        output = sp.getstatusoutput("sudo hadoop-daemon.sh start datanode")
        return output
    else:
        output = sp.getstatusoutput(
            'sshpass -p "{}" sudo ssh root@{} "sudo hadoop-daemon.sh start datanode"'.format(datanode_password,
                                                                                             datanode_ip))
        return output


def namenode_stop(namenode_ip, namenode_password, host):
    """
    this function stops the name node daemon.
    if host = 0 --> local name node stop
    if host = 1 --> remote name node stop
    :param namenode_ip: string datatype namenode ip
    :param namenode_password: string datatype name node ip
    :param host: integer value (0 or 1)
    :return: output tuple datatype variable
    """
    if host == 0:
        output = sp.getstatusoutput("sudo hadoop-daemon.sh stop namenode")
        return output
    else:
        output = sp.getstatusoutput(
            'sshpass -p "{}" sudo ssh root@{} "sudo hadoop-daemon.sh stop namenode"'.format(namenode_password,
                                                                                            namenode_ip))
        return output


def datanode_stop(datanode_ip, datanode_password, host):
    """
    this function stops the data node daemon.
    if host = 0 --> local data node stop
    if host = 1 --> remote data node stop
    :param datanode_ip: string datatype data node ip
    :param datanode_password: string datatype data node password
    :param host: integer value (0 or 1)
    :return: output tuple datatype variable
    """
    if host == 0:
        output = sp.getstatusoutput("sudo hadoop-daemon.sh stop datanode")
        return output
    else:
        output = sp.getstatusoutput(
            'sshpass -p "{}" sudo ssh root@{} "sudo hadoop-daemon.sh stop datanode"'.format(datanode_password,
                                                                                            datanode_ip))
        return output


def check_report():
    """
    this function shows the report of hadoop cluster
    :return: output tuple variable containing cluster report.
    """
    output = sp.getstatusoutput("sudo hadoop dfsadmin -report")
    return output
