import tkinter as tk
from tkinter import filedialog, messagebox


class KasirMakanan:
    def __init__(self, master):
        self.master = master
        master.title("Kasir Makanan")

        # Membuat frame untuk inputan jumlah menu makanan yang dipesan
        self.input_frame = tk.LabelFrame(master, text="Input Jumlah Menu Makanan")
        self.input_frame.pack(pady=20)

        # Membuat entry dan label untuk setiap menu makanan
        self.menu_items = {
            "Nasi Goreng": 15000,
            "Mie Goreng": 12000,
            "Ayam Goreng": 18000,
            "Sate Ayam": 20000,
            "Sop Ayam": 16000,
            "Nasi Uduk": 14000,
            "Mie Rebus": 13000
        }

        self.menu_entries = {}
        for i, (name, price) in enumerate(self.menu_items.items()):
            label = tk.Label(self.input_frame, text=f"Menu {i+1}: {name} (Rp {price})")
            label.grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(self.input_frame, width=10)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.menu_entries[name] = entry

        # Membuat tombol untuk menghitung total pembayaran
        self.total_button = tk.Button(master, text="Hitung Total Pembayaran", command=self.hitung_total)
        self.total_button.pack(pady=10)

        # Membuat frame untuk menampilkan total pembayaran dan tombol cetak bon
        self.total_frame = tk.LabelFrame(master, text="Total Pembayaran")
        self.total_frame.pack(pady=20)

        self.total_label = tk.Label(self.total_frame, text="Total Pembayaran:")
        self.total_label.pack(padx=5, pady=5)

        self.total_value = tk.Label(self.total_frame, text="Rp 0")
        self.total_value.pack(padx=5, pady=5)

        self.cetak_bon_button = tk.Button(self.total_frame, text="Cetak Bon", command=self.cetak_bon)
        self.cetak_bon_button.pack(padx=5, pady=5)


    def hitung_total(self):
        # Menghitung total pembayaran berdasarkan jumlah menu makanan yang dipesan
        total_harga = 0

        for name, entry in self.menu_entries.items():
            if entry.get():
                total_harga += int(entry.get()) * self.menu_items[name]

        self.total_value.config(text=f"Rp {total_harga}")

    def cetak_bon(self):

        bon = "===== Bon Pembayaran =====\n\n"
        bon += "Menu Pembelian:\n"
        for name, entry in self.menu_entries.items():
            if entry.get():
                bon += "\nTotal Pembayaran:  " + str(entry.get()) + " " + name + " x RP " + str(self.menu_items[name]) + " = Rp " + str(
                    int(entry.get()) * self.menu_items[name]) + "\n"
        bon += "\nTotal Pembayaran:  " + self.total_value.cget("text")
        # Menyimpan bon pembayaran dalam file txt
        filename = filedialog.asksaveasfilename(defaultextension=".txt")
        with open(filename, "w") as f:
            f.write(bon)
        messagebox.showinfo("Info", "Bon pembayaran berhasil disimpan!")


root = tk.Tk()
my_gui = KasirMakanan(root)
root.mainloop()