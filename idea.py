import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
#import tkinter
import numpy as np

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'>Kemiskinan dan Stunting di Kabupaten Bekasi Tahun 2021</h1>", unsafe_allow_html=True)
#st.title("Kemiskinan dan Stunting di Kabupaten Bekasi Tahun 2021")
st.markdown("<h4 style='text-align: center; color: blue;'>Ambar Widi Sayekti - Capstone Project TETRIS 2022</h4>", unsafe_allow_html=True)
#st.write("Ambar Widi Sayekti - Capstone Project TETRIS 2022")



st.write("____________________________________________________________________________________________________________________")

c1, c2= st.columns(2)
with c1:
    st.write("**Kemiskinan** adalah keadaan saat ketidakmampuan untuk memenuhi kebutuhan dasar seperti makanan, pakaian, tempat berlindung, pendidikan, dan kesehatan. Kemiskinan dapat disebabkan oleh kelangkaan alat pemenuh kebutuhan dasar, ataupun sulitnya akses terhadap pendidikan dan pekerjaan. Kemiskinan merupakan masalah global.")
with c2:
    st.write("**Stunting** merupakan masalah kurang gizi kronis yang disebabkan oleh kurangnya asupan gizi dalam waktu yang cukup lama, sehingga mengakibatkan gangguan pertumbuhan pada anak yakni tinggi badan anak lebih rendah atau pendek (kerdil) dari standar usianya.")

# Deklarasi dataset Jumlah Penduduk Miskin
df_miskin= pd.read_excel("jumlah_penduduk_miskin_2021n.xlsx");
#st.write("Tabel jumlah_penduduk_miskin_2021 tahun 2021.")
df_miskin_u=df_miskin.sort_values(['Jumlah Penduduk Miskin','Jumlah Penduduk'],ascending=False)
#st.dataframe(df_miskin_u)
#st.dataframe(df_miskin.sort_values(['Jumlah Penduduk','Jumlah Penduduk Miskin'],ascending=False))
#st.area_chart(df_miskin_u.sort_values(['Jumlah Penduduk','Jumlah Penduduk Miskin'],ascending=False).groupby('Kecamatan').sum())
#st.area_chart(df_miskin_u.groupby('Kecamatan').sum().sort())
st.write("**Data Jumlah Penduduk Miskin di Kabupaten Bekasi pada tahun 2021.**")
st.bar_chart(df_miskin_u.groupby('Kecamatan').sum().nlargest(n=23,columns=['Jumlah Penduduk Miskin','Jumlah Penduduk']))
st.write("Dari data tersebut, menunjukan bahwa masih terdapat penduduk di Kabupaten Bekasi yang termasuk dalam kategori miskin. Kecamatan Pebayuran merupakan kecamatan dengan jumlah penduduk miskin tertinggi, yakni: 30322. Disusul kecamatan Karang Bahagia (18954), dan kecamatan Babelan(16279).")
#df_miskin = df_miskin.sort_values(by='', ascending=True)
#cusips_df = cusips_df.groupby(['cusip'], as_index=False).agg({"principal":sum})

print('1 ===========================')
df_miskin.info()
print('2 ===========================')
print(df_miskin.describe())
print('3 ===========================')
print(df_miskin.corr())
print('4 ===========================')
#jumlah kecamatan
#n_kecamatan= df_miskin['Kecamatan'].nunique()
#print(n_kecamatan)
#print('5 ===========================')
#st.line_chart(df_miskin.groupby('Kecamatan').sum())
#print('6 ===========================')

#group berdasarkan Klasifikasi Desa IBM
#print(df_miskin.groupby(['Kecamatan','Klasifikasi Desa IDM']).sum())
#st.write("**Tabel Data Penduduk Miskin di Kabupaten Bekasi berdasarkan Klasifikasi Desa IDM pada tahun 2021.**")
#st.dataframe(df_miskin.groupby(['Kecamatan','Klasifikasi Desa IDM']).sum())
#st.bar_chart(df_miskin.groupby(['Kecamatan','Klasifikasi Desa IDM']).sum().nlargest(n=23,columns=['Jumlah Penduduk Miskin','Jumlah Penduduk']))
#df_miskin_group=df_miskin.groupby(['Kecamatan','Klasifikasi Desa IDM']).sum()
#st.line_chart(df_miskin_group)
#print('7 ===========================')
#data 3 kecamatan yg menunjukan jumlah penduduk miskin tertinggi
#st.write("Tabel 3 Kecamatan dengan Jumlah Data Penduduk Miskin Tertinggi pada tahun 2021.")
#df_miskin.groupby('Kecamatan').sum().nlargest(n=3,columns=['Jumlah Penduduk Miskin'])
#print(df_miskin.groupby('Kecamatan').sum().nlargest(n=10,columns=['Jumlah Penduduk Miskin']))
#st.write(df_miskin.groupby('Kecamatan').sum().nlargest(n=10,columns=['Jumlah Penduduk Miskin']))
#print('8 ===========================')
#data 3 kecamatan yg menunjukan jumlah penduduk miskin terrendah
#st.write("Tabel 3 Kecamatan dengan Jumlah Data Penduduk Miskin Terendah pada tahun 2021.")
#df_miskin.groupby('Kecamatan').sum().nsmallest(n=3,columns=['Jumlah Penduduk Miskin'])
#print(df_miskin.groupby('Kecamatan').sum().nsmallest(n=10,columns=['Jumlah Penduduk Miskin']))
#st.write(df_miskin.groupby('Kecamatan').sum().nsmallest(n=10,columns=['Jumlah Penduduk Miskin']))
#print('9 ===========================')
#print(pd.pivot_table(
#    data=df_miskin,
#    index=['Kecamatan'],
#    columns=['Klasifikasi Desa IDM'],
#    values=['Jumlah Penduduk Miskin'],
#    aggfunc='sum',
#    fill_value=0
#))
st.write("____________________________________________________________________________________________________________________")

