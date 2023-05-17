import plotly.express as px
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
     page_title="Job Data Analysis App",
     page_icon="📊",
     layout="wide",
     initial_sidebar_state="expanded",
 )

st.title(':blue[분야]별 :blue[급여] 차이 비교')

current_file = os.path.abspath(os.path.dirname(__file__))

tab_yearly, tab_monthly, tab_daily = st.tabs(('연봉 막대 그래프', '월급 분산차트', '단기급여 분산차트'))

with tab_yearly:
    html_file = open(current_file+"\\..\..\data\domain_by_salary_yearly.html", 'r', encoding='utf-8')
    source_code = html_file.read() 
    components.html(source_code,height=400)
    st.code('''# 인바운드tm, 대출tm, 모바일 게임, 부동산, 법인컨설팅, 신용애널리스트 등의 직군에서 높은 연봉이 제시되었고,
# 전기, AR/VR개발자, 기계 설비 등이 그 다음,
# 사무보조, 요리사, 조리사 등의 직군에서는 낮은 연봉이 제시되었다.''')

with tab_monthly:
    html_file = open(current_file+"\\..\..\data\domain_by_salary_monthly.html", 'r', encoding='utf-8')
    source_code = html_file.read() 
    components.html(source_code,height=400)
    st.code('''#월급과 단기급여 분산차트에서는 동일 업종에서 구직업체별로
# 급여 차이가 큰 업종과 업체들 간 급여 차이가 적은 업종의 차이를 확인할 수 있었다.
# 또한 월급 분산차트와 단기급여 분산차트의 비교를 통해
# 월급을 기준으로 구인하는 업종과 단기급여를 기준으로 구인하는 업종의 차이의 확인이 가능했다.''')

with tab_daily:
    html_file = open(current_file+"\\..\..\data\domain_by_salary_daily.html", 'r', encoding='utf-8')
    source_code = html_file.read() 
    components.html(source_code,height=400)
    st.code('''#월급과 단기급여 분산차트에서는 동일 업종에서 구직업체별로
# 급여 차이가 큰 업종과 업체들 간 급여 차이가 적은 업종의 차이를 확인할 수 있었다.
# 또한 월급 분산차트와 단기급여 분산차트의 비교를 통해
# 월급을 기준으로 구인하는 업종과 단기급여를 기준으로 구인하는 업종의 차이의 확인이 가능했다.''')
