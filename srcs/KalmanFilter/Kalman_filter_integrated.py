# Kalman filter

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## import notification packages
import tweepy
from pyfcm import FCMNotification
from slackclient import SlackClient


plt.rcParams['figure.figsize'] = (10, 8)


## Twitter post
# def get_api(cfg):
#     auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
#     auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
#     return tweepy.API(auth)
#
#
# def sendTweet():
#     # Fill in the values noted in previous step here
#     cfg = {
#         "consumer_key": "<Consumer Key>",
#         "consumer_secret": "<Consumer Secret>",
#         "access_token": "<Access Token>",
#         "access_token_secret": "<Access Token Secret>"
#     }
#
#     api = get_api(cfg)
#     tweet = "Hello, world!"
#     status = api.update_status(status=tweet)
#     # Yes, tweet is called 'status' rather confusing
# # intial parameters
# # g for column 3
# # g1 for column 4


################# Read input data
with open("g1.csv") as f:
    col = ['a', 'b']
    dta = pd.read_csv(f, names=col)

# dta.columns = ['a', 'b']

print(len(dta['b']))

n_iter = len(dta['b'])
# n_iter = 50


################# Kalman filter operation
sz = (n_iter,)  # size of array
# x = -0.37727 # truth value (typo in example at top of p. 13 calls this z)
x = 0.12371447630385488
# z = np.random.normal(x,0.1,size=sz) # observations (normal about x, sigma=0.1)
z = dta['b']
Q = 0.5  # process variance 1e-5 2e-3 1e-1

# allocate space for arrays
xhat = np.zeros(sz)  # a posteri estimate of x
P = np.zeros(sz)  # a posteri error estimate
xhatminus = np.zeros(sz)  # a priori estimate of x
Pminus = np.zeros(sz)  # a priori error estimate
K = np.zeros(sz)  # gain or blending factor

R = 0.1 ** 2  # estimate of measurement variance, change to see effect
delta = np.zeros(sz)
# intial guesses
xhat[0] = 0.0
P[0] = 1.0
f = open("delta_col4.csv", "w+")
for k in range(1, n_iter):
    # time update
    xhatminus[k] = xhat[k - 1]
    Pminus[k] = P[k - 1] + Q

    # measurement update
    K[k] = Pminus[k] / (Pminus[k] + R)

    delta[k] = Pminus[k] - float(z[k])
    xhat[k] = xhatminus[k] + K[k] * float(z[k]) - xhatminus[k]
    P[k] = (1 - K[k]) * Pminus[k]

for item in delta:
    f.write("%s\n" % item)

dataset_delta = pd.read_csv("delta_col4.csv")
dataset_delta = dataset_delta.abs()
threshold = dataset_delta.values.std() + dataset_delta.values.mean()
dataset_threshold = dataset_delta[dataset_delta >= threshold]

if not dataset_threshold.empty:
    print("Anomaly Detected!!")

    plt.figure()
    plt.plot(z,'k+',label='noisy measurements')
    plt.plot(xhat,'b-',label='a posteri estimate')
    plt.axhline(x,color='g',label='truth value')
    #plt.legend()
    plt.title('Estimate vs. iteration step', fontweight='bold')
    plt.xlabel('Iteration')
    plt.ylabel('Voltage')

    # plt.figure()
    # valid_iter = range(1,n_iter) # Pminus not valid at step 0
    # plt.plot(valid_iter,Pminus[valid_iter],label='a priori error estimate')
    # plt.title('Estimated $\it{\mathbf{a \ priori}}$ error vs. iteration step', fontweight='bold')
    # plt.xlabel('Iteration')
    # plt.ylabel('$(Voltage)^2$')
    # plt.setp(plt.gca(),'ylim',[0,.01])
    plt.show()

    ################# Send notification to a single device.
    push_service = FCMNotification(api_key="<API key>")

    # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
    registration_id = "<Registration ID>"
    message_title = "ALERT!"
    message_body = "Anamoly detected in the component power trace."
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body)

	################# Twitter post (Need to be fixed!)										   
    #sendTweet()

    ################# Slack post
    slack_token = "<Slack token>"
    sc = SlackClient(slack_token)

    sc.api_call(
        "chat.postMessage",
        channel="#<target channel name>",
        text="<your message>"
    )

