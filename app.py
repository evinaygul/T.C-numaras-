import streamlit as st

# Sitenin Başlığı ve Görseli
st.title("🛡️ T.C. Kimlik No Güvenlik Analizi")
st.subheader("Algoritma Çözücü ve Prototip")

st.write("""
Bu araç, T.C. Kimlik numaralarının matematiksel algoritmasını kullanarak 
güvenlik zafiyetlerine dikkat çekmek için tasarlanmıştır.
""")

# Kullanıcıdan Giriş Al
tc_input = st.text_input("Kimlik numaranızın İLK 9 HANESİNİ giriniz:", max_chars=9)

if len(tc_input) == 9 and tc_input.isdigit():
    # Matematiksel Hesaplama (Algoritma)
    r = [int(d) for d in tc_input]
    
    # 10. Hane Hesabı
    tekler = r[0] + r[2] + r[4] + r[6] + r[8]
    ciftler = r[1] + r[3] + r[5] + r[7]
    hane10 = ((tekler * 7) - ciftler) % 10
    
    # 11. Hane Hesabı
    hane11 = (sum(r) + hane10) % 10
    
    # Sonuçları Ekranda Göster
    st.success(f"Analiz Tamamlandı!")
    st.metric("Hesaplanan 10. Hane", hane10)
    st.metric("Hesaplanan 11. Hane", hane11)
    
    st.info(f"Oluşturulan Tam Numara: {tc_input}{hane10}{hane11}")
    
    st.warning("⚠️ NOT: Bu durum, kimlik numaranızın matematiksel olarak tahmin edilebilir olduğunu kanıtlar.")
else:
    st.write("Lütfen tam olarak 9 rakam giriniz.")
