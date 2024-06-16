import streamlit as st
import pandas as pd
import random
import datetime
from template import *

st.set_page_config(
    page_title = 'Dashboard',
    page_icon = None,
    layout = 'wide',
    initial_sidebar_state = 'auto')
st.markdown('##')
UI()
st.markdown('##')

today_date = datetime.date.today()
random_num = random.randint(0, 1000)

df = pd.read_excel('data.xlsx', sheet_name = 'Sheet1')
df['date_added'] = pd.to_datetime(df['date_added'])
st.dataframe(data = df, use_container_width = True)

def Analytics():
 purchasing_price_ = float(df['purchasing_price'].sum())
 selling_price_ = float(df['selling_price'].sum())
 profit = float(df['expected_profit'].sum())

 tot1, tot2, tot3= st.columns(3,gap='small')
 with tot1:

    st.info('Purchasing Price', icon="🔍")
    st.metric(label = 'TZS', value= f"{purchasing_price_:,.0f}")
    
 with tot2:
    st.info('Selling Price', icon="🔍")
    st.metric(label='TZS', value=f"{selling_price_:,.0f}")

 with tot3:
    st.info('Expected Profit', icon="🔍")
    st.metric(label= 'TZS',value=f"{profit:,.0f}")

Analytics()

st.sidebar.header('Add New Product')
opt_form = st.sidebar.form('Option Form')
pr_name = opt_form.text_input('Name')
pr_category = opt_form.selectbox('Category', ('Soap', 'Perfume', 'Lotion', 'Other'))
pr_type = opt_form.selectbox('Type', ('new', 'used'))
serial_num = opt_form.text_input("ID", value=random_num,disabled=True)
date_added=opt_form.text_input("Registered", value=today_date, disabled=True)
purchasing_price=opt_form.number_input("Purchasing price")
selling_price=opt_form.number_input("Selling Price")
add_data=opt_form.form_submit_button(label="Add new record")

if pr_name != '':
    df = pd.concat([df, pd.DataFrame.from_records([{
        'product_name': pr_name,
        'type': pr_type,
        'category': pr_category,
        'date_added': date_added,
        'ID': serial_num,
        'purchasing_price': purchasing_price,
        'selling_price': selling_price,
        'expected_profit': selling_price - purchasing_price
    }])])
    try:
        df.to_excel("data.xlsx", index=False)
    except:
        st.warning('Unable to write, close your dataset')
else:
    st.sidebar.error('Product Name required')

with st.expander("Records"):
   shwdata = st.multiselect('Filter: ', df.columns, default = [
      'product_name', 'type', 'category', 'date_added', 'ID',
      'purchasing_price', 'selling_price', 'expected_profit'
   ])
   st.dataframe(df[shwdata], use_container_width = True)

with st.expander('Cross Tab'):
   tab = pd.crosstab([df.category], df.type, margins = True)
   st.dataframe(tab)


