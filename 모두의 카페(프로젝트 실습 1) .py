#!/usr/bin/env python
# coding: utf-8

# # 모두 카페 프로젝트

# ## 3-1 데이터 불러오기
# 

# In[31]:


# 필요 라이브러리 호출하기
# Pandas, Numpy, Matplotlib, Seaborn을 호출해봅니다.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')
import seaborn as sns
import datetime as dt


# In[3]:


# 데이터 호출하기
# 데이터 호출하기
# entry_data.csv, sales_data.csv, item_data.csv, item_entry_data.csv의
# 총 네 가지 파일을 각각 호출합니다.
# 파일들은 본 클라우드에 저장되어있어 다음을 참고하여 호출해주세요.
# entry_data = pd.read_csv('~/aiffel/data_analysis_basic/data/entry_data.csv')
entry_data = pd.read_csv('/aiffel/data/entry_data.csv')
sales_data = pd.read_csv('/aiffel/data/sales_data.csv')
item_data = pd.read_csv('/aiffel/data/item_data.csv')
item_entry_data = pd.read_csv('/aiffel/data/item_entry_data.csv')


# In[4]:


# entry_data 데이터 정보 확인하기
entry_data.head()


# In[5]:


# sales_data 데이터 정보 확인하기
sales_data.head()


# In[6]:


# item_data 데이터 정보 확인하기
item_data.head()


# In[7]:


# item_entry_data 데이터 정보 확인하기
item_entry_data.head()


# ### 3-2 데이터 분석하기
# - 필수 문제 1 : 월별 매출액 추세(sales_data이용)
#     월별 매출액 추세를 집계하고 그 결과를 시각화해보자. *groupby()함수 이용

# In[10]:


# 활용할 데이터(sales_data)를 temp_var로 정의하기
temp_var = sales_data


# In[33]:


# temp_var의 date열을 만들고, sales_date의 결제일시 중 앞에서 7번째 값까지 할당
temp_var['date'] = sales_data['결제일시'].str[0:7]


# In[12]:


# salse_data의 결제금액에 포함된 쉼표(,) 지우기
# -> salse_data의 결제금액에 쉼표가 들어있어서
#문자열로 인식되고 있기때문에 지워서 숫자로 변경해주기
sales_data['결제금액'] = sales_data['결제금액'].str.replace(',', '')


# In[13]:


# salse_data의 결제금액을 숫자형태로 바꾸기
temp_var['payment'] = sales_data['결제금액'].astype(int)


# In[14]:


# temp_var의 payment열을 date 기준으로 집계하기
payment_data = temp_var['payment'].groupby(temp_var['date']).sum()
payment_data


# In[15]:


# 집계 결과를 시각화하기
ax = payment_data.plot(kind='bar')

plt.title('Sales By Months')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()


# - 필수문제 2 : 가장 인기있는 음식/음료(salses_data 이용)
# 여러 메뉴들(음식, 음료)을 판매 개수 순으로 정렬하고 상위 10개를 뽑아 결과를 시각화해보자.

# In[16]:


# temp_var의 상품명을 value_counts를 이용해 집계하기
items_count = temp_var[temp_var['판매수량']!=-1].value_counts()
items_count


# In[17]:


# 집계 결과를 데이터프레임으로 변환하고, 상위 10개 선정하기
items_count = pd.DataFrame(items_count)
items_count[:10]


# In[18]:


# 한글이 포함된 시각화를 위해 Matplotlib 설정
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=9)
plt.rc('font', family='NanumBarunGothic') 
mpl.font_manager.findfont(font)
print("완료!")


# In[20]:


# 집계 결과를 시각화하기
items_count[:10].plot(kind='bar')
plt.ylabel('개')
plt.title('판매 개수')
plt.show()


# - 여러 메뉴들(음식,음료)을 판매 매출(판매 개수 x 결제 금액) 순으로 정렬하고 상위 10개를 뽑아 결과를 시각화해봅니다.
# 

# In[22]:


# temp_var의 payment열을 상품명을 기준으로 집계하기
items_payment = temp_var['payment'].groupby(temp_var['상품명'][temp_var['판매수량']!=-1]).sum()
items_payment


# In[23]:


# item_payment의 값을 내림차순으로 정렬하고 상위 10개 도출하기
items_payment = items_payment.sort_values(ascending=False)
items_payment[:10]


# In[24]:


# 집계 결과 시각화하기
items_payment[:10].plot(kind='bar')
plt.ylabel('원')
plt.title('판매 금액')
plt.show()


# - 필수 문제3: 가장 많이 팔린 입장권 종류(entry_data를 이용합니다.)
# 여러 입장권 종류를 판매 매출(판매 개수 x 금액) 순으로 정렬하고 상위 10개를 뽑아 결과를 시각화해봅니다.

# In[25]:


# 활용할 데이터(entry_data)를 temp_var로 정의하기
temp_var = entry_data
temp_var


# In[26]:


# temp_var의 금액을 숫자형태로 변환하기
temp_var['금액'] = temp_var['금액'].astype(int)


# In[27]:


# temp_var의 금액을 요금제명을 기준으로 집계하기
tickets = temp_var['금액'].groupby(temp_var['요금제명']).sum()
tickets


# In[28]:


# tickets의 값을 내림차순으로 정렬하고 상위 10개 도출하기
tickets = tickets.sort_values(ascending=False)
tickets[:10]


# In[29]:


# 집계 결과 시각화하기
tickets[:10].plot(kind='bar')
plt.ylabel('원')
plt.title('입장권별 판매금액')
plt.show()


# ### 회고
# - 아직 함수의 종류에 대해 미숙한 것 같다. 
# - 어떤 상황이 주어졌을 때, 어떤 함수를 사용해야할지가 잘 떠오르지 않는다. -> 더 많이 써보고 익숙해져야 할 것 같다. 
# - 오타가 너무 많다(오류의 대부분 원인 .. 오타)
# - str[]이 생각보다 많이 쓰이는데, 잘 생각해내지 못했다.. 확인확인
# - 쉼표를 지워서 문자열을 숫자로 바꿔주는데, replace함수를 사용한다는 것이 신박했다! del일줄 알았음. 왜 대체로 하지? 지우는건 안되나?
# - 어떨때 ax= 을 쓰고 어떨때 안쓰는 거지 ? 
# 

# In[ ]:




