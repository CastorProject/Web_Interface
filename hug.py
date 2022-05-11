#! /usr/bin/env python
import time
import rospy

from flask import Flask, render_template, request
import threading

from std_msgs.msg import String
######################################
################ ROS #################
######################################
threading.Thread(target=lambda: rospy.init_node('abrazos', disable_signals=True)).start()
######################################
############# PUBLISHERS #############
######################################
pubMovements = rospy.Publisher('/movements', String, queue_size = 5)
pubHug = rospy.Publisher('/hug', String, queue_size = 5)
pubEmotions = rospy.Publisher('/emotions', String, queue_size = 5)
######################################
############# MAIN MENU ##############
######################################
app = Flask(__name__)
@app.route("/")
def mainMenu():
    templateData = {
        'title' : 'Main Menu',
    }
    return render_template('abrazos.html', **templateData)

@app.route("/<action>")
def actionMainMenu(action):
    if action == "comenzar":
        pubMovements.publish("hug")
	pubEmotions.publish("happy")
    elif action == "abrir":
        pubMovements.publish("hugOpen")
	pubEmotions.publish("happy")
    elif action == "cerrar":
        pubMovements.publish("hugClose")
	pubEmotions.publish("happy")
    elif action == "neutral":
        pubMovements.publish("neutral")
	pubEmotions.publish("neutral")
    elif action == "tiempo_corto":
        pubHug.publish("short_time")
	pubEmotions.publish("happy")
    elif action == "tiempo_largo":
        pubHug.publish("large_time")
	pubEmotions.publish("happy")
    elif action == "boton":
        pubHug.publish("button")
	pubEmotions.publish("happy")
    elif action == "globo":
        pubHug.publish("ballon")
	pubEmotions.publish("happy")
    templateData = {
        'title' : 'Main Menu',
    }
    return render_template('abrazos.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
