import os


def Namenode_confi():
    Ip=input("what is your IP:")
    os.system("mkdir /nn")
    f1=open("/etc/hadoop/hdfs-site.xml","w")
    f1.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> \n\n\n<!-- Put site-specific property overrides in this file. -->\n\n\n<configuration>\n\n<property>\n<name>dfs.name.dir</name>\n<value>/nn</value>\n</property>\n\n</configuration>')
    f1.close()
    f2=open("/etc/hadoop/core-site.xml","w")
    f2.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n\n</configuration>'.format(Ip))
    f2.close()
    os.system("hadoop namenode -format")


def Datanode_confi():
    Ip=input("what is Master Node IP:")
    os.system("mkdir /dn")
    f1=open("/etc/hadoop/hdfs-site.xml","w")
    f1.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> \n\n\n<!-- Put site-specific property overrides in this file. -->\n\n\n<configuration>\n\n<property>\n<name>dfs.data.dir</name>\n<value>/dn</value>\n</property>\n\n</configuration>')
    f1.close()
    f2=open("/etc/hadoop/core-site.xml","w")
    f2.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n\n</configuration>'.format(Ip))
    f2.close()

def Namenode_start():
    os.system("hadoop-daemon.sh start namenode")

def datanode_start():
    os.system("hadoop-daemon.sh start datanode")

def Namenode_stop():
    os.system("hadoop-daemon.sh stop namenode")

def Datanode_stop():
    os.system("hadoop-daemon.sh stopt datanode")

def check_report():
    os.system("hadoop dfsadmin -report")
