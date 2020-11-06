from time import sleep
from database.database_manager import Database_Manager
import mysql


class Profile_Manager():
    def authentication(self, user_id, passwd):
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
                if data.split()[2] == passwd and data.split()[1] == user_id:
                    return True
                else:
                    return False
            else:
                return False

    def create_profile(self, user, passwd, name, v_code):
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
            fp.write(name + " " + user + " " + passwd + "\n")
            fp.close()
            print("Configuring voice setting...")
            sleep(1)
            fp = open("database/voice_settings.txt", "a")
            fp.write(name + " " + str(v_code) + "\n")
            fp.close()
            sleep(1)
            print("profile created")
        except Exception as e:
            print("profile not created")
