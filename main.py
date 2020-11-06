from Features.ai_features import Ai_Features
from database.profile_manager import Profile_Manager
import Features.Docker_operations as docker


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
        ai = Ai_Features
        while (True):
            print("Here are the features of the Saha Assistent")
            print("1. create patitions")
            print("2. configure hadoop cluster")
            print("3. docker operations")
            print("4. Aws commands")

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
                speak one of the following commands to execute the docker operations
                1. Check available images
                2. Launch a Container
                3. stop a running container
                4. Relaunch a Stopped container
                5. Show corrently Running Container
                6. Delete all containers
                """)
                print()
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
                    if status[0] == 0:
                        print("container has been stopped successfuly")
                        print(status[1])
                    else:
                        print("failed to stop the container")
                        print(status[1])

                elif "relaunch a stopped container" in command:
                    osname = input("Enter the Container name for your OS: ")
                    status = docker.run_prelaunched_container(osname)
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
