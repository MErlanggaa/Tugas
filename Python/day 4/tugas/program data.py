import tkinter as tk

def simpan_data():
    nama = entry_nama.get()
    tanggal_lahir = entry_tanggal_lahir.get()
    asal_sekolah = entry_asal_sekolah.get()
    nisn = entry_nisn.get()
    nama_ayah = entry_nama_ayah.get()
    nama_ibu = entry_nama_ibu.get()
    nomor_telepon = entry_nomor_telepon.get()
    alamat = text_alamat.get("1.0", "end-1c")

    result = f'Nama: {nama}\nTanggal Lahir: {tanggal_lahir}\nAsal Sekolah: {asal_sekolah}\nNISN: {nisn}\nNama Ayah: {nama_ayah}\nNama Ibu: {nama_ibu}\nNomor Telepon: {nomor_telepon}\nAlamat: {alamat}'
    popup = tk.Toplevel(root)
    popup.title("Data Disimpan")
    popup.geometry("300x200")
    tk.Label(popup, text=result).pack()

root = tk.Tk()
root.title("Data siswa baru")
root.configure(bg="orange")

label_nama = tk.Label(root, text='Nama:', bg="orange")
label_tanggal_lahir = tk.Label(root, text='Tanggal lahir:', bg="orange")
label_asal_sekolah = tk.Label(root, text='Asal Sekolah:', bg="orange")
label_nisn = tk.Label(root, text='NISN:', bg="orange")
label_nama_ayah = tk.Label(root, text='Nama Ayah:', bg="orange")
label_nama_ibu = tk.Label(root, text='Nama Ibu:', bg="orange")
label_nomor_telepon = tk.Label(root, text='Nomor Telepon / HP:', bg="orange")
label_alamat = tk.Label(root, text='Alamat:', bg="orange")

label_nama.grid(row=0, column=0, sticky='w')
label_tanggal_lahir.grid(row=1, column=0, sticky='w')
label_asal_sekolah.grid(row=2, column=0, sticky='w')
label_nisn.grid(row=3, column=0, sticky='w')
label_nama_ayah.grid(row=4, column=0, sticky='w')
label_nama_ibu.grid(row=5, column=0, sticky='w')
label_nomor_telepon.grid(row=6, column=0, sticky='w')
label_alamat.grid(row=7, column=0, sticky='w')

entry_nama = tk.Entry(root)
entry_tanggal_lahir = tk.Entry(root)
entry_asal_sekolah = tk.Entry(root)
entry_nisn = tk.Entry(root)
entry_nama_ayah = tk.Entry(root)
entry_nama_ibu = tk.Entry(root)
entry_nomor_telepon = tk.Entry(root)

entry_nama.grid(row=0, column=1)
entry_tanggal_lahir.grid(row=1, column=1)
entry_asal_sekolah.grid(row=2, column=1)
entry_nisn.grid(row=3, column=1)
entry_nama_ayah.grid(row=4, column=1)
entry_nama_ibu.grid(row=5, column=1)
entry_nomor_telepon.grid(row=6, column=1)

text_alamat = tk.Text(root, height=5, width=30)
text_alamat.grid(row=7, column=1)

button_hapus = tk.Button(root, text="Hapus", fg="white", bg="red", command=root.destroy)
button_simpan = tk.Button(root, text="Simpan", fg="white", bg="red", command=simpan_data)

button_hapus.grid(row=8, column=0, padx=10, pady=10)
button_simpan.grid(row=8, column=1, padx=10, pady=10)

root.mainloop()
