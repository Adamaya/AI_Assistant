import os

"""
namenode configuration
if host = 0 --> local configure
if host = 1 --> remote configure

"""

def namenode_configuration(namenode_ip,namenode_directory,namenode_password,host):
    if host==0:
            os.system("sudo mkdir /{}".format(namenode_directory))
            f1=open("/etc/hadoop/hdfs-site.xml","w")
            f1.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> \n\n\n<!-- Put site-specific property overrides in this file. -->\n\n\n<configuration>\n\n<property>\n<name>dfs.name.dir</name>\n<value>/{}</value>\n</property>\n\n</configuration>'.format(namenode_directory))
            f1.close()
            f2=open("/etc/hadoop/core-site.xml","w")
            f2.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n\n</configuration>'.format(namenode_ip))
            f2.close()
            os.system("sudo hadoop namenode -format")
    else:
            os.system('sshpass -p "{}" sudo ssh {} "sudo mkdir /{}"'.format(namenode_password,namenode_ip,namenode_directory))
            os.system("sudo touch /root/hdfs-site.xml")
            f1=open("/root/hdfs-site.xml","w")
            f1.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> \n\n\n<!-- Put site-specific property overrides in this file. -->\n\n\n<configuration>\n\n<property>\n<name>dfs.name.dir</name>\n<value>/{}</value>\n</property>\n\n</configuration>'.format(namenode_directory))
            f1.close()
            os.system("sudo touch /root/core-site.xml")
            f2=open("/root/core-site.xml","w")
            f2.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n\n</configuration>'.format(namenode_ip))
            f2.close()
            os.system('sshpass -p "{}" sudo scp hdfs-site.xml {}:/etc/hadoop'.format(namenode_password,namenode_ip))
            os.system('sshpass -p "{}" sudo scp core-site.xml {}:/etc/hadoop'.format(namenode_password,namenode_ip))
            os.system('sshpass -p "{}" sudo ssh {} "sudo hadoop namenode -format"'.format(namenode_password,namenode_ip))

"""
datanode configuration
if host = 0 --> local configure
if host = 1 --> remote configure

"""  


def datanode_configuration(namenode_ip,datanode_ip,datanode_directory,datanode_password,host):

    if host==0:
                os.system("sudo mkdir /{}".format(datanode_directory))
                f1=open("/etc/hadoop/hdfs-site.xml","w")
                f1.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> \n\n\n<!-- Put site-specific property overrides in this file. -->\n\n\n<configuration>\n\n<property>\n<name>dfs.data.dir</name>\n<value>/{}</value>\n</property>\n\n</configuration>'.format(datanode_directory))
                f1.close()
                f2=open("/etc/hadoop/core-site.xml","w")
                f2.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n\n</configuration>'.format(namenode_ip))
                f2.close()

    else:
                os.system('sshpass -p "{}" sudo ssh {} "sudo mkdir /{}"'.format(datanode_password,datanode_ip,datanode_directory))
                os.system("sudo touch /root/hdfs-site.xml")
                f1=open("/root/hdfs-site.xml","w")
                f1.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> \n\n\n<!-- Put site-specific property overrides in this file. -->\n\n\n<configuration>\n\n<property>\n<name>dfs.data.dir</name>\n<value>/{}</value>\n</property>\n\n</configuration>'.format(datanode_directory))
                f1.close()
                os.system("sudo touch /root/core-site.xml")
                f2=open("/root/core-site.xml","w")
                f2.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n\n</configuration>'.format(namenode_ip))
                f2.close()
                os.system('sshpass -p "{}" sudo scp hdfs-site.xml {}:/etc/hadoop'.format(datanode_password,datanode_ip))
                os.system('sshpass -p "{}" sudo scp core-site.xml {}:/etc/hadoop'.format(datanode_password,datanode_ip))

"""
namenode / datanode --> start
if host = 0 --> local start
if host = 1 --> remote start

"""
def namenode_start(namenode_ip,namenode_password,host):
    if host==0:

        """ start name_node """
        
        os.system("sudo hadoop-daemon.sh start namenode")
    else:
        os.system('sshpass -p "{}" sudo ssh {} "sudo hadoop-daemon.sh start namenode"'.format(namenode_password,namenode_ip))

def datanode_start(datanode_ip,datanode_password,host):
    if host==0:

        """ start data_node"""

        os.system("sudo hadoop-daemon.sh start datanode")
    else:
        os.system('sshpass -p "{}" sudo ssh {} "sudo hadoop-daemon.sh start datanode"'.format(datanode_password,datanode_ip))
"""
namenode /datanode --> stop
if host = 0 --> local stop
if host = 1 --> remote stop

"""
def namenode_stop(namenode_ip,namenode_password,host):
    if host==0:

        """ stop name_node"""

        os.system("sudo hadoop-daemon.sh stop namenode")
    else:
        os.system('sshpass -p "{}" sudo ssh {} "sudo hadoop-daemon.sh stop namenode"'.format(namenode_password,namenode_ip))

def datanode_stop(datanode_ip,datanode_password,host):
    if host==0:

        """ stop data_node"""

        os.system("sudo hadoop-daemon.sh stop datanode")
    else:
        os.system('sshpass -p "{}" sudo ssh {} "sudo hadoop-daemon.sh stop datanode"'.format(datanode_password,datanode_ip))

"""
report checking

"""
def check_report(host):
        os.system("sudo hadoop dfsadmin -report")
   