![Banner](/PARKSGaze.png)
# PARKS-Gaze 
## Details and access of PARKS-gaze Dataset


### Link to the paper: [Towards Precision in Appearance-based Gaze Estimation](https://arxiv.org/abs/2302.02353)

We provide an In-the-Wild gaze estimation dataset PARKS-Gaze. 

- PARKS-Gaze contains 300,961 images of 28 subjects. We divide the dataset into Train, Valid and Test splits ensuring similar head pose and gaze distribution in all three splits. The number of subjects in Train, Valid and Test splits are 18, 4, and 6. 

- The dataset was collected in both indoor and outdoor environments, covering a wide range of  head poses, illumination conditions and intra-person appearance variations. 

- We provide the PARKS-Gaze dataset in two formats to cater to different input requirements of existing gaze estimation methods:
  * Format 1: Face and Eye Crops
    - Normalized face crop of size 120x120
    - Left and right eye crops of size 36x60
  * Format 2: Face Crop Only
    - Normalized face crop of size 3x224x224
    - No separate eye crops <br>
- We chose to release in these formats as most of the existing methods / approaches adopt one of these input sizes. 

## Dataset Structure
```
Parks-Gaze-Release.7z
├── Participant0
│   │── session_x.h5
│   │── session_y.h5
│   │── ...
│   │── ...
│   │── session_z.h5   
├── Participant1
│   │── session_x.h5
│   │── session_y.h5
│   │── ...
│   │── ...
│   │── session_z.h5   
├── Participant2
│   │── session_x.h5
│   │── session_y.h5
│   │── ...
│   │── ...
│   │── session_z.h5   
├── Participant3
│   │── session_x.h5
│   │── session_y.h5
│   │── ...
│   │── ...
│   │── session_z.h5   
├── ....
├── ....
├── ....
├── ....
├── Participant27
│   │── session_0.h5
│   │── session_1.h5
│   │── ...
│   │── ...
│   │── session_xx.h5   
```

## session_x.h5 File Structure

```
The attributes of each h5 file is a dictionary named "session_metadata" which contains the following necessary information about each session. 

- ParticipantID
- SessionID
- Intrinsic_Matrix : Camera Intrinsics Information
- Dist_Coeffs : Distortion coefficients of the camera (Used to undistort the images obtained using the camera during normalization)
- Screen_Resolution_X_mm : Width of the display (X direction) used in this particular session in millimeters
- Screen_Resolution_Y_mm : Height of the display (Y direction) used in this particular session in millimeters
- Screen_Resolution_X_px : Horizontal resolution of display used in this particular session in pixels
- Screen_Resolution_Y_px : Vertical resolution of display used in this particular session in pixels
- Camera_Screen_R : Extrinsic rotational matrix between camera and the screen coordinate systems
- Camera_Screen_T : Extrinsic translational vector between camera and the screen coordinate systems

In the format where a normalized face crop of 120x120 and left and right eye crops are present, a generic session_x.h5 file contains dictionaries with below keys.

- Norm_Face: Contains normalized face crops of that session (size 120x120).
- Norm_Leye: Contains normalized left eye crops of that session (size 36x60).
- Norm_Reye: Contains normalized right eye crops of that session (size 36x60).
- FixationID: Fixation IDs of the normalized samples available in this session. Each session recorded participants while making multiple fixations. Each fixation involves participant looking at a point on screen and making one of the following: head pose variation (position / orientation), facial expressions, activities like talking. 
- Norm_gaze: Normalized gaze data representing where the participant was looking. Format : [pitch, yaw]
- Norm_hp: Normalized head pose data, useful for understanding the head orientation.
- GazePt_Px: Gaze points in pixels (screen coordinate system).
- GazePt_mm: Gaze points in millimeters (screen coordinate system).
- FcCenter: Face center information of all normalized samples in the session. Format: [x, y, z], obtained as the average of the four eye corner landmarks using OpenFace 2.0 toolkit [1]
- FcRotMat: Rotation matrix of the face.


In the format where a normalized face crop of 224x224 is available, the left and right eye crops are not provided.


- For the task of 3D gaze estimation, one may use the Norm_Face, Norm_Leye and Norm_Reye along with Norm_gaze to train and evaluate the models. 

- For evaluating precision of the models on this dataset, one may transform the gaze predictions from the model (preds) to screen points using the python script "maptodisplay.py". The standard deviation across all predicted screen points corresponding to a single FixationID would be the precision error. 


```


## Train, Valid and Test Split Details:

```

Train
├── ParticipantIDs: 0, 1, 2, 3, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26 
Valid
├── ParticipantIDs: 6, 7, 11, 22 
Test
├── ParticipantID: 4, 5, 8, 9, 10, 27

```

## Download
To obtain access to the dataset, please send an email to `lrdmurthy@iisc.ac.in`. 
You will receive a Google Drive link within three days for downloading the dataset.
Please mention which format you would like to request (Either the face crops of size 120x120 along with eye crops or the one only with face crops of size 3x224x224. You may request both). 

Here's a sample email template for requesting access to the PARKS-Gaze Dataset. Please do not change the email subject.

Kindly fill the following details before sending

```
Subject: Request for Access to PARKS-Gaze Dataset

Dear Murthy,

XXXXXXXXXX

Your Name: 
Your Position / Role: 
Your Affiliation : 
Your Motivation to request the dataset: 

Kindly mention and guarantee that you will only utilize the dataset for academic and research purposes and will not use it for commercial activities.

```	


For any queries and collaborations related to gaze estimation, feel free to write to: lrdmurthy@iisc.ac.in
I would love to collaborate or provide more details.  


## License + Attribution

- The PARKS-Gaze dataset is licensed under CC BY-NC-SA 4.0. Commercial usage is not permitted. If you use this dataset or the code in a scientific publication or in a patent, please cite the following paper:

```
@article{lrd2023towards,
  title={Towards Precision in Appearance-based Gaze Estimation in the Wild},
  author={LRD, Murthy and Mukhopadhyay, Abhishek and Aggarwal, Shambhavi and Anand, Ketan and Biswas, Pradipta},
  journal={arXiv preprint arXiv:2302.02353},
  year={2023}
}
```

- The full manuscript with additional experiments compared to the arxiv version is currently under review for a journal. 

## Notes
- The name of the dataset is formed using the first letters of the first names of the authors, Pradipta, Abhishek, Raghavendra, Ketan and Shambhavi.
- I Took help of "https://github.com/yihuacheng/IVGaze?tab=readme-ov-file" to make this page. Thanks to Dr. Yihua Cheng. 
