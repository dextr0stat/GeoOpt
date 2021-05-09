import clr 
clr.AddReference('System.Web.Extensions')
from System.Web.Script.Serialization import JavaScriptSerializer
from System.Net import WebClient

#if fetch:
    
#create new web client
client= WebClient()

 #Downoad the results of that URL
results= client.DownloadString(url)

#print these results
a= results