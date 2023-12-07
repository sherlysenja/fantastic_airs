import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('shopping_trends.csv')

st.write("""
# Customer Shopping Trends Dataset

## Kelompok : fantastic_airs

### Nama Anggota:
###### Sherly Senja Rindiani (021002214011)
###### Rania Yasmin (021002214010)
###### Indah Triend Elisabeth (021002101001)
###### Azizah Amelia Eka Susanti (02100221402)


""")

Season_dict= st.multiselect('Season',
                            options= ['Winter', 'Spring', 'Fall', 'Summer'],
                            default=['Fall'] )

st.markdown(f"Data Berdasarkan Item Purchased Per Season :")
st.write( df[df['Season'] == 'Fall'])

attributes = st.selectbox("Pilih Data yang dibutuhkan:", 
                               options = ['Age', 'Gender', 'Item Purchased', 'Category', 'Purchase Amount (USD)', 'Location', 'Size', 'Color', 'Season', 'Review', 'Rating', 'Subscription', 'Status', 'Shipping', 'Type', 'Discount', 'Applied', 'Promo', 'Code', 'Used', 'Previous', 'Purchases', 'Payment Method', 'Frequency of Purchases'])

st.plotly_chart(
    px.histogram(
        df,
        x = attributes,
        title = 'Line Chart Item Purchased'))

