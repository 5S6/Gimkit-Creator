from os import name
import requests
import random
import time
import threading
import json

tokenFile = open("Student/[Results]/tokens.txt", "w")
idFile = open("Student/[Results]/ids.txt", "w")
comboFile = open("Student/[Results]/combos.txt", "w")

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
    "accountType": "student",
    "areaOfExpertise": "",
    "bulkSubscriptionToJoin": "",
    "country": "",
    "dateOfBirth": "",
    "districtId" : "" ,
    "email": email,
    "firstName": namegen(),
    "googleToken": "",
    "gradeLevel": "",
    "groupJoining": "61c3dbf9751f6800233d78fa",
    "guardianEmail": "",
    "lastName": "r",
    "organization": "",
    "password": pass_gen,
    "schoolId": ""
    }
    signup = requests.post(link,data)
    print(signup.text)
    token = json.loads(signup.text)
    tokenFile.write(token['token']+ "\n")
    id = json.loads(signup.text)
    idFile.write(id['_id']+ "\n")
    comboFile.write(email + ":" + pass_gen + "\n")

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
