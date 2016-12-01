import requests
import json
import webbrowser

 #API TO FIND DETAIL OF USER/COMPANY

cond=True
while(cond): 
 print("Trending repo\n")
 lang = raw_input("enter the language to search trending repo on the basis of language ")
 if(lang!=""):

     s  = requests.get("https://api.github.com/search/repositories?q=stars:>0+language:"+lang)
 else:
      s  = requests.get("https://api.github.com/search/repositories?q=stars:>0")
 
 if s.status_code!=200:
 	print("Doesn't exsit")
 else:
     #Parsing JSON so it can be can be used as a dictionary
      print("Trending repo\n")
      parsed_json = json.loads(s.text)
      x = (parsed_json["items"])
      for i in x:
          print("REPO: %s, Language: %s"%(i["name"],i["language"]))
      choice= raw_input("want description of repo y or n ")
      if choice=='y':

          desc = raw_input("enter repo name to get description ")
          for i in x:
              if i["name"]==desc:
                 print(i["description"])
                 print("DETAILS ABOUT USERS\n")
                 users = json.loads((requests.get(i["url"])).text)
                 print("StrangersCount = %s watchers_count: %s Subscriber_Count: %s \n"%(users["stargazers_count"],users["watchers_count"],users["subscribers_count"]))
                 c = raw_input("want to open page y or n \n")
                 if c =='y':
                    webbrowser.open((i["html_url"]))
	
                  
                            
 option = raw_input("want to continue y or n ")
 if(option=='n'):
     cond = False      