c3, c4= st.columns(2)
with c3:
    df_miskin_idm= pd.read_excel("jumlah_penduduk_miskin_2021n_idm.xlsx");
    st.write('**Tabel 3 Kecamatan dengan data penduduk miskin tertinggi di Kabupaten Bekasi berdasarkan Klasifikasi Desa IDM pada tahun 2021**')
    st.write(pd.pivot_table(
    data=df_miskin_idm,
    index=['Kecamatan'],
    columns=['Klasifikasi Desa IDM'],
    values=['Jumlah Penduduk Miskin'],
    aggfunc='sum', 
    fill_value=0)
    )   
    
with c4:
    st.write('Dalam pengukuran status desa oleh Kemendes, terdapat lima klasifikasi status desa dalam Indeks Desa Membangun (IDM). Lima status itu adalah:')
    st.write('(1) Desa Sangat Tertinggal; ')
    st.write('(2) Desa Tertinggal;')
    st.write('(3) Desa Berkembang; ')
    st.write('(4) Desa Maju; ')
    st.write('(5) Desa Mandiri')
    st.write('Kecamatan Pebayuran merupakan kecamatan dalam IDM, Berkembang. Disusul kecamatan Karang Bahagia dalam IDM (Berkembang), dan kecamatan Babelan dalam IDM (sebagian Berkembang dan sebagian Maju).')
 
st.write("____________________________________________________________________________________________________________________")

print('10 ===========================')

#st.write('Tabel Persentase')
#df_miskin_persen=df_miskin.insert(5, 'Persentase', (df_miskin['Jumlah Penduduk Miskin']/df_miskin['Jumlah Penduduk'])*100)
#df_akhir = df_miskin.assign(Persentase=((df_miskin['Jumlah Penduduk Miskin']/df_miskin['Jumlah Penduduk'])*100))
#st.write(df_miskin_persen)
#print('11 ===========================')

# Deklarasi dataset rekap_data_stunting
print('***************************************************')
df_stunting= pd.read_excel("rekap_data_stunting_2021n.xlsx");
#st.write("Tabel rekap_data_stunting_2021 tahun 2021.")
#st.dataframe(df_stunting)
print('1 ******************************')
df_stunting.info()
print('2 ******************************')
print(df_stunting.describe())
print('3 ******************************')
print(df_stunting.corr())
print('4 ******************************')
#n_kecamatan_s= df_stunting['Kecamatan'].nunique()
#print(n_kecamatan_s)
print('5 ******************************')
#print(df_stunting.groupby('Kecamatan').sum())
st.write("**Data Stunting di Kabupaten Bekasi tahun 2021.**")
st.line_chart(df_stunting.groupby('Kecamatan').sum())
st.write("Berikut adalah data stunting di kabupaten Bekasi pada tahun 2021. Menunjukan bahwa masih terdapat balita yang termasuk dalam kategori stunting. Kecamatan Setu merupakan kecamatan dengan jumlah balita stunting tertinggi, yakni: 1751. Disusul kecamatan Cikarang Utara (1254), dan kecamatan Cibarusah (1018).")
print('6 ******************************')
#group berdasarkan Puskesmas
#print(df_stunting.groupby(['Kecamatan','Puskesmas']).sum())
#st.write("Tabel rekap_data_stunting berdasarkan Puskesmas pada tahun 2021.")
#st.dataframe(df_stunting.groupby(['Kecamatan','Puskesmas']).sum())

