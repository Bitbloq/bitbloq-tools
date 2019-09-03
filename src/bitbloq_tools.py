import json
from os import listdir, system
from os.path import isfile, join
import random
import string
import webbrowser

message = ["","Merge your life", "We love JSONs", "Make the difference"]

def remove_char(s):
    return s[ 1:len(s) - 1]

def change(id):
    while(True):
        newId = id[0:len(id) - 1] + str(random.randint(0,10000))
        if not newId in originIDs:
            originIDs.append(newId)
            return newId
#Show menu options
system('clear')
print("Tools:")
print("1 - Merger")
print("2 - Prettify")
print("3 - Change name")
#Ask the users
print("\r\n")
tool = int(input("Choose a tool: "))

#Read files
onlyfiles = [f for f in listdir("./") if isfile(join("./", f))]
#Show files
system('clear')
print(message[tool])
index = 0
for file in onlyfiles:
    print(str(index) + " - " + file);
    index += 1

if tool == 1:
    #Ask the user
    print("\r\n")
    baseFile = int(input("Choose a base file: "))
    contentFile = int(input("Choose a secondary file: "))
    nameFlag = str(raw_input("Use base file name for the merge file? y/n: ") )
    if nameFlag == "y":
        name = onlyfiles[baseFile].split(".")[0]
    else:
        name = str(raw_input("New name: ") )

    originIDs = []
    new = {}
    contents = []

    #Open base file
    with open(onlyfiles[baseFile]) as json_file:
        data = json.load(json_file)
        new = data
        contents = json.loads(data["content"])
        #Get all parents ids
        for o in contents:
            originIDs.append(o["id"])

    #Open secondary file
    with open(onlyfiles[contentFile]) as json_file:
        data = json.load(json_file)
        secondaryContents = json.loads(data["content"])
        #Verify first level IDs
        for o in secondaryContents:
            #Change the id if it is repeated
            if o["id"] in originIDs:
                local = o
                local["id"] = change(local["id"])
                contents.append(o)
            else:
                contents.append(o)

    #Append content to new file and change the document title
    new["content"] = json.dumps(contents)
    new["title"] = name
    #Save the new file
    with open(name + '.3d.bitbloq', 'w') as outfile:
        json.dump(new, outfile)

elif tool == 2:
    #Ask the user
    print("\r\n")
    baseFile = int(input("Choose the file: "))

    #Read the file
    data = {}
    with open(onlyfiles[baseFile]) as json_file:
        data = json.load(json_file)
        #Format the content string
        content = data["content"]
        data["content"] = json.loads(content)

    #print(json.dumps(data, indent=4, sort_keys=True));

    #Change document title and file name
    data["title"] = data["title"] + "_pretty"
    name = onlyfiles[baseFile].split(".")[0] + "_pretty.json"
    #Save the document as JSON
    with open(name, 'w') as outfile:
        json.dump(data, outfile)

    #Open the webbrowser
    chrome_path = '/usr/bin/google-chrome %s'
    file_path = "./" + name
    webbrowser.get(chrome_path).open(file_path)
    print("\r\nOpening in Google Chrome. Remember to install a JSON viewer in Chrome.");

elif tool == 3:

    baseFile = int(input("Choose the file: "))
    name = str(raw_input("New name: "))

    #Read the file
    data = {}
    with open(onlyfiles[baseFile]) as json_file:
        data = json.load(json_file)
        data["title"] = name

    with open(name + '.3d.bitbloq', 'w') as outfile:
        json.dump(data, outfile)
