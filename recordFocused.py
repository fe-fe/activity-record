from win32gui import GetWindowText, GetForegroundWindow
from getpass import getuser
import os
import re
from datetime import datetime
import json
from commitChanges import commitActivity
import asyncio


tags = [
    # one-word tags that must be tracked
    # if the tag is an array[2], the first index is the word to be matched 
    # and the second is the one to be shown
    "Python", ["py", "Python"], "Java", "Selenium", "JavaScript", ["js", "JavaScript"], 
    "Flutter", "Bootstrap", "Spring", ["nlp", "PLN"], "Flask",
    "PLN", "HTML", "CSS", "Git", "Django",
    "GitHub", "React", "Angular", "Linkedin", "JSON", ["ts", "TypeScript"], "Coursera"  
]

multiTags = [
    "Visual Studio Code", "Stack Overflow", "Tensor Flow" 
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
        if mtag.lower() in title:
            matches.append(mtag)

    title = re.split(r'[, .:]', title)

    for tag in tags:
        if type(tag) == str:
            tag = [tag, tag]
        if tag[0].lower() in title and tag[1] not in matches:
            matches.append(tag[1])
        
    return matches


def getFocus():
    windowTitle = GetWindowText(GetForegroundWindow()) # gets the currently focused window's title
    tags = checkForTags(windowTitle)
    return tags # extracts data from the title


def writeActivity(tags, time):
    try:
        with open("activity.json", "r") as activity:
            data:dict = json.load(activity)
    except:
        data = {"last_wipe": str(datetime.today().date()), "activity": []}

    for tag in tags:
        tag = re.sub(" ", "_", tag)
        entry = next((entry for entry in data["activity"] if entry["name"] == tag), None)

        if entry:
            hours = entry["time_spent"]
            data["activity"].remove(entry)
        else:
            hours = 0
            
        data["activity"].append({"name": tag, "time_spent": round(hours + time, 3)})

    result = json.dumps(data, indent=4)

    with open("activity.json", "w") as activity:
        activity.write(result)


async def waitForInput():
    await asyncio.to_thread(input, "::: press any key to stop :::")


async def mainLoop():
    global run
    while run:

        # the current window's data (tags) is extracted
        # and the current time is stored in "start"
        # the program sleeps until the program identifies changes in the tags
        # and then it writes the tags and how much time in hours they have been positive 
        # commit changes every 5 hours

        current = getFocus()
        start = datetime.now()
        await asyncio.sleep(5)
        
        while current == getFocus():
            await asyncio.sleep(5)
        
        elapsed = datetime.now() - start 
        elapsed = (elapsed.total_seconds())/3600
        
        writeActivity(current, elapsed)

        if ((datetime.now() - lastcommit).total_seconds()/3600) >= 3:
            commitActivity()


async def main():
    global run
    asyncio.create_task(mainLoop())
    await waitForInput()
    run = False


checkForIntelliJ()
lastcommit = datetime.now()
run = True

asyncio.run(main())