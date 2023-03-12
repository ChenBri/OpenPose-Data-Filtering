import os
import json


def writeFiles(file):
    filteredPath = file.replace("Unfiltered", "Filtered")
    filteredPath = os.path.dirname(os.path.dirname(f"{filteredPath}/"))

    fileName = os.path.basename(file)

    with open(file, "r") as unfiltered_file:
        fileContent = unfiltered_file.read()

        # Filter
        fileContent = filterJson(file)

        if not os.path.exists(filteredPath):
            os.makedirs(filteredPath)

        with open(f"{filteredPath}/{fileName}", "w") as filtered_file:
            filtered_file.write(fileContent)


def iterateFiles(file):
    for filename in os.listdir(file):
        f = os.path.join(file, filename)

        if os.path.isfile(f):
            writeFiles(f)


def iterateFolders(folder):
    for filename in os.listdir(folder):
        f = os.path.join(folder, filename)

        if os.path.isdir(f):
            iterateFiles(f)

    print("Done.")


def filterJson(file):

    personObj = {}

    with open(file, "r") as f:
        data = json.load(f)

        people = data["people"]

        for (index, person) in enumerate(people):

            personList = []

            for (index2, position) in enumerate(person["pose_keypoints_2d"]):

                if index2 in range(15):
                    personList.append(position)

            personObj[f"person_{index}"] = personList

    return repr(personObj).replace("'", '"')


iterateFolders(r"Unfiltered")
