import requests
import random
import time
import threading
import json


print("""
  ________.__         __   .__  __    _________                        __                
 /  _____/|__| _____ |  | _|__|/  |_  \_   ___ \_______   ____ _____ _/  |_  ___________ 
/   \  ___|  |/     \|  |/ /  \   __\ /    \  \/\_  __ \_/ __ \\__  \\   __\/  _ \_  __ \
\    \_\  \  |  Y Y  \    <|  ||  |   \     \____|  | \/\  ___/ / __ \|  | (  <_> )  | \/
 \______  /__|__|_|  /__|_ \__||__|    \______  /|__|    \___  >____  /__|  \____/|__|   
        \/         \/     \/                  \/             \/     \/                  
""")

print("By Alek#0001")

email_gen = input("Custom Email Names? (Y/N)")
if email_gen == "Y":
    final_email = input("Email Prefix: ") + namegen() + "@gmail.com"
if email_gen == "N":
    final_email = namegen() + "@gmail.com
if email_gen == "y":
    final_email = input("Email Prefix: ") + namegen() + "@gmail.com"
if email_gen == "n":
    final_email = namegen() + "@gmail.com
    
tokenFile = open("Teacher/[Results]/tokens.txt", "w")
idFile = open("Teacher/[Results]/ids.txt", "w")
comboFile = open("Teacher/[Results]/combos.txt", "w")
prefix = input("Account Names: ")
last_prefix = input("Account Last Names: ")


def namegen():
    length = random.randint(7, 15) #set your min and max (min, max)
    eval = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
    "S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0",""


    return ''.join(random.choice(eval) for i in range(length))

def SignUp():
    link = "https://www.gimkit.com/api/register"
    email = namegen() + "@gmail.com"
    pass_gen = "AlekCodes" + namegen()
    data = {
    "accountType": "educator",
    "areaOfExpertise": "Communications",
    "bulkSubscriptionToJoin": "",
    "country": "US",
    "dateOfBirth": "",
    "districtId": "",
    "email": final_email,
    "firstName": prefix,
    "googleToken": "",
    "gradeLevel": "High School",
    "groupJoining": "",
    "guardianEmail": "",
    "lastName": last_prefix,
    "organization": "",
    "password": pass_gen,
    "schoolId": ""
    }
    signup = requests.post(link,data)
    token = json.loads(signup.text)
    tokenFile.write(token['token']+ "\n")
    id = json.loads(signup.text)
    idFile.write(id['_id']+ "\n")
    comboFile.write(final_email + ":" + pass_gen + "\n")
    print(signup.text)
   
threads=[]


for i in range(100000):
  t = threading.Thread(target = SignUp)
  t.Daemon = True
  threads.append(t)

for i in range(100000):
  threads[i].start()
  time.sleep(0.2)

for i in range(100000):
  threads[i].join()
