import cv2, time
from datetime import datetime
import pandas




video=cv2.VideoCapture(0)

first_frame=None
status_list=[None, None]
times=[]
df=pandas.DataFrame(columns=["Start", "End"])


while True:
    #count the total frame
    #a=a+1

    #check, frame=video.read()

    #print(check)
   # print(frame)
    #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   # time.sleep(3)


    check, frame=video.read()
    status=0
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #make the image blur
    gray=cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame=gray
        continue
    status=1

    delta_frame=cv2.absdiff(first_frame, gray)

    thresh_delta=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    #smooth the thresh_frame white area delate method
    thresh_frame=cv2.dilate(thresh_delta, None, iterations=2)

    #contour line
    (cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for countour in cnts:
        if cv2.contourArea(countour) <1000:
            continue
        status=1
        (x, y, w, h)=cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        status_list.append(status)


    if status_list[-1]==1 and status_list[-2]==0:
        #appen current date time
        times.append(datetime.now())

    if status_list[-1]==1 and status_list[-2]==1:
        times.append(datetime.now())


    #cv2.imshow("Cvideapturing",frame)
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key=cv2.waitKey(1)

    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

    print(status_list)
    print(times)

for i in range(0, len(times), 2):
    df=df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("times.csv")
video.release()
cv2.destroyAllWindows()
