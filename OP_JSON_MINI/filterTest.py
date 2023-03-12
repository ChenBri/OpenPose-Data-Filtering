import json


def writeFiles(file):
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

    return repr(personObj)


print(
    writeFiles(
        r"C:\Users\chenb\Desktop\OP_JSON_MINI\Unfiltered\1001_JSON\1001_000000000001_keypoints.json"
    )
)
