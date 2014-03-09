from twython import TwythonStreamer, Twython


class TAPPStreamer(TwythonStreamer):


    def __init__(self, APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET):
        super(TAPPStreamer, self).__init__(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        print "Initializing TAPP Daemon"
        self.twython = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        self.credentials = self.twython.verify_credentials()
        self.id = self.credentials['id']
        self.screen_name = self.credentials['screen_name']
        print "%d - %s"%(self.id, self.screen_name)
        self.users_fix()

    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

    def users_fix(self):
        print "Fixing users friends and followers"
        pass


APP_KEY = 'CkpAMnvPzPywJV11w7K6eA'
APP_SECRET = 'PesJvI6AsWO5dortIqC6UPEulrGPIhg5RuKEJ4W5U'
OAUTH_TOKEN = '2374204129-le0emmc0f58af0EvjJs4mNVjlIq5runsuWxlIzP'
OAUTH_TOKEN_SECRET = 'tmsLkujsYeIYiRMJBOS5bvezczwt4zIcaB307lNmOPwPw'

st = TAPPStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)