lanjut = "y"
while lanjut.lower() == "y":
    print("======================")
    print("SIMPLE CODE CALCILATOR")
    print("======================")
    #INPUT DATA USER
    angka1 = int(input("Masukan angka Pertama: "))
    Opr = input('Operasi yang dipilih "+"-"/"*": ')
    angka2 = int(input("Masukan angka kedua: "))
    
    #OPERASI PENJUMLAHAN
    if Opr == "+":
        hasil = angka1+angka2
        print ("Hasil dari penjumlahan",angka1,Opr,angka2,"adalah",hasil)
    #OPERASI PENGURANGAN
    elif Opr == "-":
        hasil = angka1-angka2
        print ("Hasil dari pengurangan",angka1,Opr,angka2,"adalah",hasil)
    #OPERASI PEMBAGIAN    
    elif Opr == "/":
        hasil = angka1/angka2
        print ("Hasil dari pembagian",angka1,Opr,angka2,"adalah",hasil)
    #OPERASI PERKALIAN
    elif Opr == "*":
        hasil = angka1*angka2
        print ("Hasil dari perkalian",angka1,Opr,angka2,"adalah",int(hasil))
    else:
        print("ERROR MAMPUSSS!!!")
    print("======================")
    #INPUT DATA KONFIRMASI    
    lanjut = input("Mau lanjut berhitung?  y/n : ")
    if lanjut == 'n':
        print("HAVE A GREAT DAYY~ SEMANGAT BELAJARR")
        break
