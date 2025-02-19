from win32gui import GetWindowText, GetForegroundWindow, GetClassName
from time import sleep
from getpass import getuser
import os


tracked = [
#   (title in window, title to be shown if positive)
    ["Visual Studio Code"],
    ["Stack Overflow - Brave", "Stack Overflow"],
    ["Linkedin"],
    ["Command Prompt"],
    ["GitHub Desktop", "GitHub"]
]


tags = [
    # tags that must be tracked
    # if the index is an array, the first index is the word to be matched 
    # and the second is the one to be shown
    "python", ["py", "python"], "java", "selenium", "javascript", ["js", "javascript"], "django", "flask",
    "flutter", "bootstrap", "spring", ["nlp", "natural language processing"], "html", "css", "git",
    "github", "react", "angular"
]


def checkForIntelliJ():
    # appends to the tracked list the name of the projects from your IntelliJ folder
    # if positive, the name shown will be "IntelliJ" instead of the project's name
    user = getuser()
    path = f"C:/Users/{user}/IdeaProjects" # Default IntelliJ project folder
    for p in os.listdir(path):
        if os.path.isdir(f"{path}/{p}"):
            tracked.append([p, "IntelliJ"])


def checkByTitle(title: str):
    # checks every index of tracked list
    # sees if the end of the title matches with the tracked title
    # returns the show title if positive
    # returns False if the title didnt match any of the tracked titles
    for t in tracked:
        if title.startswith(t[0]) or title.endswith(t[0]):
            if len(t) == 2:
                return t[1]
            else:
                return t[0]
    return False


def checkForTags(title):
    # checks if the title of the window has matching tags
    # will append a value only one time, no repetition
    # if the matching tag is a list, the second index will be append if the first index is positive
    # returns a list of tags that matched
    matches = []
    for tag in tags:
        if type(tag) == str:
            if tag in title.lower():
                matches.append(tag)
        else:
            if tag[0] in title.lower() and tag[1] not in matches:
                matches.append(tag[1])
    return matches


def getFocus():
    windowTitle = GetWindowText(GetForegroundWindow()) # gets the currently focused window's title
    showTitle = checkByTitle(windowTitle)
    tags = checkForTags(windowTitle)
    return showTitle, tags # extracts data from the title


checkForIntelliJ()
