from win32gui import GetWindowText, GetForegroundWindow
from time import sleep
from getpass import getuser
import os
import re
from datetime import datetime
import json
from commitChanges import commitActivity


tags = [
    # one-tags that must be tracked
    # if the index is an array, the first index is the word to be matched 
    # and the second is the one to be shown
    "python", ["py", "python"], "java", "selenium", "javascript", ["js", "javascript"], 
    "flutter", "bootstrap", "spring", ["nlp", "natural language processing"], "flask",
    ["pln", "natural language processing"], "html", "css", "git", "django",
    "github", "react", "angular", "linkedin", "json", ["ts", "typescript"],
    
]

multiTags = [
    "visual studio code", "stack overflow", "natural language processing", "tensor flow" 
]

def checkForIntelliJ():
    # appends to the tracked list the name of the projects from your IntelliJ folder
    # if positive, the name shown will be "IntelliJ" instead of the project's name
    user = getuser()
    path = f"C:/Users/{user}/IdeaProjects" # Default IntelliJ project folder
    for p in os.listdir(path):
        if os.path.isdir(f"{path}/{p}"):
            tags.append([p, "IntelliJ"])


def checkForTags(title):
    # checks if the title of the window has matching tags
    # will append a value only one time, no repetition
    # multi-word tags required context so they are checked before chopping the title
    # one-word tags require precision so they are checked after chopping the title
    matches = []
    title = title.lower()

    for mtag in multiTags:
        if mtag in title:
            matches.append(mtag)

    title = re.split(r'[, .:]', title)

    for tag in tags:
        if type(tag) == str:
            tag = [tag, tag]
        if tag[0] in title and tag[1] not in matches:
            matches.append(tag[1])
        
    return matches


def getFocus():
    windowTitle = GetWindowText(GetForegroundWindow()) # gets the currently focused window's title
    tags = checkForTags(windowTitle)
    return tags # extracts data from the title


def writeAcitivity(tags, time):
    try:
        with open("activity.json", "r") as activity:
            data:dict = json.load(activity)
    except:
        data = {}

    for tag in tags:
        tag = re.sub(" ", "_", tag)
        hours = data.get(tag) # int or None
        if not hours:
            hours = 0
        data[tag] = hours + time

    result = json.dumps(data, indent=4)

    with open("activity.json", "w") as activity:
        activity.write(result)


checkForIntelliJ()
lastcommit = datetime.now()

while True:

    # the current window's data (tags) is extracted
    # and the current time is stored in "start"
    # the program sleeps until the program identifies changes in the tags
    # and then it writes the tags and how much time in hours they have been positive 
    # commit changes every 5 hours

    current = getFocus()
    start = datetime.now()
    sleep(5)
    
    while current == getFocus():
        sleep(5)
    
    elapsed = datetime.now() - start 
    elapsed = (elapsed.total_seconds())/3600
    
    writeAcitivity(current, elapsed)

    if ((datetime.now() - lastcommit).total_seconds()/3600) >= 5:
        commitActivity()

     