from Features.ai_features import Ai_Features
from database.profile_manager import Profile_Manager
import Features.Docker_operations as docker
from voice.voice_configuration import speak
import Features.lvm as lvm


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
    print("__Welcome to AI Console__ \n\nUser Login(1)\t\tCreate New Profile(2)")
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

            query = None
            while (query == None):
                query = ai.takeCommand()
            query = query.lower()
            if 'wikipedia' in query:
                ai.wikipedia_search(query, 2)

            elif "exit" in query:
                ai.speak("Have a good day!")
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
                while (command == None):
                    command = ai.takeCommand()
                command = command.lower()
                if "check available images" in command:
                    status = docker.check_available_images()
                    if status[0] == 0:
                        print("here are the available images")
                        print(status[1])
                elif "launch a container" in command:
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

                elif "stop a running container" in command:
                    osname = input("Enter the Container name for your OS: ")
                    status = docker.stop_running_container(osname)
                    print("Stopping the container")
                    if status[0] == 0:
                        print("container has been stopped successfuly")
                        print(status[1])
                    else:
                        print("failed to stop the container")
                        print(status[1])

                elif "relaunch a stopped container" in command:
                    osname = input("Enter the Container name for your OS: ")
                    status = docker.run_prelaunched_container(osname)
                    print("Relaunching....")
                    if status[0] == 0:
                        print("container has been relaunched successfuly")
                        print(status[1])
                    else:
                        print("failed to relaunch the container")
                        print(status[1])

                elif "show currently running container" in command:
                    status = docker.show_currently_running_containers()
                    if status[0] == 0:
                        print("here are the running containers")
                        print(status[1])
                    else:
                        print("docker internal error occered")
                        print(status[1])

                elif "delete all containers" in command:
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
                while (command == None):
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
