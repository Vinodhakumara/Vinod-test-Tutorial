import os
print('THIS PROGRAM HELPS US TO RUN ,OPEN ALL FOLDERS,FILES,APPS,SETTINGS,CREATES file,DELETES file for windows\n')
while True:
    print("Chat with me with your requirments : ",end="");
    p = input().lower()
#   Start/Run Chrome
    if(('not' not in p) and ('don\'t' not in p)and ('nt' not in p) and ('dont' not in p) and ('never' not in p) and ('nvr' not in p) and ('n\'t' not in p) and ('dnt' not in p) and ('rename' not in p) and ('change' not in p) and ('edit file name' not in p) and ('edit folder name' not in p)) and ('open' in p or ('opn' in p) or 'run' in p or ('exicute' in p) or ('execute' in p)) and (("chrome" in p or ('chrom' in p)) or ('google' in p or ('googl' in p) or ('internet' in p))):  
        os.system('start chrome')
        print('Chrome opened\n')
#   Start/run notepad
    elif(('not' not in p) and ('don\'t' not in p)and ('nt' not in p) and ('dont' not in p) and ('never' not in p) and ('nvr' not in p) and ('n\'t' not in p) and ('dnt' not in p) and ('rename' not in p) and ('change' not in p) and ('edit file name' not in p) and ('edit folder name' not in p)) and ('open' in p or ('opn' in p) or 'run' in p or ('exicute' in p)or ('execute' in p)) and (("notepad" in p or ('editor' in p)) or ('edtr' in p or ('ntpd' in p) )):  
        os.system('start notepad')
        print('Notepad opened\n')
#   Start/run VScode
    elif(('not' not in p) and ('don\'t' not in p)and ('nt' not in p) and ('dont' not in p) and ('never' not in p) and ('nvr' not in p) and ('n\'t' not in p) and ('dnt' not in p) and ('rename' not in p) and ('change' not in p) and ('edit file name' not in p) and ('edit folder name' not in p)) and ('open' in p or ('opn' in p) or 'run' in p or ('exicute' in p)or ('execute' in p)) and (("vsode" in p or ('visualstudiocode' in p)) or ('visual studio code' in p or ('code' in p) or ('vs code' in p))):  
        os.system('start code')
        print('VScode opened\n')
#   Start/run MSword
    elif(('not' not in p) and ('don\'t' not in p)and ('nt' not in p) and ('dont' not in p) and ('never' not in p) and ('nvr' not in p) and ('n\'t' not in p) and ('dnt' not in p) and ('rename' not in p) and ('change' not in p) and ('edit file name' not in p) and ('edit folder name' not in p)) and ('open' in p or ('opn' in p) or 'run' in p or ('exicute' in p)or ('execute' in p)) and (("chrome" in p or ('chrom' in p)) or ('winword' in p or ('ms word' in p)or ('ms-word' in p) or ('msword' in p) or ('microsoftword' in p) or ('microsoft word' in p) or ('office word' in p))):  
        os.system('start winword')
        print('MSword opened\n')
#   Start/run dev-cpp
    elif(('not' not in p) and ('don\'t' not in p)and ('nt' not in p) and ('dont' not in p) and ('never' not in p) and ('nvr' not in p) and ('n\'t' not in p) and ('dnt' not in p) and ('rename' not in p) and ('change' not in p) and ('edit file name' not in p) and ('edit folder name' not in p)) and ('open' in p or ('opn' in p) or 'run' in p or ('exicute' in p)or ('execute' in p)) and (("dev-cpp" in p or ('dev-c++' in p)) or ('cpp editor' in p or ('c++ editor' in p)or ('devc++' in p))) :  
        os.system('start div-c++')
        print('DivStarted\n')
