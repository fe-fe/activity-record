from win32gui import GetWindowText, GetForegroundWindow
from time import sleep
from getpass import getuser
import os
import re

tags = [
    # tags that must be tracked
    # if the index is an array, the first index is the word to be matched 
    # and the second is the one to be shown
    "python", ["py", "python"], "java", "selenium", "javascript", ["js", "javascript"], "django", "flask",
    "flutter", "bootstrap", "spring", ["nlp", "natural language processing"], "html", "css", "git",
    "github", "react", "angular", "linkedin", "stack overflow",
    
]

multiTags = [
    "visual studio code", "stack overflow", "natural language processing" 
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
    # if the matching tag is a list, the second index will be append if the first index is positive
    # returns a list of tags that matched
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


checkForIntelliJ()

i=0
while i < 10:
    print(getFocus())
    i+=1
    sleep(4)