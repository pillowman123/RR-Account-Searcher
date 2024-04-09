import requests, json, time, colorama


usernameInput = input("username: ")


api = "https://apim.rec.net/accounts/account?username="
apiLink = (api + usernameInput)
GetInfo = requests.get(apiLink)

MyCrappyAssData = GetInfo.json()

accountId = MyCrappyAssData["accountId"]
username = MyCrappyAssData["username"]
displayName = MyCrappyAssData["displayName"]
profileImage = MyCrappyAssData["profileImage"]
isJunior = MyCrappyAssData["isJunior"]
platforms = MyCrappyAssData["platforms"]
personalPronouns = MyCrappyAssData["personalPronouns"]
identityFlags = MyCrappyAssData["identityFlags"]
createdAt = MyCrappyAssData["createdAt"]

if GetInfo.status_code == 200:
    
    colorama.init()
    
    print(colorama.Fore.GREEN, "Api Link:", apiLink)
    print(colorama.Fore.GREEN, "Account ID: ", accountId)
    print(colorama.Fore.GREEN, "Username: ", username)
    print(colorama.Fore.GREEN, "Display Name: ", displayName)
    print(colorama.Fore.GREEN, "Profile Image:" , profileImage)
    print(colorama.Fore.GREEN, "Is Juinored: ", isJunior)
    print(colorama.Fore.GREEN, "Personal Pronoun Count: ", personalPronouns)
    print(colorama.Fore.GREEN, "Identity Flag Count: ", identityFlags)
    print(colorama.Fore.GREEN, "Created At: ", createdAt)
    print("")
    print(colorama.Fore.RED, "Press Enter to Quit")
    input()

    
else:
    print("This username is invalid!")

