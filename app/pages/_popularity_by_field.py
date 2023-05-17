import plotly.express as px
import pandas as pd
import streamlit as st
from PIL import Image
import os
from collections import Counter

st.set_page_config(
     page_title="Job Data Analysis App",
     page_icon="📊",
     layout="wide",
     initial_sidebar_state="expanded",
 )

current_file = os.path.abspath(os.path.dirname(__file__))

data3 = pd.read_csv(current_file+"\\..\..\data\jobkorea_data.csv")
data_2020 = pd.read_csv(current_file+"\\..\..\data/data_2/data_2020.csv")
data_2021 = pd.read_csv(current_file+"\\..\..\data/data_2/data_2021.csv")

data_list = [data_2020, data_2021]

# 사이드바
year_list = ['2020년','2021년']
year_select = st.sidebar.selectbox('년도별 공고 키워드 빈도수', year_list)
#st.write(year_select)
st.title('년도별 :red[공고 키워드] 빈도수 비교')
st.subheader(year_select)


img_ida = year_list.index(year_select)

folder = current_file+"\\..\..\data\data_1/"
# 서로 다른 리스트를 묶어서 하나처럼 사용하려면 같은 인덱스에 있음을 이용하면 됩니다 
image_files = ['2020년공고키워드.PNG', '2021년공고키워드.PNG']
#  
image_path = folder + image_files[img_ida]
image = Image.open(image_path) # 경로와 확장자 주의!
st.image(image)


def frequency(x):
    #data_2020 = frequency()
    key_list = x['해당채용공고키워드명'].values.tolist()
    #key_list

    result_list = []
    for i in range(0, len(key_list)):
        result_list += key_list[i].split(',')
    #result_list

    #Counter module을 이용해 키워드 빈도수 계산
    count_2020 = Counter(result_list)
    #count_2020 #2020년의 키워드별 빈도수 dictionary

    #count_keywords의 key와 value 추출(리스트로 변횐돰)
    keys2 = list(count_2020.keys())
    values2 = list(count_2020.values())

    #데이터프레임 만들기
    keywords_df2 = pd.DataFrame({'공고 키워드명':keys2,
                          '빈도수':values2})
    keywords_df2=keywords_df2.sort_values(by='빈도수', ascending=False)
    st.dataframe(keywords_df2.head(), use_container_width=True)



st.divider()  # 👈 Draws a horizontal rule
st.subheader(year_select+"의 채용 공고 키워드 TOP5❗")
if year_select =='2020년':
    frequency(data_2020)
else:
    frequency(data_2021)

#st.dataframe(keywords_df2, use_container_width=True)
if year_select =='2020년':
    st.write('''- 2021년의 채용공고에는 ‘물류’, ‘부동산개발’, ‘컴퓨터’, ‘문서관리’ ,’유지보수’ 키워드가 많이 나옴''')
    st.divider()  # 👈 Draws a horizontal rule
    st.subheader(year_select+"TOP5 키워드별 직업군")
    st.write('''

- 물류 직업군 : 배송납품 직원
- 부동산 개발 : 부동산 컨설턴트, 자산관리
- 컴퓨터, 유지보수 : 데이터복구, 컴퓨터 설치
- 문서관리: 사무직, 인사총무''')
else:
    st.write('''- 2020년의 채용공고에는 ‘생명보험’, ‘보험영업’, ‘손해보험’ ,’컴퓨터’, ‘물류’ 키워드가 많이 나옴''')
    st.divider()  # 👈 Draws a horizontal rule
    st.subheader(year_select+"TOP5 키워드별 직업군")
    st.write('''

- 생명보험, 보험영업, 손해보험 : 보험 사무 보조원, 금융설계사, 금융전문가
    
      * 보험영업이지만 사무보조원 파트타임 업무가 많은 것으로 확인됨
    
- 컴퓨터, 물류는 2020년 직업군과 동일''')