﻿# OpenPose Data Filtering
 
 This script shows an example of taking the first five elements from the BODY_25 model from 3 participants in the same video.
The script takes a folder separated into different sessions, each with up to 5,000 JSON files.

The script filters the raw data into more readable data.
In this example, the script takes the first five elements from each participant (each part is separated into three components, x1, y1, and c1.

Unfiltered:
```
{"version":1.3,"people":[{"person_id":[-1],"pose_keypoints_2d":[1301.34,503.739,0.879129,1230.82,506.784,0.887376,1166.09,506.641,0.824263,1089.49,621.553,0.908344,1166.03,709.877,0.881702,1289.64,506.776,0.820521,1304.31,612.663,0.871652,1322,689.229,0.809425,1201.3,692.075,0.737008,1157.19,695.008,0.688801,1189.59,801.019,0.551479,1104.23,880.524,0.226973,1242.53,686.328,0.710115,1330.9,786.382,0.813165,1230.73,860.022,0.768912,1286.76,483.235,0.899501,1307.27,486.111,0.535373,1248.44,453.788,0.884608,0,0,0,1204.24,907.129,0.679175,1213.13,907.14,0.759391,1213.07,859.851,0.543717,1107.18,910.001,0.215509,1107.21,909.998,0.176995,1095.37,877.563,0.1953],"face_keypoints_2d":[],"hand_left_keypoints_2d":[],"hand_right_keypoints_2d":[],"pose_keypoints_3d":[],"face_keypoints_3d":[],"hand_left_keypoints_3d":[],"hand_right_keypoints_3d":[]},{"person_id":[-1],"pose_keypoints_2d":[989.487,439.118,0.861657,889.412,527.255,0.817493,833.385,530.36,0.740816,812.874,674.512,0.73267,948.267,589.163,0.782658,954.048,509.66,0.847246,953.997,656.898,0.783424,1024.69,727.436,0.838671,912.879,733.333,0.613252,877.591,742.271,0.539288,1039.5,853.969,0.667173,0,0,0,951.118,718.576,0.646028,1095.42,809.904,0.826445,1071.79,889.355,0.200574,965.891,418.513,0.832446,992.365,415.545,0.678057,904.113,430.138,0.878892,0,0,0,1086.59,927.562,0.100318,0,0,0,1071.8,883.441,0.174235,0,0,0,0,0,0,0,0,0],"face_keypoints_2d":[],"hand_left_keypoints_2d":[],"hand_right_keypoints_2d":[],"pose_keypoints_3d":[],"face_keypoints_3d":[],"hand_left_keypoints_3d":[],"hand_right_keypoints_3d":[]},{"person_id":[-1],"pose_keypoints_2d":[880.609,509.698,0.869486,706.852,627.447,0.608123,668.518,650.97,0.59138,692.258,930.488,0.732131,906.958,904.02,0.785855,745.181,603.84,0.425503,792.208,786.221,0.672625,907.055,856.941,0.780485,780.485,942.346,0.339389,724.566,986.453,0.332165,1104.18,1051.28,0.614972,0,0,0,830.466,889.418,0.403877,1071.93,951.094,0.728481,0,0,0,860.018,494.939,0.838554,0,0,0,771.634,503.642,0.844651,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"face_keypoints_2d":[],"hand_left_keypoints_2d":[],"hand_right_keypoints_2d":[],"pose_keypoints_3d":[],"face_keypoints_3d":[],"hand_left_keypoints_3d":[],"hand_right_keypoints_3d":[]}]}
```

Filtered:
```
{"person_0": [1301.34, 503.739, 0.879129, 1230.82, 506.784, 0.887376, 1166.09, 506.641, 0.824263, 1089.49, 621.553, 0.908344, 1166.03, 709.877, 0.881702], "person_1": [989.487, 439.118, 0.861657, 889.412, 527.255, 0.817493, 833.385, 530.36, 0.740816, 812.874, 674.512, 0.73267, 948.267, 589.163, 0.782658], "person_2": [880.609, 509.698, 0.869486, 706.852, 627.447, 0.608123, 668.518, 650.97, 0.59138, 692.258, 930.488, 0.732131, 906.958, 904.02, 0.785855]}
```
 
 When converting the filtered data into a CSV file, each group gets 3 CSV files.
 Each CSV file represents 1 participant (1 person).
 Each Column represents a different key point (x1, y1, c1, x2, y2, c2...).
 Each row represents a frame.
 
 CSV:
 |0      |1      |2       |3      |4      |5       |6      |7      |8       |9      |10     |11      |12     |13     |14      |
|-------|-------|--------|-------|-------|--------|-------|-------|--------|-------|-------|--------|-------|-------|--------|
|1301.34|503.739|0.879129|1230.82|506.784|0.887376|1166.09|506.641|0.824263|1089.49|621.553|0.908344|1166.03|709.877|0.881702|
|1301.34|503.736|0.877089|1233.57|506.788|0.890749|1166.11|506.629|0.821096|1089.47|621.417|0.884327|1166.03|709.864|0.870098|
|1301.34|503.737|0.877867|1230.83|506.79 |0.888034|1166.1 |506.651|0.822907|1089.5 |621.531|0.90014 |1166.02|709.843|0.87482 |
|1301.34|503.737|0.876821|1230.83|506.784|0.887942|1166.1 |506.646|0.822933|1089.48|621.504|0.89655 |1166.01|709.848|0.876973|
|1301.34|503.737|0.877307|1230.83|506.781|0.887874|1166.09|506.644|0.823892|1089.48|621.496|0.893082|1166.01|709.838|0.874441|
|1301.34|503.738|0.878067|1230.83|506.781|0.888902|1166.1 |506.646|0.822996|1089.45|621.501|0.894637|1166.01|709.805|0.870204|

 
![Nose movement visualization](Nose_compare_rawdata.jpg)

![BODY_25 Image](keypoints_pose_25.png)

