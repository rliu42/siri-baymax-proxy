from SiriBaymax.SiriBaymax import *

SiriBaymax = SiriBaymax("icloud_user", "apple_pw", "http://72.29.29.198:1337/")

SiriBaymax.connect() #Connect to iCloud

input("Baymax listening on Siri. Press any key to close connection...\n")
SiriBaymax.disconnect()