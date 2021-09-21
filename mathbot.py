from random import randint

# list-list penting untuk printing dan control flow
listNamaKuis = ['penjumlahan','pengurangan','campur','akhiri program']
listNomorKuis = ['1','2','3','4']
listNomorJenis = ['1','2','3','4']
# menu
def main():
    # menu pertama: meminta user untuk memilih salah satu mode kuis atau mengakhiri program
    modeKuis = input('Halo, selamat datang di Mathbot\nPilih mode:\n(1) Penjumlahan\n(2) Pengurangan\n(3) Campur\n(4) Akhiri program\n\nMasukkan perintah: ')
    # meminta input ulang jika input yang diberikan di luar pilihan
    while modeKuis not in listNomorKuis:
        print('\nInput salah!')
        modeKuis = input('\nMasukkan perintah: ')
    else:
        # jika user memilih salah satu dari tiga mode kuis, program lanjut ke menu kedua
        if listNomorKuis.index(modeKuis) != 3:
            # menu kedua: meminta user untuk memilih salah satu jenis kuis, kembali ke menu pertama, atau mengakhiri program
            print('\nBaik, pilih mode',listNamaKuis[eval(modeKuis)-1],'ya, sekarang pilih jenis kuis apa?')
            jenisKuis = input('''Pilih kuis:\n(1) Kuis Lepas\n(2) Kuis 5\n(3) Ganti mode\n(4) Akhiri program\n\nMasukkan jenis kuis: ''')
            while jenisKuis not in listNomorJenis:
                print('\nInput salah!')
                jenisKuis = input('\nMasukkan jenis kuis: ')
            else:
                # jika user memilih 1 atau 2, program menjalankan kuis sesuai pilihan mode dan jenis kuis
                if jenisKuis == '1':
                    print("\n(ketik 'akhiri kuis' untuk kembali ke menu)")
                    kuisLepas(modeKuis)
                elif jenisKuis == '2':
                    kuis5(modeKuis)
                # jika user memilih 3, maka kembali ke menu pertama
                elif jenisKuis == '3':
                    print('\n')
                    main()
                # jika user memilih 4 pada menu kedua, maka program diakhiri
                else:
                    endGame()
        # jika user memilih 4 pada menu pertama, maka program diakhiri
        else:
            endGame()
# menjalankan kuis lepas sesuai mode kuis yang dipilih
def kuisLepas(n):
    if n == '1':
        penjumlahan(1)
    elif n == '2':
        pengurangan(1)
    else:
        campur(1)
    print('\n')
    main()
# menjalankan kuis 5 nomor sesuai mode kuis yang dipilih
def kuis5(n):
    if n == '1':
        penjumlahan(2)
    elif n == '2':
        pengurangan(2)
    else:
        campur(2)
    print('\n')
    main()
# modul kuis penjumlahan
def penjumlahan(n):
    # kuis lepas
    if n == 1:
        while True:
            num1 = randint(1,10)
            num2 = randint(1,10)
            print('\nPertanyaan: ',num1,' + ',num2,sep='')
            ans1 = str(input('Jawab: '))
            if ans1 == 'akhiri kuis':
                break
            elif ans1.isdigit():
                if eval(ans1) == num1+num2:
                    print("\nBenar!")
                else:
                    print("\nSalah! Jawabannya ",num1+num2,'.',sep='')
            else:
                print('\nInput Salah!')
    # kuis 5 nomor
    else:
        skor = 0
        for i in range (1,6):
            num1 = randint(1,10)
            num2 = randint(1,10)
            print('\nPertanyaan ',i,': ',num1,' + ',num2,sep='')
            ans1 = str(input('Jawab: '))
            if ans1 == num1+num2:
                if eval(ans1) == num1+num2:
                    print("\nBenar!")
                    skor += 20
                else:
                    print("\nSalah! Jawabannya ",num1+num2,'.',sep='')
            else:
                print('\nInput salah!')
        print('\nSkor kamu:',skor)
        input('(tekan enter untuk lanjut) ')
# modul kuis pengurangan
def pengurangan(n):
    # kuis lepas
    if n == 1:
        while True:
            num1 = randint(1,10)
            num2 = randint(1,num1)
            print('\nPertanyaan: ',num1,' - ',num2,sep='')
            ans1 = str(input('Jawab: '))
            if ans1 == 'akhiri kuis':
                break
            elif ans1.isdigit():
                if eval(ans1) == num1-num2:
                    print("\nBenar!")
                else:
                    print("\nSalah! Jawabannya ",num1-num2,'.',sep='')
            else:
                print('\nInput Salah!')
    # kuis 5 nomor
    else:
        skor = 0
        for i in range (1,6):
            num1 = randint(1,10)
            num2 = randint(1,num1)
            print('\nPertanyaan ',i,': ',num1,' - ',num2,sep='')
            ans1 = str(input('Jawab: '))
            if ans1.isdigit():
                if eval(ans1) == num1-num2:
                    print("\nBenar!")
                    skor += 20
                else:
                    print("\nSalah! Jawabannya ",num1-num2,'.',sep='')
            else:
                print('\nInput salah!')
        print('\nSkor kamu:',skor)
        input('(tekan enter untuk lanjut) ')
# modul kuis campur (penjumlahan dan pengurangan)
def campur(n):
    # kuis lepas
    if n == 1:
        while True:
            operation = randint(1,2)
            if operation == 1:
                num1 = randint(1,10)
                num2 = randint(1,10)
                print('\nPertanyaan: ',num1,' + ',num2,sep='')
                ans1 = str(input('Jawab: '))
                if ans1 == 'akhiri kuis':
                    break
                elif ans1.isdigit():
                    if eval(ans1) == num1+num2:
                        print("\nBenar!")
                    else:
                        print("\nSalah! Jawabannya ",num1+num2,'.',sep='')
                else:
                    print('\nInput Salah!')
            else:
                num1 = randint(1,10)
                num2 = randint(1,num1)
                print('\nPertanyaan: ',num1,' - ',num2,sep='')
                ans1 = str(input('Jawab: '))
                if ans1 == 'akhiri kuis':
                    break
                elif ans1.isdigit():
                    if eval(ans1) == num1-num2:
                        print("\nBenar!")
                    else:
                        print("\nSalah! Jawabannya ",num1-num2,'.',sep='')
                else:
                    print('\nInput Salah!')
    # kuis 5 nomor
    else:
        skor = 0
        for i in range(1,6):
            operation = randint(1,2)
            if operation == 1:
                num1 = randint(1,10)
                num2 = randint(1,10)
                print('\nPertanyaan ',i,': ',num1,' + ',num2,sep='')
                ans1 = str(input('Jawab: '))
                if ans1.isdigit():
                    if eval(ans1) == num1+num2:
                        print("\nBenar!")
                        skor += 20
                    else:
                        print("\nSalah! Jawabannya ",num1+num2,'.',sep='')
                else:
                    print('\nInput salah!')
            else:
                num1 = randint(1,10)
                num2 = randint(1,num1)
                print('\nPertanyaan ',i,': ',num1,' - ',num2,sep='')
                ans1 = str(input('Jawab: '))
                if ans1.isdigit():
                    if eval(ans1) == num1-num2:
                        print("\nBenar!")
                        skor += 20
                    else:
                        print("\nSalah! Jawabannya ",num1-num2,'.',sep='')
                else:
                    print('\nInput salah!')
        print('\nSkor kamu:',skor)
# pesan yang keluar jika user mengakhiri program
def endGame():
    input('\nTerima kasih telah bermain kuis ini. Sampai jumpa lagi! ')
# menjalankan program
main()
