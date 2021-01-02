import sqlite3
import pathlib
import getpass

class DataManager:
    def __init__(self):
        database = str(pathlib.Path().absolute())+"/projek.db"
        self.connector = sqlite3.connect(database)
        self.cursor = self.connector.cursor()
        
    def executeQuery(self, query, retVal=False):
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.connector.commit()
        if retVal:
            return all_results

class User(DataManager):
    def __init__(self):
        DataManager.__init__(self)
        self.id_user = None
        self.email = None
        self.password = None
        self.username = None
        self.alamat = None
        self.luas = None
        self.bangun = None
        
    def login(self, email, password):
        query = 'SELECT id_user, email, password, username, alamat FROM user_data \
            where email=\'%s\' and password=\'%s\' '
        query = query % (email, password)
        data_login = self.executeQuery(query, True)
        konfirm_login = False
        for i in range(0,len(data_login)):
            if email == data_login[i][1] and password == data_login[i][2]:
                konfirm_login = True
                self.id_user = data_login[i][0]
                self.email = data_login[i][1]
                self.password = data_login[i][2]
                self.username = data_login[i][3]
                self.alamat = data_login[i][4]
                print("Login berhasil")
                print(f"Selamat datang {self.username} di KONVERSI SERBA GUNA")
        if konfirm_login == False:
            print(f"Data Login email {email}, password {password} tidak ditemukan, harap untuk melakukan register")

    def register(self, email, password, username, alamat):
        query = 'INSERT INTO user_data (email, password, username, alamat) \
                VALUES (\'%s\', \'%s\', \'%s\', \'%s\')'
        query = query % (email, password, username, alamat)
        self.executeQuery(query)
        query = 'SELECT id_user, email, password, alamat FROM user_data \
            where email=\'%s\' and password=\'%s\' '
        query = query % (email, password)
        data_login = self.executeQuery(query, True)
        for i in range(0,len(data_login)):
            if email == data_login[i][1] and password == data_login[i][2]:
                self.id_user = data_login[i][0]
        self.email = email
        self.password = password
        self.username = username
        self.alamat = alamat
        print(f"Akun berhasil dibuat. Selamat datang {self.username} di KONVERSI SERBA GUNA")

    def akun(self):
        print(f"email: {self.email}\npassword: {self.password}\nusername: {self.username}\nalamat: {self.alamat}")

class BangunDatar:
    luas = 0
    def __init__(self, jenis):
        self.jenis = jenis

class BangunRuang:
    luas = 0
    volume = 0
    def __init__(self, jenis):
        self.jenis = jenis

#jenis-jenis bangun datar
class Persegi(BangunDatar):
    sisi = 0
    def hitungLuas(self):
        self.sisi = float(input("Masukkan panjang sisi : "))
        self.luas = self.sisi**2

class Lingkaran(BangunDatar):
    jari2 = 0
    def hitungLuas(self):
        self.jari2 = float(input("Masukkan jari-jari lingkaran : "))
        self.luas = 3.14 * self.jari2**2

class Persegi_panjang(BangunDatar):
    panjang = 0
    lebar = 0
    def hitungLuas(self):
        self.panjang = float(input("Masukkan panjang persegi panjang : "))
        self.lebar = float(input("Masukkan lebar persegi panjang : "))
        self.luas = self.panjang * self.lebar

class Segitiga(BangunDatar):
    alas = 0
    tinggi = 0
    def hitungLuas(self):
        self.alas = float(input("Masukkan panjang alas segitiga : "))
        self.tinggi = float(input("Masukkan tinggi segitiga : "))
        self.luas = self.alas * self.tinggi / 2

#jenis-jenis bangun ruang
class Tabung(BangunRuang):
    jari2 = 0
    tinggi = 0
    def hitungLuas(self):
        self.jari2 = float(input("Masukkan jari-jari alas tabung : "))
        self.tinggi = float(input("Masukkan tinggi tabung : "))
        self.luas = 3.14 * self.jari2**2

    def hitungVolume(self):
        self.volume = self.luas * self.tinggi

class Balok(BangunRuang):
    panjang = 0
    lebar = 0
    tinggi = 0
    def hitungLuas(self):
        self.panjang = float(input("Masukkan panjang balok : "))
        self.lebar = float(input("Masukkan lebar balok : "))
        self.tinggi = float(input("Masukkan tinggi balok : "))
        self.luas = self.panjang * self.lebar
    def hitungVolume(self):
        self.volume = self.luas * self.tinggi

class Bola(BangunRuang):
    jari2 = 0
    def hitungLuas(self):
        self.jari2 = float(input("Masukkan jari-jari bola : "))
        self.luas = 4 * 3.14 * self.jari2**2
    def hitungVolume(self):
        self.volume = 4 * 3.14 * self.jari2**3 / 3

class Kubus(BangunRuang):
    rusuk = 0
    def hitungLuas(self):
        self.rusuk = float(input("Masukkan panjang rusuk kubus : "))
        self.luas = 6 * self.rusuk**2
    def hitungVolume(self):
        self.volume = self.rusuk**3


u = User()
print("Selamat datang di KONVERSI SERBA GUNA")
print("(Masukkan menu dengan menginputkan angka)")

while True:
    print("=== MENU ===\n1. Login\n2. Register\n3. Konversi\n4. Akun\n5. Exit")
    menu = input("Menu >").lower()
    
    if menu == '1':
        print("===== Login =====")
        email = input("Masukkan email:")
        password = getpass.getpass ("Masukkan password:")
        u.login(email,password)
        
    elif menu == '2':
        print("===== Register =====")
        email = input("Masukkan email:")
        password = input("Masukkan password:")
        username = input("Masukkan username:")
        Alamat = input("Masukkan Alamat:")
        u.register(email, password, username, Alamat)
        
    elif menu == '3':
        print("===== Konversi =====")
        if u.username != None:
            print("1. Persegi\n2. Lingkaran\n3. Persegi Panjang\n4. Segitiga\n5. Tabung\n6. Balok\n7. Bola\n8. Kubus  ")
            bangunan = input("Masukkan sebuah bangun datar atau bangun ruang : ").lower()
            if bangunan == "persegi":
                bangun = Persegi(bangunan)
            elif bangunan == "lingkaran":
                bangun = Lingkaran(bangunan)
            elif bangunan == "persegi panjang":
                bangun = Persegi_panjang(bangunan)
            elif bangunan == "segitiga":
                bangun = Segitiga(bangunan)
            elif bangunan == "tabung":
                bangun = Tabung(bangunan)
            elif bangunan == "balok":
                bangun = Balok(bangunan)
            elif bangunan == "bola":
                bangun = Bola(bangunan)
            elif bangunan == "kubus":
                bangun = Kubus(bangunan)
            else :
                print(bangunan + " bukanlah bangun datar maupun bangun ruang...")
        
            if isinstance(bangun, BangunDatar):
                bangun.hitungLuas()
                print("Luas {} adalah {}".format(bangun.jenis, bangun.luas))        
            else:
                bangun.hitungLuas()
                print("Luas permukaan {} adalah {}".format(bangun.jenis, bangun.luas))
                bangun.hitungVolume()
                print("Volume {} adalah {}".format(bangun.jenis, bangun.volume))
        else:
            print("Diperlukan Login terlebih dahulu")
               
    elif menu == '4':
        print("===== Akun =====")
        u.akun()
        
    elif menu == '5':
        print("===== Selamat Tinggal =====")
        print("Terima kasih telah mengunjungi KONVERSI SERBA GUNA")
        break
        
    elif menu == 'menu':
        print("(Masukkan menu dengan menginputkan angka)")
        print("1. Login\n2. Register\n3. Konversi\n4. Akun\n5. Exit")
        
    else:
        print("ketik menu untuk melihat daftar menu")