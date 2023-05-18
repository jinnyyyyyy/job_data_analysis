import plotly.figure_factory as ff
import pandas as pd
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import os 

st.set_page_config(
     page_title="Job Data Analysis App",
     page_icon="📊",
     layout="wide",
     initial_sidebar_state="expanded",
 )

current_file = os.path.abspath(os.path.dirname(__file__))

data = pd.read_csv(current_file+"/../../data/jobkorea_data.csv")

# st.dataframe(data, use_container_width=True)

st.header("2020년, 2021년 공고별 경력,학력조건")
# st.subheader("2020년, 2021년 공고별 경력,학력조건")

with st.sidebar:
    job_ed_list = ['2020년', '2021년']
    job_ed_select = st.selectbox('년도별로 확인', job_ed_list)
    
st.subheader(job_ed_select)


if job_ed_select =='2020년':
    html_file = open(current_file+"\\..\..\data\공고별_경력학력_2020.html", 'r', encoding='utf-8')
    source_code = html_file.read() 
    components.html(source_code,height=500)
    st.markdown('''- 2020년 그래프에서는
    
    경력직을 선호하고, 신입은 약 5% 인것을 확인 할 수 있다. 
    
    학력에서는 무관인 경우가 압도적으로 많았지만, 반대로 고학력일수록 퍼센트는 낮다는 것이 확인된다.''')
else:
    html_file = open(current_file+"\\..\..\data\공고별_경력학력_2021.html", 'r', encoding='utf-8')
    source_code = html_file.read() 
    components.html(source_code,height=500)
    st.markdown('''- 2021년 그래프는
    
    전년도보다 2021년도 공고는 신입의 비율이 0.2% 줄어들고, 여전히 신입 채용은 낮다는 것을 알 수있다.  학력무관이 약 10% 더 늘어난 것을 볼 수 있다.''')