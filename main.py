import cv2
import streamlit as st
import datetime as dt


def get_date_time():
    date_time = dt.datetime
    now = date_time.now()
    day = now.strftime("%A")
    time = now.time().strftime("%H:%M:%S")
    return day, time


st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        week_day, current_time = get_date_time()
        cv2.putText(img=frame, text=f"{week_day}", org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20, 100, 200),
                    thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=f"{current_time}", org=(50, 100),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20, 100, 200),
                    thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)
