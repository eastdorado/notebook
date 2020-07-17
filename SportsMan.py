#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @Product: PyCharm
#  @Project: Neworld
#  @File    : SportsMan.py
#  @Author  : big
#  @Email   : shdorado@126.com
#  @Time    : 2020/7/14 0:09
#  功能：


import sys
import numpy as np
import cv2
import requests
import re
import json


class VideoManager(object):

    def play(self, file):
        cap = cv2.VideoCapture(r'f:/rain_of_love sickness.mp4')
        while cap.isOpened():
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(40) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def getVipVideoInHtml(self):
        url = "http://v.qq.com/x/cover/5a3aweewodeclku/b0024j13g3b.html"

        # def get_address(url):
        md5 = re.search(r'key:"(.*?)"', requests.get("http://jiexi_site_url/lines?url=" + url).text).group(1)
        dic = json.loads(
            requests.post("http://jiexi_site_url/lines/getdata", data={"url": url, "type": "", "key": md5}).text)

        for i in dic:
            iurl = i["Url"]
            posturl = iurl.split("?url=")[0] + "/api/"
            url = iurl.split("url=")[1].split("&")[0].replace("%3d", "=").replace("%2f", "/").replace("%2b", "+")
            if "type=" in iurl:
                utype = iurl.split("type=")[1]
            r = requests.post(posturl,
                              data={"url": url, "type": utype, "from": "jiexi_site_url", "device": "", "up": ""})
            print(r.text)


def main():
    pass


if __name__ == '__main__':
    main()
