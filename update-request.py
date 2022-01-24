#Made By Blake McCullough
#Discord - Spoiled_Kitten#4911
#Github - https://github.com/Blake-McCullough/
#Email - privblakemccullough@protonmail.com

#Server is run by python -m http.server
from datetime import datetime #Gets the date and time
from ensurepip import version #Decoding import
import urllib.request # the lib that handles the url stuff

def UpdatePackages(serveraddress):
    #Makes the address and path for the latest version file to be opened
    url = serveraddress +'/latestversion.txt'
    data = urllib.request.urlopen("") # it's a file like object and works just like a file
    

    for line in data:
        version = line
    data.close()
    #decodes the line from binary so it can be read correctly
    latestversion = version.decode()
    #opens the current version (aka what the current mirror is) in read so that it can just view the file, but not edit
    current_version = open("/etc/pacman.d/mirrorlist", "r") #To test if it works properly
    #Reads the current version from the file
    for line in current_version:
        currentversion = line
    current_version.close() 
    #If the current mirror server is the same as in the latestversion.txt
    if currentversion != latestversion:
        #opens the current version (aka what the current mirror is) so it can edit the file
        current_version = open("/etc/pacman.d/mirrorlist", "w")
        current_version.write(latestversion)
        current_version.close()
        updatelog = open("updatelog.txt", "a")
        #Gets current time
        now = datetime.now() 
        timenow = now.strftime("%d/%m/%Y %H:%M:%S")
        #Adds to a log with the time for admins to view what happens, in case of an error
        log =timenow+"-  updated to the latest version for the packages:"+latestversion+"\n"
        updatelog.write(log)
        updatelog.close()

    else:
        updatelog = open("packageupdatelog.txt", "a")
        #Gets current time
        now = datetime.now()
        timenow = now.strftime("%d/%m/%Y %H:%M:%S")
        #Adds to a log with the time for admins to view what happens, in case of an error
        log =timenow+"-  No Update was necessary for the packages\n"
        updatelog.write(log)
        updatelog.close()






#Prevents running if imported

if __name__ == "__main__":
    #Set this to whatever the server address is (for the updating of packages)
    UpdatePackages('DOMAIN/IPADDRESS')

       