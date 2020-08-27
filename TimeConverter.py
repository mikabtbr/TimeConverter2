def konversi(detik):  # function konversi dengan parameter detik

    detik = detik % (24 * 3600)  # variabel detik dimana di konversi kan terhadap detik per jam (24 jam dikali 3600 detik)
    jam = detik // 3600          # variabel detik di konversikan terhadap jam
    detik %= 3600                
    menit = detik // 60          # variabel menit dimana konversi menit terhadap detik
    detik %= 60
      
    return "%d:%02d:%02d" % (jam, menit, detik)  #memanggil hasil dengan format HH:MM:SS (jam, menit, detik)
      

print(konversi(3600))  # memanggil fungsi dengan isi parameternya