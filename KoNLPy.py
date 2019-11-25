# -*- encoding: utf-8 -*-

# ==================================================
# @ DESC  :
# @ REF     : 코엔엘파이(KoNLPy) 설치 과정
# @            (1) JAVA 1.7 이상의 설치 
# @            (2) JAVA_HOME Path 설정 
# @                • JDK가 정상적으로 동작하기 위하여 JAVA_HOME 경로(Path)를 설정해야한다. 
# @                • [시스템 변수]에 path의 변수값 부분에 JDK가 설치되어있는 경로를 입력한다.
# @            (3) JPype1 (>=0.5.7) 설치 (pip 모듈 이용)
# @                • JAVA로 작성된 모듈을 로드하여야 하기 때문에 JPype1 0.5.7 이상이 설치되어야 한다.
# @                • pip install jpype1
# @                • 설치 중 에러 발생시 본 링크(https://www.visualstudio.com/vs/older-downloads/) 에서 Microsoft Visual C++ 14.0 build tool 설치
# @                  (Redistributables and Build Tools > Microsoft Build Tools 2015 Update 3)
# @            (4) KoNLPy 설치 (pip 모듈 이용)
# @                • pip install konlpy
# @                • 아래와 같은 Warning 메시지가 발생시 JPype1 버전을 하향시킬 필요가 있다 (미필수 선택사항)
#==================================================

from konlpy.tag import Hannanum
hannanum = Hannanum()
 
hannanum.analyze  #구(Phrase) 분석
hannanum.morphs   #형태소 분석
hannanum.nouns    #명사 분석
hannanum.pos      #형태소 분석 태깅

# 사용예시
print(hannanum.analyze(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
print(hannanum.morphs(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
print(hannanum.nouns(u'다람쥐 헌 쳇바퀴에 타고파'))
print(hannanum.pos(u'웃으면 더 행복합니다!'))