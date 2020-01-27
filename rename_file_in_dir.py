#!/bin/python3
import os

count = 1
for dirname in os.listdir("."):
    if os.path.isdir(dirname):
        for i, filename in enumerate(os.listdir(dirname)):
            os.rename(dirname + "/" + filename, dirname + "/" + "captcha_" + str(count) + ".jpg")
            count += 1