#   Start/run MS-Photos
    elif(('not' not in p) and ('don\'t' not in p)and ('folder'not in p) and ('file'not in p) and ('fldr' not in p) and ('fle' in p) and ('nt' not in p) and ('dont' not in p) and ('never' not in p) and ('nvr' not in p) and ('n\'t' not in p) and ('dnt' not in p) and ('rename' not in p) and ('change' not in p) and ('edit file name' not in p) and ('edit folder name' not in p)) and ('open' in p or ('opn' in p) or 'run' in p or ('exicute' in p)or ('execute' in p)) and (("photos" in p or ('gallery' in p)) or ('images' in p or ('image' in p)or ('photo' in p) or ('ms-images' in p) or ('msimages' in p) or ('ms-photos' in p) or ('microsoftimages' in p) or ('microsoft images' in p) or ('microsoft-images') or ('msphotos' in p) or ('microsoftphotos' in p) or ('microsoft photos' in p) or ('microsoft-photos' in p)) ):  
        os.system('start ms-photos:')
        print('MS-photos opened\n')
#   creating a new folder
    elif(('not' not in p)and ('rename' not in p) and ('change' not in p) and ('edit file name' not in p) and ('edit folder name' not in p) and ('don\'t' not in p)and ('nt' not in p) and ('dont' not in p) and ('never' not in p) and ('nvr' not in p) and ('n\'t' not in p) and ('dnt' not in p) and ('open' not in p or ('opn' not in p))) and ("create" in p or ('new' in p) or ('add' in p)) and ("folder" in p):
        folderName = input('Enter new folder name :')
        os.system('mkdir '+folderName)
#   Deleting a existing folder
    elif(('not' not in p)and ('rename' not in p) and ('change' not in p) and ('edit file name' not in p) and ('edit folder name' not in p) and ('don\'t' not in p)and ('nt' not in p) and ('dont' not in p) and ('never' not in p) and ('nvr' not in p) and ('n\'t' not in p) and ('dnt' not in p)) and ('remove' in p or ('rmv' in p) or ('delete' in p) or ('dlt' in p) or ('destroy' in p) or ('cut out' in p) or ('cutout' in p) or ('take out' in p) or ('takeout' in p) or ('erase' in p) or ('dispatch' in p)) and (("folder" in p or ('fldr' in p)) or ('file' in p or ('fle' in p))): 
        os.system('dir')
        removeFolder = input('Make sure deleting file name and reenter name:')
        os.system('rmdir '+removeFolder)
#   Open a folder which existing already
    elif(('not' not in p) and ('don\'t' not in p)and ('nt' not in p) and ('dont' not in p) and ('never' not in p) and ('nvr' not in p) and ('n\'t' not in p) and ('dnt' not in p) and ('rename' not in p) and ('change' not in p) and ('edit file name' not in p) and ('edit folder name' not in p)) and ('open' in p or ('opn' in p) or 'run' in p or ('exicute' in p)) and (("folder" in p or ('fldr' in p)) or ('file' in p or ('fle' in p))):  
        os.system('dir')
        openFolder = input('Enter a folder Name from above list to open a folder:')
        os.system('start '+openFolder)	
#   Change folder or file name  
    elif(('not' not in p) and ('don\'t' not in p)and ('nt' not in p) and ('dont' not in p) and ('never' not in p) and ('nvr' not in p) and ('n\'t' not in p) and ('dnt' not in p))and('rename' in p or ('change' in p) or ('edit file name' in p) or ('edit folder name' in p) or ('modify file name' in p) or ('modify folder name' in p)) and ('folder' in p or 'file' in p):
        folderNameToChange = input('Enter a folder name to change:')
        folderNewName = input('Enter new name to a folder:')
        os.system('rename '+folderNameToChange+' '+folderNewName)
#   Open windows settings
    elif(('not' not in p) and ('don\'t' not in p)and ('nt' not in p) and ('dont' not in p) and ('never' not in p) and ('nvr' not in p) and ('n\'t' not in p) and ('dnt' not in p)) and ('open' in p or ('opn' in p)) and (("settings" in p or ('sttg' in p) or "setting" in p or ('sttgs' in p) or 'stgs' in p)):  
        os.system('start ms-settings:')
        print('settings opned\n')
#   Exit 
    elif(('not' not in p) and ('don\'t' not in p)and ('nt' not in p) and ('dont' not in p) and ('never' not in p) and ('nvr' not in p) and ('n\'t' not in p) and ('dnt' not in p))and('exit' in p or 'leave' in p or 'come out' in p):
        print('exited program\n')
        break
#   Don't support a chat
    else:
        print("don't support")