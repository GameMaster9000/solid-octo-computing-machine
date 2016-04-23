from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
import random,urllib2

activities_to_do = urllib2.urlopen('https://raw.githubusercontent.com/bellcodo/potential-octo-chainsaw/master/code_activities_we_like.lst').read()                  
activities_to_do = activities_to_do.split()
going_to_do = random.choice(activities_to_do)


print "We can do the following" + str(activities_to_do)
print "We are going to do " + going_to_do 
return typing_choice

if __name__ == "__main__":
    # go get the PORT from the environment
    port = os.environ.get("PORT")
    # run the app with the port and bind to any ip
    app.run(
      "0.0.0.0"
    , port
    )
