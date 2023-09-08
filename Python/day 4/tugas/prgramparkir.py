import tkinter as tk
from datetime import datetime, timedelta

class ParkirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Parkir")
        
        # Inisialisasi data pelanggan
        self.pelanggan = []
        
        # Label untuk menampilkan informasi harga parkir
        self.harga_parkir_label = tk.Label(root, text="Biaya per Jam", font=("Arial", 16), foreground="red")
        self.harga_parkir_label.grid(row=2, column=4, columnspan=3, pady=10)
        
        self.harga_parkir_label = tk.Label(root, text="RP. 2.000", font=("Arial", 40), foreground="red")
        self.harga_parkir_label.grid(row=3, column=4, columnspan=3, pady=10)
        
        # Label dan Entry untuk input nomor plat polisi
        tk.Label(root, text="Nomor Plat Polisi:").grid(row=1, column=0, sticky="w")
        self.nomor_plat_entry = tk.Entry(root)
        self.nomor_plat_entry.grid(row=1, column=1, sticky="w")
        
        # Label dan Entry untuk input waktu masuk
        tk.Label(root, text="Waktu Masuk (HH:MM):").grid(row=2, column=0, sticky="w")
        self.waktu_masuk_entry = tk.Entry(root)
        self.waktu_masuk_entry.grid(row=2, column=1, sticky="w")
        
        # Label dan Entry untuk input waktu keluar
        tk.Label(root, text="Waktu Keluar (HH:MM):").grid(row=3, column=0, sticky="w")
        self.waktu_keluar_entry = tk.Entry(root)
        self.waktu_keluar_entry.grid(row=3, column=1, sticky="w")
        
        # Tombol untuk menghitung biaya
        tk.Button(root, text="Hitung Biaya", command=self.hitung_biaya).grid(row=5, column=0, columnspan=2)
        
        # Label untuk menampilkan biaya
        self.biaya_label = tk.Label(root, text="")
        self.biaya_label.grid(row=4, column=0, columnspan=2)
        
        # Label dan Entry untuk mencari nomor polisi
        tk.Label(root, text="Cari No Polisi:").grid(row=0, column=0, sticky="w")
        self.cari_nomor_plat_entry = tk.Entry(root)
        self.cari_nomor_plat_entry.grid(row=0, column=1, sticky="w")
        tk.Button(root, text="Cari", command=self.cari_nomor_polisi).grid(row=0, column=2)
        
        # Label dan Text untuk menampilkan daftar pelanggan terakhir keluar
        tk.Label(root, text="Daftar Pelanggan Terakhir Keluar:").grid(row=6, column=0, sticky="w")
        self.daftar_terakhir_text = tk.Text(root, height=10, width=40)
        self.daftar_terakhir_text.grid(row=7, column=0, columnspan=3)
        
        # Label dan Text untuk menampilkan daftar pelanggan banyak bayar
        tk.Label(root, text="Daftar Pelanggan Banyak Bayar:").grid(row=6, column=4, sticky="w")
        self.daftar_bayar_text = tk.Text(root, height=10, width=40)
        self.daftar_bayar_text.grid(row=7, column=4, columnspan=3)

        # Membuat variabel untuk pelanggan dengan biaya lebih dari 10 ribu
        self.pelanggan_bayar_tinggi = []

    def format_as_rupiah(self, angka):
        rupiah = "Rp. {:,.2f}".format(angka)
        return rupiah

    def format_waktu(self, waktu):
        return waktu.strftime("%d-%m-%Y %H:%M")

    def hitung_biaya(self):
        try:
            waktu_masuk_str = self.waktu_masuk_entry.get()
            waktu_keluar_str = self.waktu_keluar_entry.get()
            
            waktu_masuk = datetime.strptime(waktu_masuk_str, "%H:%M")
            waktu_keluar = datetime.strptime(waktu_keluar_str, "%H:%M")
            
            selisih_waktu = waktu_keluar - waktu_masuk
            selisih_jam = selisih_waktu.total_seconds() / 3600
            
            # Set biaya minimum 2 ribu jika waktu parkir kurang dari satu jam
            biaya = max(selisih_jam * 2000, 2000)
            
            # Tambahkan biaya tambahan 2 ribu jika waktu parkir lebih dari 1 jam
            if selisih_jam > 1:
                biaya += int((selisih_jam - 1) * 2000 + 2000)

            formatted_biaya = self.format_as_rupiah(biaya)
            self.biaya_label.config(text=f"Biaya: {formatted_biaya}")
            
            if biaya > 10000:
                nomor_plat = self.nomor_plat_entry.get()
                pelanggan_data = f"No Plat: {nomor_plat}, Masuk: {waktu_masuk_str}, Keluar: {waktu_keluar_str}, Biaya: {formatted_biaya}"
                self.pelanggan_bayar_tinggi.append(pelanggan_data)
                self.daftar_bayar_text.delete("1.0", "end")
                self.daftar_bayar_text.insert("1.0", "\n".join(self.pelanggan_bayar_tinggi))
            
            # Menampilkan daftar pelanggan terakhir keluar secara otomatis
            nomor_plat = self.nomor_plat_entry.get()
            pelanggan_data = f"No Plat: {nomor_plat}, Masuk: {waktu_masuk_str}, Keluar: {waktu_keluar_str}, Biaya: {formatted_biaya}"
            self.pelanggan.append(pelanggan_data)
            self.daftar_terakhir_text.delete("1.0", "end")
            self.daftar_terakhir_text.insert("1.0", "\n".join(reversed(self.pelanggan)))

        except ValueError:
            self.biaya_label.config(text="Format waktu salah")
    
    def cari_nomor_polisi(self):
        nomor_plat_cari = self.cari_nomor_plat_entry.get()
        hasil_pencarian = []
        for pelanggan_data in self.pelanggan:
            if nomor_plat_cari in pelanggan_data:
                hasil_pencarian.append(pelanggan_data)
        if hasil_pencarian:
            self.daftar_terakhir_text.delete("1.0", "end")
            self.daftar_terakhir_text.insert("1.0", "\n".join(hasil_pencarian))
        else:
            self.daftar_terakhir_text.delete("1.0", "end")
            self.daftar_terakhir_text.insert("1.0", "Nomor Plat tidak ditemukan.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ParkirApp(root)
    root.mainloop()
