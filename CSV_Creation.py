import pandas as pd
import os
import numpy as np

person_num = 3

# Run on all folders:

folders = os.listdir("Filtered")

for folder in folders:
    group_num = folder.split("_")[0]

    print(group_num)
    try:
        frames = os.listdir(f"Filtered/{folder}")

        outputs = [[], [], []]

        for f in frames:
            df = pd.read_json(f"Filtered/{folder}/{f}")

            for person in range(person_num):
                datas = np.array(df[f"person_{person}"])
                outputs[person].append(datas)

        for person in range(person_num):
            df_person = pd.DataFrame(outputs[person])
            df_person.to_csv(
                f"CSV/{group_num}_p{person}.csv", encoding="utf-8", index=False
            )
    except Exception:
        print(f"Data is missing, skipped group {group_num}")
        pass


# Run on a specific folder/folders:

# folders = os.listdir("Filtered")

# for folder in folders:
#     group_num = folder.split("_")[0]

#     if int(group_num) > 1031:
#         print(group_num)
#         try:
#             frames = os.listdir(f"Filtered/{folder}")

#             outputs = [[], [], []]

#             for f in frames:
#                 df = pd.read_json(f"Filtered/{folder}/{f}")

#                 for person in range(person_num):
#                     datas = np.array(df[f"person_{person}"])
#                     outputs[person].append(datas)

#             for person in range(person_num):
#                 df_person = pd.DataFrame(outputs[person])
#                 df_person.to_csv(
#                     f"CSV/{group_num}_p{person}.csv", encoding="utf-8", index=False
#                 )
#         except Exception:
#             print(f'Data is missing, skipped group {group_num}.')
#             pass
