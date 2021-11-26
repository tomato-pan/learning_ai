# 摄像头+视频操作
import cv2,time
import numpy as np


def video_demo():
    capture = cv2.VideoCapture(0)
    while True:
        # ret, frame = capture.read()
        # frame = cv2.flip(frame, 1)
        # cv2.imshow("video", frame)
        num_frames = 60
        print("Capturing {0} frames".format(num_frames))
        # Start time
        start = time.time()
        # Grab a few frames
        for i in range(0, num_frames):
            ret, frame = capture.read()
            frame = cv2.flip(frame, 1)
            cv2.imshow("video", frame)
        # End time
        end = time.time()
        # Time elapsed
        seconds = end - start
        print("Time taken : {0} seconds".format(seconds))
        # 计算FPS，alculate frames per second
        fps = num_frames / seconds
        print("Estimated frames per second : {0}".format(fps))
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 如果按下q 就截图保存并退出
            cv2.imwrite("test.png", frame)  # 保存路径
            capture.release()
            break


if __name__ == '__main__':
    video_demo()
    cv2.destroyAllWindows()
