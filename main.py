
from Features.ai_features import Ai_Features
from database.profile_manager import Profile_Manager


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
        ai = Ai_Features(0)
        while (True):
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
