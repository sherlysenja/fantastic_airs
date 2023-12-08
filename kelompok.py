#Sherly mengerjakan impor data frame, membuat judul, dan histogram gender
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('shoppingtrends.csv', sep =',')

st.header("Data Tren Belanja Di Amerika:shopping_trolley:", divider = 'red')
st.subheader('Data ini disusun oleh _:blue[Fantastic_Airs]_:fire:')
st.write("""
#### Nama Anggota:
##### Azizah Amelia Eka Susanti (02100221402)
##### Indah Triend Elisabeth (021002101001
##### Rania Yasmin (021002214010)
##### Sherly Senja Rindiani (021002214011)

""")

st.dataframe(df)

st.write("# Tren Belanja Berdasarkan Gender")
plot_gender = px.histogram(df,
                           x = 'Gender',
                           title = 'Histogram Tren Belanja Berdasarkan Gender')
plot_gender.update_layout(
    xaxis_title = 'Gender',
    yaxis_title = 'Jumlah')
st.plotly_chart(plot_gender)
with st.expander("Lihat Penjelasan"):
    st.write("Grafik ini menunjukkan bahwa Laki-laki lebih sering belanja dibandingkan perempuan.")

#Azizah Amelia mengerjakan multi select season dan histogram dengan berbagai opsi
Season_dict= st.multiselect('Season',
                            options= ['Winter', 'Spring', 'Fall', 'Summer'],
                            default=['Fall'] )

st.markdown(f"Data Berdasarkan Item Purchased Per Season :")
st.write( df[df['Season'] == 'Fall'])

attributes = st.selectbox("Pilih Data yang dibutuhkan:", 
                               options = ['Age', 'Gender', 'Item Purchased', 'Category', 'Purchase Amount (USD)', 'Location', 'Size', 'Color', 'Season', 'Review Rating', 'Subscription', 'Status', 'Shipping', 'Type', 'Discount', 'Applied', 'Promo', 'Code', 'Used', 'Previous', 'Purchases', 'Payment Method', 'Frequency of Purchases'])

st.plotly_chart(
    px.histogram(
        df,
        x = attributes,
        title = 'Line Chart Item Purchased'))

#Indah mengerjakan visualisasi Purchased Amount berdasarkan Payment Method
fig = px.pie(df, values = 'Purchase Amount (USD)', names='Payment Method', title='Purchased Amount berdasarkan Peyment Methond',color_discrete_sequence=px.colors.qualitative.Antique)
st.plotly_chart(fig)
with st.expander("Lihat Penjelasan"):
    st.write("Grafik ini menunjukkan bahwa lebih banyak orang berbelanja dengan metode pembayaran Credit Card")
    