print('7 **********************************')
#data 3 kecamatan yg menunjukan jumlah stunting tertinggi
#st.write("Tabel 3 Kecamatan dengan Jumlah Data Stunting Tertinggi pada tahun 2021.")
#print(df_stunting.groupby('Kecamatan').sum().nlargest(n=10,columns=['Total Stunting']))
#st.write(df_stunting.groupby('Kecamatan').sum().nlargest(n=10,columns=['Total Stunting']))
#print('8 **********************************')
#data 3 kecamatan yg menunjukan jumlah penduduk miskin terrendah
#st.write("Tabel 3 Kecamatan dengan Jumlah Data Stunting Terendah pada tahun 2021.")
#print(df_stunting.groupby('Kecamatan').sum().nsmallest(n=10,columns=['Total Stunting']))
#st.write(df_stunting.groupby('Kecamatan').sum().nsmallest(n=10,columns=['Total Stunting']))
#print('9 ************************************')
#print(pd.pivot_table(
#    data=df_stunting,
#    index=['Kecamatan'],
#    columns=['Puskesmas'],
#    values=['Total Stunting'],
#    aggfunc='sum',
#    fill_value=0
#))
#st.write('Tabel Data Penduduk Stunting berdasarkan Puskesmas pada tahun 2021')
#st.write(pd.pivot_table(
#    data=df_stunting,
#    index=['Kecamatan'],
#    columns=['Puskesmas'],
#    values=['Total Stunting'],
#    aggfunc='sum',
#    fill_value=0
#))

st.write("____________________________________________________________________________________________________________________")

#df_row = pd.concat([df_miskin, df_stunting])
df_row = pd.concat([df_stunting,df_miskin])
#df_row_u = pd.merge([df_miskin, df_stunting],right_index=True, left_index=True)
#st.dataframe(df_row_u)
print(df_row)
st.write("**Data Penduduk Miskin dan Sunting di kabupaten Bekasi pada tahun 2021.**")
#st.dataframe(df_row)
#st.write("Data Penduduk Miskin dan Sunting di kabupaten Bekasi pada tahun 2021.")
#st.bar_chart(df_row.groupby('Kecamatan').sum())
#st.write("Data Penduduk Miskin dan Sunting di kabupaten Bekasi pada tahun 2021.")
st.area_chart(df_row.groupby('Kecamatan').sum())
st.write('Menteri Koordinator Bidang Pembangunan Manusia dan Kebudayaan (Menko PMK) Muhadjir Effendy menjelaskan, kunci untuk menurunkan stunting adalah penanganan kemiskinan. Menurutnya, kemiskinan merupakan salah satu penyebab ibu dan anak tak memeroleh gizi yang cukup.')
st.write(' "Memang tidak semua orang miskin anaknya stunting. Tapi sebagian besar stunting itu diakibatkan karena kemiskinan. Dan karena itu kemiskinan itu yang harus ditangani," ujar Menko PMK."')
st.write('Lebih lanjut Menko PMK mengatakan, kaitan antara kemiskinan dan munculnya stunting pada anak sangat erat. Apalagi di masa pandemi Covid-19, angka kemiskinan juga mengalami peningkatan. Karena itu, pemerintah menggelontorkan berbagai stimulus agar kemiskinan bisa teratasi. Seperti program Bantuan Sosial, Bantuan Langsung Tunai (BLT), program sembako, dan Program Keluarga Harapan (PKH).')
st.write("____________________________________________________________________________________________________________________")

st.write('**Kesimpulan dan Saran Rekomendasi**')
st.write(' - Pemerintah perlu usaha berkelanjutan untuk mengatasi tingkat kemiskinan masyarakat, sehingga jumlah anak stunting juga ikut berkurang.')
st.write(' - Masyarakat perlu di edukasi dan difasilitasi oleh pemerintah, sehingga masyarakat punya kesadaran bahwa pentingnya kecukupan Gizi bagi tumbuh kembang anak. Karena Stunting merupakan ancaman utama terhadap kualitas manusia Indonesia, juga ancaman terhadap kemampuan daya saing bangsa.')


st.write('**Sumber Data:**')
st.write(' - http://opensatudata.bekasikab.go.id')
st.write(' - https://www.kemenkopmk.go.id/')
st.write(' - https://kanaldesa.com')
# Deklarasi dataset Data Fasilitas Kesehatan tahun 2021
#print('***************************************************')
#df_faskes= pd.read_excel("Data_Fasilitas_Kesehatan.xlsx");
#st.write("Tabel Data Fasilitas Kesehatan tahun 2021.")
#st.dataframe(df_faskes)
#print('1 ******************************')
#df_faskes.info()
#print('2 ******************************')
#print(df_faskes.describe())
#print('3 ******************************')
#print(df_faskes.corr())
#print('4 ******************************')
#st.bar_chart(df_faskes.groupby('Kecamatan').sum())
#print('5 ******************************')
#print(df_faskes.groupby('Kecamatan').sum())
#st.write("Data faskes tahun 2021.")
#st.line_chart(df_faskes.groupby('Kecamatan').sum())
#print('6 ******************************')


#from sklearn.cluster import KMeans
#model cluster= KMens(n_cluster=3)
#model_cluster.fit(data)
#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report
#df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
#pr = df.profile_report()
#st_profile_report(pr)
#report = ProfileReport(df_miskin)
#df_miskin.to_file('report.html')
