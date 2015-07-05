from SiriBaymax.SiriBaymax import *

host = "http://72.29.29.198:1337/"

SiriBaymax = SiriBaymax("iCloud_user", "iCloud_pass", host)

SiriBaymax.connect() #Connect to iCloud

input("Baymax listening on Siri at " + host + ". Press any key to close connection...\n")
SiriBaymax.disconnect()