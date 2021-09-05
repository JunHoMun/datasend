#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32
import pyrebase

config = {
    "apiKey": "AIzaSyDx5CNQ4a41MtJnMm80Ntge2I93dvdHEXU",
    "authDomain": "bicycle-data-f3bde.firebaseapp.com",
    "databaseURL": "https://bicycle-data-f3bde-default-rtdb.firebaseio.com",
    "projectId": "bicycle-data-f3bde",
    "storageBucket": "bicycle-data-f3bde.appspot.com",
    "messagingSenderId": "523579318376",
    "appId": "1:523579318376:web:da12f9c56bd499d4e75bdd",
    "measurementId": "G-91YTVG2N92"
}

def lati_callback(data):
    rospy.loginfo("lati is : %d", data.data)
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    db.update({"velo": data.data})




def main():
    rospy.init_node('testsub', anonymous=True)
    rospy.loginfo("firebase module is actived")
    sub = rospy.Subscriber('lati', Int32, lati_callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
