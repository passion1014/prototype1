# -*- encoding: utf-8 -*-

import re
import urllib.request

pattern = ".+\.pdf$"
re.match(pattern, "http://www.lgeri.com/uploadFiles/ko/pdf/man/LGBI970-20_20080109091428.pdf")

print(re.match(pattern, "http://www.lgeri.com/uploadFiles/ko/pdf/man/LGBI970-20_20080109091428.pdf"))
print("http://www.lgeri.com/uploadFiles/ko/pdf/man/LGBI970-20_20080109091428.pdf"["http://www.lgeri.com/uploadFiles/ko/pdf/man/LGBI970-20_20080109091428.pdf".rfind("/") + 1: ])

#urllib.request.urlretrieve("http://www.lgeri.com/uploadFiles/ko/pdf/man/LGBI970-20_20080109091428.pdf", "C:/Users/Dasol/Desktop/ess/test.pdf")