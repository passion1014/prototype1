# -*- encoding: utf-8 -*-

# ==================================================
# > 동아 비즈니스 리뷰 스크랩핑 
#==================================================
import os
import string
import random
import re

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request

# ==================================================
def getRandomString (arg001) :
    rtn = ""

    if type(0) is type(arg001) and None is not arg001 :
        stringPool = string.ascii_letters + string.digits
        
        for i in range(arg001) :
            rtn += random.choice(stringPool)

    return rtn
# ==================================================

# ==================================================
def webScraping (arg001) :
    if type([]) is type(arg001) and None is not arg001 :
        pdfFilePattern = ".+\.pdf$" # PDF 파일 여부를 확인하기 위한 정규표현식
        spcCharPattern = "[\\\/\*\?\<\>\|\"]" # 특수문자를 제거하기 위한 정규표현식
        fileName = ""

        for info in arg001 :

            # ==================================================
            # Step [001] > 정보 적재
            # ==================================================
            href = info["href"]
            category = re.sub(spcCharPattern, " ", info["category"])
            title = re.sub(spcCharPattern, " ", info["title"])
            author = re.sub(spcCharPattern, " ", info["author"])

            # ==================================================
            # Step [002] > 파일 정보 설정
            # ==================================================
            fileName = "[" + category +"] " + title + "-" + author
            imgFolderName = "img_" + getRandomString(16)

            page = urlopen(homeUrl + href)
            htmlDoc = page.read()
            page.close()

            soup = BeautifulSoup(htmlDoc, "html.parser")
            doc = soup.body.find("div", {"class" : "cboth cont-article mg-b40" })
            f = open(localTargetPath + "/" + fileName + ".html", "w", -1, "utf-8")

            for item in doc.find_all() :

                # ==================================================
                # Step [003-01] > PDF 여부 확인 후 PDF 파일 저장
                # ==================================================
                if re.match(pdfFilePattern, item.get_text().strip()) :
                    print("대상 >> " + item.get_text().strip())

                    try :
                        urllib.request.urlretrieve(item.get_text().strip(), localTargetPath + "/" + fileName + ".pdf")
                    except urllib.error.HTTPError as e :
                        print(e)

                # ==================================================
                # Step [003-02] > 그 외에 경우 HTML 파일 및 이미지 저장
                # ==================================================
                else :

                    if "img" == item.name and item.has_attr("src") :
                        try :
                            os.mkdir(localTargetPath + "/" + imgFolderName)

                        # 기존재 폴더가 있는 경우
                        except FileExistsError as e :
                            print(e)

                        src = item.get("src").replace(" ", "%20")
                        imgName = getRandomString(20) # 이미지명 랜덤한 String으로 변경
                        
                        try :
                            urllib.request.urlretrieve("https://dbr.donga.com" + src, localTargetPath + "/" + imgFolderName + "/" + imgName + ".jpg")
                            item["src"] = "./" + imgFolderName + "/" + imgName + ".jpg"

                        except urllib.error.HTTPError as e :
                            print(e)

            f.write(str(doc))
            f.close()

        return "Success"

# ==================================================

# ==================================================
# @process    : 숫자 앞에 0을 N자리 만큼 추가한 문자열 형태의 값을 반환
# @argument : arg001 [Number] 대상 숫자
# @argument : arg002 [Number] : 0을 추가할 최대 사이즈
# @return      : string
# ==================================================
def addZeroPrefix (arg001, arg002) :
    rtn = ""

    if type(0) is type(arg001) and None is not arg001 :
        rtn = str(arg001)

        # 사이즈 확인
        if arg002 > len(rtn) :
            prefix = "" 

            # N자리 만큼 0 추가 
            for i in range(arg002 - len(rtn)) :
                prefix += "0"

            rtn = prefix + rtn

    return rtn
# ==================================================

homeUrl = "https://dbr.donga.com"
localBasicPath ="C:/Users/Dasol/Desktop/ess/"
localTargetPath = ""

infoList = list()

startYear = 2008
pubNumber = 1

page = urlopen(homeUrl + "/magazine/mcontents/type/list/year/" + str(startYear) + "/pub_number/" + str(pubNumber))
htmlDoc = page.read()
page.close()

soup = BeautifulSoup(htmlDoc, "html.parser")
doc = soup.body.find("div", {"class" : "article_list" })
document = page.read()
page.close()

for elem in doc.find_all("a"):
    infoList.append({
        "href" : elem.get("href") # 경로
         , "category" : elem.find("span", {"class" : "category"}).get_text() # 카테고리
         , "title" : elem.find("span", {"class" : "title"}).get_text() # 제목
         , "author" : elem.find("span", {"class" : "name"}).get_text() # 작성자
    })

localTargetPath = localBasicPath + str(startYear) + "_" + addZeroPrefix(pubNumber, 3) 

# ==================================================
# Step [003] > 폴더 생성 시도
# ==================================================
try :
    os.mkdir(localTargetPath)

# 기존재 폴더가 있는 경우
except FileExistsError as e :
    print(e)

print(webScraping(infoList))