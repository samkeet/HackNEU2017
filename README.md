# Documenting in progress...
# HackNEU 2017
Northeastern University 2017 Hackathon (HackNEU) repository includes source files and documents for developing the hackathon project.
## Overview
We have developed an anomaly detection system using machine learning, to detect abnormal patterns in power traces of computers, servers and later extended to household electric consumption. The motivation behind this system was, to detect anomalous power dynamics by a device which is integrated with Google (Firebase) Cloud messaging to notify users on their mobile devices using push notifications, twitter and/or slack channels, of the detected event. The project was initially developed to notify system admins of organizations of anomalous power traces usage which can be used by hackers to determine the general behavior and possibly learn the secret encryption keys of the machine. Hence as a test case, we used a power trace from an unmasked version of AES encryption, also we used a household power consumption dataset from the University of California, Irvine to evaluate our platform. The power traces with regular trends were categorised as normal behaviour by our machine learning model. Whereas the anomalous trace/plot clearly indicates outliers in the trace, which immediately alerts the user/admin.

## What's inside and how it works?
## Building the toolchain
## Let's go live!
## License

This project is licensed under the MIT License - see the [license]() file for details

## Acknowledgments

This project was based on the materials presented and taught by professor Refael Ubal for the Compilers course (EECE-7398) at Northeastern University in Fall 2016.
