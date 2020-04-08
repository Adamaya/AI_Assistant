from time import sleep

from Features.ai_features import Ai_Features


def authentication(user_id, passwd):
    """
    it authenticate the profile of user to provide secured access to AI. If user is authorised then it will return True
    otherwise it will return the False.
    :param user_id: this parameter consists the userId.
    :param passwd: this parameter consists the password.
    :return: method returns a boolean value.
    """
    fp = open("database/profiles.txt", "r")
    credential = fp.readlines()
    fp.close()
    for data in credential:
        if user_id in data:
            if data.split()[1] == passwd and data.split()[0] == user_id:
                return True
            else:
                return False
        else:
            return False


def create_profile(user, passwd, name, v_code):
    """
    This method creates a user profile to access and configure the AI for specific user.
    :param user: this parameter consist the userId.
    :param passwd: this parameter consist the password.
    :param name: this parameter consist the username.
    :param v_code: this parameter consist voice code of ai.
    :return: None
    """
    try:
        print("Creating your Profile....")
        fp = open("database/profiles.txt", "a")
        fp.write("\n" + name + " " + user + " " + passwd)
        fp.close()
        print("Configuring voice setting...")
        sleep(1)
        fp = open("database/voice_settings.txt", "a")
        fp.write("\n" + name + " " + str(v_code))
        fp.close()
        sleep(1)
        print("profile created")
    except Exception as e:
        print("profile not created")


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


while (True):
    print("__Welcome to AI Console__ \n\nUser Login(1)\t\tCreate New Profile(2)")
    user_option = select_in_between_user_login_and_create_profile()
    if user_option == 1:
        print("-----User Login----- ")
        while (True):
            username = input('User Name Id: ')
            password = input('Password: ')
            voice_code = 0
            verified = authentication(username, password)
            if verified:
                # TODO create my_sql database for profile data
                print("Welcome")
                break
            else:
                print("enter the valid username password or create the profile first")
                continue
        ai = Ai_Features(1)
        ai.wishMe()
        while (True):
            query = ai.takeCommand().lower()
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

    if user_option == 2:
        print("----Configure and create your AI profile---")
        user = input("enter your username Id: ")
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
        create_profile(user, passwd, name, voice_code)
