from playsound import playsound
import time
import json
import getpass


# Important Concept for better Viewing Experience .. 
CLEAR = "\033[2J"   #clear screen
CLEAR_AND_RETURN = "\033[H"   #view on the same line
DOT = "."


class Alarm:

    def __init__(self,database):
        self.database = database

    def maine(self):
         
        minutes = int(input("Enter MINUTES after which u want ur alarm to ring : "))
        seconds = int(input("Enter SECONDS after which u want ur alarm to ring : "))
        total_time = minutes*60 + seconds
        time_elapsed = 0
        
        print(CLEAR)
        while time_elapsed < total_time:
            time.sleep(1)
            time_elapsed += 1

            time_left = total_time - time_elapsed
            minutes_left = time_left // 60
            seconds_left = time_left % 60

            print(f"{CLEAR_AND_RETURN}Alarm will sound in : {minutes_left:02d} : {seconds_left:02d}")
            
        print("\n")

        print(CLEAR)
        print("WAKE UP ........... ")

        playsound("alarm.mp3")

        print(CLEAR)

    def login(self):

        user = input("Enter Username : ")
        passwd = getpass.getpass("Enter Password : ")
        print(CLEAR)
        for j in range(1,11):
            time.sleep(1)
            print(f"{CLEAR_AND_RETURN}Verifying ( {DOT*j} ) {j*10} %")
        print()

        length = len(self.database['user_data'])

        for i in range(length):
            if (self.database['user_data'][i]['username'] == user) and \
                (self.database['user_data'][i]['password'] == passwd):
                    print(CLEAR)
                    print(f"User Logged In ......... - {user}")
                    time.sleep(2)
                    return self.passe()

        print("Access Denied ... ") 
        return self.fail()
    
    def fail(self):
        return False
    
    def passe(self):
        return self.maine()

        

if __name__ == "__main__":
    
    with open("database.json", "r") as read_file:
            data = json.load(read_file)
    alarm = Alarm(data)
    alarm.login()