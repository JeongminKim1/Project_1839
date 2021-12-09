#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import openpyxl
from selenium import webdriver
import time
from bs4 import BeautifulSoup



driver = webdriver.Chrome('크롬드라이버저장위치')
url = 'https://nid.naver.com/nidlogin.login'
driver.get(url)
driver.execute_script("document.getElementsByName('id')[0].value='본인아이디'")
driver.execute_script("document.getElementsByName('pw')[0].value='본인패스워드'") 
driver.find_element_by_xpath('//*[@id="log.login"]').click()

study_text = []
study_num = []
study_nickname = []

for z in range(23, 30, 1):      ##수정 필요! n~m번째 페이지 할 거면 (n-1, m, 1)!!

  print(str(z+1) + "번째 페이지")

  mbti = 12  ##수정 필요! 1번째 게시판(INFP & ENFP) ~ 8번째 게시판(ISTJ & ESTJ)까지 = 18~11 (1씩 작아짐)

  url = "https://cafe.naver.com/ArticleList.nhn?search.clubid=11856775&search.menuid=" + str(mbti) + "&search.boardtype=L&search.totalCount=151&search.cafeId=11856775&search.page=" + str(z+1)
  driver.get(url)
  time.sleep(3)
  element = driver.find_element_by_id("cafe_main") #iframe 태그 엘리먼트 찾기
  driver.switch_to.frame(element)
  time.sleep(3)
  a = driver.find_elements_by_class_name("inner_number")
  k = [0 for i in range(len(a))]

  for i in range(0,len(a),1):
    n = a[i].text
    k[i] = n

  time.sleep(3)

  for i in range(0, len(k), 1):
    print(str(z+1) + "번째 페이지 " + str(i+1) + "번째 게시물")
    url = 'https://cafe.naver.com/mbticafe/' + k[i]

    driver.get(url)
    time.sleep(3)
    element = driver.find_element_by_id("cafe_main") #iframe 태그 엘리먼트 찾기
    driver.switch_to.frame(element)

    time.sleep(3)

    # 본문 내용, 닉네임 추출

    tex = k[i] + '본문'

    time.sleep(3)
    
    title = driver.find_element_by_css_selector("h3.title_text").text
    b = driver.find_elements_by_css_selector("p.se-text-paragraph.se-text-paragraph-align-")

    if(len(b)==0):
      b = driver.find_elements_by_css_selector("p.se-text-paragraph.se-text-paragraph-align-left")

    if(len(b)!=0):
      c= [0 for j in range(len(b))]
      time.sleep(3)

      for j in range(0,len(b),1):
        n = b[j].find_element_by_tag_name("span")
        c[j] = n.text

    if(len(b)==0):
      b = driver.find_elements_by_css_selector("div.ContentRenderer")
      for j in range(0,len(b),1):
         n = b[j].find_element_by_tag_name("p")
         c[j] = n.text

    if(len(b)==0):
      continue

    time.sleep(3)
    
    m = ""

    for q in range(0, len(c),1):

      m += c[q]
    
    m = title + " " + m

    study_text.append(m)
    
    print(m)
    print(study_text[len(study_text)-1])

    time.sleep(3)

    d = driver.find_element_by_class_name("article_writer")

    time.sleep(3)


    e = d.find_element_by_css_selector("strong.user")
    
    study_nickname.append(e.text)
    
    print(e.text)
    print(study_nickname[len(study_nickname)-1])

    time.sleep(3)

    study_num.append(tex)
    print(tex)
    print(study_num[len(study_num)-1])

    time.sleep(1)

    # 댓글 내용, 닉네임 추출

    tex = k[i] + '댓글'

    f = driver.find_elements_by_class_name("text_comment")
    time.sleep(3)
    g = driver.find_elements_by_class_name("comment_nickname")
    time.sleep(3)
    
    if(len(f)!=0):
        
      for w in range(0,len(f),1):
        if(f[w].text==""):
          continue
        study_text.append(f[w].text)
        print(f[w].text)
        print(study_text[len(study_text)-1])
      
      time.sleep(3)
    
      for w in range(0,len(g),1):
        if(f[w].text==""):
          continue
        study_nickname.append(g[w].text)
        print(g[w].text)
        print(study_nickname[len(study_nickname)-1])
      
      time.sleep(3)

      for w in range(0,len(f),1):
        if(f[w].text==""):
          continue
        study_num.append(tex)
        print(tex)
        print(study_num[len(study_num)-1])
        
      time.sleep(2)
    data_frame = pd.DataFrame({'내용': study_text, '번호': study_num, 'id': study_nickname})
    
    data_frame.to_excel('데이터를 저장할 엑셀파일의 절대경로')   ##수정 필요! 엑셀 파일 끄고 실행해주세요. 안 그러면 파일에 접근이 안 돼요!


# In[ ]:





# In[ ]:




