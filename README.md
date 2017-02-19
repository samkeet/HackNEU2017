# HackNEU 2017
![Outlier](https://github.com/samkeets/HackNEU-2017-Outliers/blob/master/figures/outlier.png)
Northeastern University 2017 Hackathon (HackNEU) repository includes source files and documents for developing the **Outlier** project.
## Overview
We have developed an anomaly detection system using machine learning and adaptive filter methods, to detect abnormal patterns in power traces of computers, servers, and household electric consumption. The motivation behind this system was to detect anomalous power dynamics by a device which is integrated with Google (Firebase) Cloud messaging to notify users on their mobile devices using push notifications, twitter and/or slack channels, of the detected event. The project was initially developed to notify system admins of organizations of anomalous power traces usage which can be used by hackers to determine the general behavior and possibly learn the secret encryption keys of the machine. Hence as a test case, we used a power trace from an unmasked version of AES encryption, also we used a household power consumption dataset from the University of California, Irvine to evaluate our platform. The power traces with regular trends were categorised as normal behaviour by our machine learning model. Whereas the anomalous trace/plot clearly indicates outliers in the trace, which immediately alerts the user/admin.

## Approach
We used a multivariate Gaussian model based on [this work](https://aqibsaeed.github.io/2016-07-17-anomaly-detection/) to learn the typical power trends and detect the outliers. The algorithm has been developed in [Python](https://www.python.org/). Particularly, various data pre-processing and post-processing challenges including restructring our dataset for our machin learning model and gathering our data to a proper analyzable form have been addressed. The following figures shows the output of our tool operated on an unmasked AES power traces (red point shows outliers which alert the user/admin about and anamolous event):
![Outlier](https://github.com/samkeets/HackNEU-2017-Outliers/blob/master/figures/outlier.png)


## Challenges Faced
* Handling large datasets (10000x3125)
* Preprocessing the datasets to remove NULL or empty fields
* Converting the input datasets into appropriate formats for applying the machine learning model
* Integrating Google Firebase notification platform to send push notification to users through a custom-designed Android app
* Integrating Slack and Twitter posting APIs and authentication procedures to our system

## License
This project is licensed under the MIT License - see the [license]() file for details

## Project members
|Name|Email|
|----|-----|
|Majid Sabbagh|sabbagh.m@husky.neu.edu|
|Samkeet Shah|shah.sam@husky.neu.edu|
|Shantanu Kawlekar|kawlekar.s@husky.neu.edu|
|Yixing Zhang|zhang.yixin@husky.neu.edu|
## Acknowledgments
We would like to thank [Rohan Jahagirdar](https://www.linkedin.com/in/rohan-jahagirdar/) and [Shreyas Mahimkar](https://www.linkedin.com/in/shreyas-mahimkar-64593918/) for their great help during the Hackathon.
