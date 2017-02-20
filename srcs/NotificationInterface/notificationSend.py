## import notification packages
import tweepy
from pyfcm import FCMNotification
from slackclient import SlackClient



    ################# Send notification to a single device.
    push_service = FCMNotification(api_key="<API key>")

    # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
    registration_id = "<Registration ID>"
    message_title = "ALERT!"
    message_body = "Anamoly detected in the component power trace."
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body)

	################# Twitter post (Need to be fixed!)										   
	def get_api(cfg):
		auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
		auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
		return tweepy.API(auth)

    # Fill in the values noted in previous step here
    cfg = {
        "consumer_key": "<Consumer Key>",
        "consumer_secret": "<Consumer Secret>",
        "access_token": "<Access Token>",
        "access_token_secret": "<Access Token Secret>"
    }

    api = get_api(cfg)
    tweet = "Hello, world!"
    status = api.update_status(status=tweet)
    # Yes, tweet is called 'status' rather confusing

    ################# Slack post
    slack_token = "<Slack token>"
    sc = SlackClient(slack_token)

    sc.api_call(
        "chat.postMessage",
        channel="#<target channel name>",
        text="<your message>"
    )

