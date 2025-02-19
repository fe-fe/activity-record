from win32gui import GetWindowText, GetForegroundWindow
from time import sleep


tracked = [
#   (title in window, title to be shown if positive)
    ("Visual Studio Code", "Visual Studio Code"),
    ("Stack Overflow - Brave", "Stack Overflow"),
    ("Linkedin", "Linkedin"),
    ("Command Prompt", "Command Prompt"),
    ("GitHub Desktop", "GitHub")
]


tags = [
    # tags that must be tracked
    # if the index is an array, the first index is the word to be matched 
    # and the second is the one to be shown
    "python", ["py", "python"], "java", "selenium", "javascript", ["js", "javascript"], "django", "flask",
    "flutter", "bootstrap", "spring", ["nlp", "natural language processing"], "html", "css", "git",
    "github", "react", "angular"
]


def checkByLengthMatch(title):
    # checks every index of tracked list
    # sees if the end of the title matches with the tracked title
    # returns the show title if positive
    # returns False if the title didnt match any of the tracked titles
    for t in tracked:
        if title[len(title)-len(t[0]):] == t[0]:
            return t[1]
    return False


def checkForTags(title):
    # checks if the title of the window has matching tags
    # will append a value only one time, no repetition
    # if the matching tag is a list, the second index will be append if the first index is positive
    # returns a list of tags that matched
    matches = []
    for tag in tags:
        if type(tag) == str:
            if tag in title:
                matches.append(tag)
        else:
            if tag[0] in title and tag[1] not in matches:
                matches.append(tag[1])
    return matches


def getFocus():
    windowTitle = GetWindowText(GetForegroundWindow()) # gets the currently focused window's title
    print(windowTitle)
    showTitle = checkByLengthMatch(windowTitle)
    tags = checkForTags(windowTitle)
    print(tags)
    return showTitle, tags # extracts data from the title


i = 0
while i < 10:
    getFocus()
    i += 1
    sleep(10)