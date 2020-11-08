from Features.ai_features import Ai_Features
from database.profile_manager import Profile_Manager
import Features.Docker_operations as docker
from voice.voice_configuration import speak
import Features.lvm as lvm
import Features.hadoop as hadoop
#import Features.awscli as aws
import Features.ML_Features.salary_estimator as sal
import Features.aws_boto as aws

def select_in_between_user_login_and_create_profile():
    """
    it checks the user option recursively till user do not select the valid input.
    :return: it returns an integer value.
    """
    option = int(input("select your option (1)/(2): "))
    if option == 1:
        return 1

    elif option == 2:
        return 2
    else:
        print("Please select valid option")
        select_in_between_user_login_and_create_profile()


try:
    profile_manager = Profile_Manager()
except Exception as e:
    print("profile manager is not working")
    exit()

while (True):
    print("""
    __Welcome to AI Console__ \n\nUser Login(1)\t\tCreate New Profile(2)
    """)
    user_option = select_in_between_user_login_and_create_profile()
    if user_option == 1:
        print("-----User Login----- ")
        while (True):
            username = input('User Name Id: ')
            password = input('Password: ')
            voice_code = 0
            verified = profile_manager.authentication(username, password)
            if verified:
                # TODO create my_sql database for profile data
                print("Welcome")
                break
            else:
                print("enter the valid username password or create the profile first")
                continue
        ai = Ai_Features()
        while (True):
            print("Here are the features of the Saha Assistent")
            print("1. create patitions")
            print("2. configure hadoop cluster")
            print("3. docker operations")
            print("4. Aws commands")
            print("5. Salery predictor using Linear Resgression")

            query = None
            while (query == None):
                query = ai.takeCommand()
            query = query.lower()
            if 'wikipedia' in query:
                ai.wikipedia_search(query, 2)

            elif "exit" in query:
                speak("Have a good day!")
                exit()

            elif "open" in query and ".com" in query:
                ai.open_website(query)

            elif "where is" in query:
                ai.location_finder(query)

            elif "play music" in query:
                ai.play_music()

            elif "search" in query and "google" in query:
                ai.google_search(query)

            elif "docker" in query:
                print("""
                1. Check available images
                2. Launch a Container
                3. stop a running container
                4. Relaunch a Stopped container
                5. Show corrently Running Container
                6. Delete all containers
                """)
                speak("speak one of the following commands to execute the docker operations")

                command = None
                while command == None:
                    command = ai.takeCommand()
                command = command.lower()
                if "check" in command and "available" in command and "images" in command:
                    status = docker.check_available_images()
                    if status[0] == 0:
                        speak("here are the available images")
                        print(status[1])
                elif "launch" in command and "container" in command:
                    osname = input("Enter the Container name for your OS: ")
                    image_name = input("Enter the OS image you want to use: ")
                    print("launching")
                    status = docker.launch_container(osname, image_name)
                    if status[0] == 0:
                        print("container launched successfuly")
                        print(status[1])
                    else:
                        print("failed to launch the container")
                        print(status[1])

                elif "stop" in command and "running" in command and "container" in command:
                    osname = input("Enter the Container name for your OS: ")
                    status = docker.stop_running_container(osname)
                    print("Stopping the container")
                    if status[0] == 0:
                        print("container has been stopped successfuly")
                        print(status[1])
                    else:
                        print("failed to stop the container")
                        print(status[1])

                elif "relaunch" in command and "stopped" in command and "container" in command:
                    osname = input("Enter the Container name for your OS: ")
                    status = docker.run_prelaunched_container(osname)
                    print("Relaunching....")
                    if status[0] == 0:
                        print("container has been relaunched successfuly")
                        print(status[1])
                    else:
                        print("failed to relaunch the container")
                        print(status[1])

                elif "show" in command and "running" in command and "container" in command:
                    status = docker.show_currently_running_containers()
                    if status[0] == 0:
                        print("here are the running containers")
                        print(status[1])
                    else:
                        print("docker internal error occered")
                        print(status[1])

                # TODO notworking correctly with voice
                elif "delete" in command and "all" in command and "container" in command:
                    status = docker.delete_all_containers()
                    if status[0] == 0:
                        print("all containers has been deleted successfuly")
                        print(status[1])
                    else:
                        print("failed to delete the containers")
                        print(status[1])

            elif "partition" in query:
                print("""
                1. Show Available Partitions
                2. Create Physical Volume
                3. Display Physical Volume
                4. Create Volume Group
                5. Display Volume Group
                6. Create Logical Volume
                7. Format Logical Volume
                8. Mount the LV
                9. Extend the LV                              
                """)
                speak("speak one of the following commands for partition operations")

                command = None
                while command == None:
                    command = ai.takeCommand()
                command = command.lower()
                if "available partitions" in command:
                    status = lvm.attached_drive_report()
                    if status[0] == 0:
                        print("here are the available drives")
                        print(status[1])
                elif "create" in command and "physical" in command:
                    drivepath = input("enter the drive path")
                    print("creating")
                    status = lvm.create_physical_volume(drivepath)
                    if status[0] == 0:
                        speak("pv created")
                        print(status[1])
                    else:
                        print(status[1])

                elif "physical" in command and "volume" in command and "show" in command:
                    status = lvm.display_physical_volume()
                    if status[0] == 0:
                        speak("here are the list of physical volumes")
                        print(status[1])
                    else:
                        speak("failed to display physical volume due to following error")
                        print(status[1])

                elif "create" in command and "volume" in command and "group" in command:
                    vgname = input("Enter the Volume group name: ")
                    drives = input("Enter the drive paths")
                    status = lvm.create_volume_group(vgname, drives)
                    speak("Creating volume group")
                    if status[0] == 0:
                        speak("volume group created successfully successfuly")
                        print(status[1])
                    else:
                        speak("failed to create volume group due to following error")
                        print(status[1])

                elif "group" in command and "volume" in command and "show" in command:
                    status = lvm.display_volume_group()
                    if status[0] == 0:
                        speak("here are the available volume groups")
                        print(status[1])
                    else:
                        speak("failed to show available volume group due to following error")
                        print(status[1])

                elif "create" in command and "logical" in command and "volume" in command:
                    vgname = input("Enter the volume group name: ")
                    lvname = input("Enter the logical volume name: ")
                    size = input("Enter the size in of new partition in GB: ")
                    status = lvm.create_logical_volume(vgname, lvname, size)
                    if status[0] == 0:
                        speak("logical volume has been created successfully")
                        print(status[1])
                    else:
                        speak("failed to create logical volume due to following reason")
                        print(status[1])

                elif "format" in command and "logical" in command and "volume" in command:
                    lvpath = input("Enter the logical volume group name: ")
                    status = lvm.format_logical_volume(lvpath)
                    if status[0] == 0:
                        speak("logical volume has been mounted successfully")
                        print(status[1])
                    else:
                        speak("failed to format logical volume due to following reason")
                        print(status[1])

                elif "mount" in command and "logical" in command and "volume" in command:
                    lvpath = input("Enter the logical volume group name: ")
                    mountDirPath = input("Enter the path of mounted directory: ")
                    status = lvm.mount_logical_volume(mountDirPath, lvpath)
                    if status[0] == 0:
                        speak("logical volume has been mounted successfully")
                        print(status[1])
                    else:
                        speak("failed to mount logical volume due to following reason")
                        print(status[1])

                elif "extend" in command and "logical" in command and "volume" in command:
                    vgname = input("Enter the volume group name: ")
                    lvname = input("Enter the logical volume name: ")
                    size = input("Enter the size in of new partition in GB: ")
                    status = lvm.extend_logical_volume(vgname, lvname, size)
                    if status[0] == 0:
                        speak("logical volume has been extended successfully")
                        print(status[1])
                    else:
                        speak("failed to extend logical volume due to following reason")
                        print(status[1])

                elif "unmount" in command and ("logical" in command or "volume" in command):
                    mountDirPath = input("Enter the enter the path of mounted directory: ")
                    status = lvm.umount_logical_volume(mountDirPath)
                    if status[0] == 0:
                        speak("logical volume has been unmounted successfully")
                        print(status[1])
                    else:
                        speak("failed to unmount logical volume due to following reason")
                        print(status[1])

            elif "hadoop" in query:
                print("""
                1. Configure Namenode
                2. Configure Datanode
                3. Start Namenode
                4. Stop Namenode
                5. Start Datanode
                6. Stop Datanode
                7. Cluster Report
                """)
                speak("speak one of the following commands to execute the hadoop operations")

                command = None
                while command == None:
                    command = ai.takeCommand()
                command = command.lower()
                if "configure" in command and ("name node" in command or "namenode" in command):
                    host = int(input('localhost(0)  remote(1): '))
                    namenode_ip = input("enter the name node ip: ")
                    namenode_dir_name = input("enter the name node directory name:")
                    namenode_password = input("enter the name node password: ")
                    status = hadoop.namenode_configuration(namenode_ip, namenode_dir_name, namenode_password
                                                           host)
                    speak("Configuring...")
                    if status[0] == 0:
                        speak("configured data node successfully")
                        print(status[1])
                    else:
                        speak("failed to configure name node due to following reason.")

                elif "configure" in command and "data node" in command:
                    host = int(input('localhost(0)  remote(1): '))
                    namenode_ip = input("enter the name node ip: ")
                    datanode_ip = input("enter the data node ip: ")
                    datanode_dir_name = input("enter the data node directory name: ")
                    datanode_password = input("enter the data node password: ")
                    status = hadoop.datanode_configuration(namenode_ip, datanode_ip, datanode_dir_name,
                                                           datanode_password, host)
                    speak("Configuring...")
                    if status[0] == 0:
                        speak("configured data node successfully")
                        print(status[1])
                    else:
                        speak("failed to configure data node due to following reason.")
                        print(status[1])

                elif "start" in command and "name node" in command:
                    host = int(input('localhost(0)  remote(1): '))
                    namenode_ip = input("enter the name node ip: ")
                    namenode_password = input("enter the name node ip password: ")
                    status = hadoop.namenode_start(namenode_ip, namenode_password, host)
                    speak("Starting name node")
                    if status[0] == 0:
                        speak("name node has been started successfully")
                        print(status[1])
                    else:
                        speak("failed to start the name node due to following reason.")
                        print(status[1])

                elif "stop" in command and "name node" in command:
                    host = int(input('localhost(0)  remote(1): '))
                    namenode_ip = input("enter the name node ip: ")
                    namenode_password = input("enter the name node ip password: ")
                    status = hadoop.namenode_stop(namenode_ip, namenode_password, host)
                    speak("stopping name node")
                    if status[0] == 0:
                        speak("name node has been stopped successfully")
                        print(status[1])
                    else:
                        speak("failed to stop name node due to following reason.")
                        print(status[1])

                elif "start" in command and "data node" in command:
                    host = int(input('localhost(0)  remote(1): '))
                    datanode_ip = input("enter the data node ip: ")
                    datanode_password = input("enter the data node ip password: ")
                    status = hadoop.datanode_start(datanode_ip, datanode_password, host)
                    speak("Starting data node")
                    if status[0] == 0:
                        speak("data node has been started successfully")
                        print(status[1])
                    else:
                        speak("failed to start the data node due to following reason.")
                        print(status[1])

                elif "stop" in command and "data node" in command:
                    host = int(input('localhost(0)  remote(1): '))
                    datanode_ip = input("enter the data node ip: ")
                    datanode_password = input("enter the data node ip password: ")
                    status = hadoop.namenode_stop(datanode_ip, datanode_password, host)
                    speak("stopping data node")
                    if status[0] == 0:
                        speak("data node has been stopped successfully")
                        print(status[1])
                    else:
                        speak("failed to stop data node due to following reason.")
                        print(status[1])

                elif "cluster" in command and "report" in command:
                    status = hadoop.check_report()
                    speak("displaying cluster report")
                    if status[0] == 0:
                        print(status[1])
                    else:
                        speak("failed to display cluster report due to following reason.")
                        print(status[1])

            elif "amazon" in query and "web" in query and "service" in query:
                print("""
                1. AWS Authentication
                2. Create Key Pair
                3. Launch EC2 Instance
                4. Create Security Group
                5. Create Volume
                6. Attach Volume
                7. Add S3
                8. exit 
                """)
                speak("speak one of the following commands to execute the amazon web services operations")
                while (True):
                    command = None
                    while command == None:
                        command = ai.takeCommand()
                    command = command.lower()
                    if "key" in command:
                        key_name = input("Enter a key name : ")
                        status = aws.create_key_pair(key_name)
                        #if status[0] == 0:
                        speak("Key Pair Created")
                        print(status)
                        #else:
                        #    speak("Failed to create a Key Pair")
                        #    print(status[1])

                    elif "launch" in command and "instance" in command:
                        size = input("Enter size : ")
                        key_name = input("Enter the key name to use : ")
                        security_grp_name = input("Enter the Security Group name to use : ")
                        status = aws.launch_ec2_instance(size,"ami-0e306788ff2473ccb",key_name,security_grp_name,"t2.micro")
                        #if status[0] == 0:
                        speak("The EC2 instance has been launched successfully")
                        print(status)
                        """
                        else:
                            speak("Failed to launch the ec2 instance")
                            print(status[1])"""
                
                    elif "security" in command and "group" in command:
                        security_grp_name = input("Enter a Security Group name : ")
                        description = input("Put a description for the Security Group : ")
                        status = aws.create_security_group(security_grp_name,description)
                        #if status[0] == 0:
                        speak("The Security Group has been created successfully")
                        print(status)
                        """
                        status = aws.launch_ec2_instance("ami-0e306788ff2473ccb", key_name, security_grp_name,
                                                         "t2.micro")
                        if status[0] == 0:
                            speak("The EC2 instance has been launched successfully")
                            print(status[1])
                        else:
                            speak("Failed to launch the ec2 instance")
                            print(status[1])

                    elif "security" in command and "group" in command:
                        security_grp_name = input("Enter a Security Group name : ")
                        description = input("Put a description for the Security Group : ")
                        status = aws.create_security_group(security_grp_name, description)
                        if status[0] == 0:
                            speak("The Security Group has been created successfully")
                            print(status[1])
                        else:
                            speak("Failed to create The Security Group")
                            print(status[1])"""

                    elif "create" in command and "volume" in command:
                        AZ = input("Enter the Availability Zone : ")
                        size = input("Enter the size of the volume : ")
                        status = aws.create_volume(AZ,size,"gp2")
                        #if status[0] == 0:
                        speak("The volume has been created successfully")
                        print(status)
                        """
                        else:
                            speak("Failed to create volume")
                            print(status[1])"""
                
                    elif "attach" in command and "volume" in command:
                        instance_id = input("Enter the instance id to attach with : ")
                        volume_id = input("Enter the volume id : ")
                        status = aws.attach_volume(instance_id,volume_id)
                        #if status[0] == 0:
                        speak("The volume has been attached successfully to the instance")
                        print(status)
                        """
                        else:
                            speak("Failed to attach volume")
                            print(status[1])"""
                
                    elif "add" in command or "s3" in command:
                        bucket_name = input("Enter a bucket name : ")
                        region = input("Enter the region : ")
                        status = aws.s3_addition(bucket_name,region)
                        #if status[0] == 0:
                        speak("The s3 has been added successfully")
                        print(status)
                        """
                        else:
                            speak("Failed to add s3")
                            print(status[1])"""



            elif "prediction" in query:
                print("""
                 Salary Prediction
                """)
                speak("enter the years of experience to perform the salary prediction")
                #
                # command = None
                # while command == None:
                #     command = ai.takeCommand()
                # command = command.lower()
                if  "prediction" in query:
                    exp = input("Enter the experience in years: ")
                    speak("here is the value of predicted salary")
                    print("Predicted Salary: ", sal.sal_est(exp))
                elif "exit" in query:
                    speak("returning to main menu")
                    break

    if user_option == 2:
        print("-----Configure and create your AI profile-----")
        userId = input("enter your username Id: ")
        passwd = input("enter the password: ")
        name = input("Enter your name: ")
        while (True):
            voice = input("Which voice would you like to choose for AI (Male or Female): ").lower()
            if voice == "male":
                voice_code = 0
                break
            elif voice == 'female':
                voice_code = 1
                break
            else:
                print("Type male or female.")
                continue
        profile_manager.create_profile(userId, passwd, name, voice)
