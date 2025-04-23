import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class CatatanHarianApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Catatan Harian")
        self.notes = {}  # {judul: (isi, timestamp)}

        # —————— MENU ——————
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Keluar", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tentang", command=self.show_about)
        menubar.add_cascade(label="Bantuan", menu=helpmenu)

        root.config(menu=menubar)

        # —————— WIDGETS ——————
        # Judul
        tk.Label(root, text="Judul:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_judul = tk.Entry(root)
        self.entry_judul.grid(row=0, column=1, columnspan=3, sticky="we", padx=5)

        # Tombol
        btn_add = tk.Button(root, text="Tambah Catatan", command=self.tambah_catatan)
        btn_add.grid(row=0, column=4, padx=5)
        btn_delete = tk.Button(root, text="Hapus Catatan", command=self.hapus_catatan)
        btn_delete.grid(row=0, column=5, padx=5)

        # Listbox + Scrollbar
        frame_list = tk.Frame(root)
        frame_list.grid(row=1, column=0, columnspan=2, rowspan=4, sticky="nswe", padx=5, pady=5)
        self.scrollbar = tk.Scrollbar(frame_list, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(frame_list, yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", self.tampilkan_catatan)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text (isi)
        tk.Label(root, text="Isi Catatan:").grid(row=1, column=2, columnspan=4, sticky="w", padx=5)
        self.text_isi = tk.Text(root, wrap=tk.WORD, state="normal")
        self.text_isi.grid(row=2, column=2, columnspan=4, rowspan=3, sticky="nswe", padx=5, pady=5)

        # Konfigurasi grid agar responsif
        for i in range(6):
            root.columnconfigure(i, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def show_about(self):
        messagebox.showinfo("Tentang", "Catatan Harian v1.0\noleh [Andryano Shevchenko Limbong]")

    def tambah_catatan(self):
        judul = self.entry_judul.get().strip()
        isi = self.text_isi.get("1.0", tk.END).strip()
        if not judul or not isi:
            messagebox.showerror("Error", "Judul dan isi catatan tidak boleh kosong.")
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        display_judul = f"{timestamp} — {judul}"
        # Simpan dalam dict
        self.notes[display_judul] = isi
        # Tambah ke Listbox
        self.listbox.insert(tk.END, display_judul)
        # Reset input
        self.entry_judul.delete(0, tk.END)
        self.text_isi.delete("1.0", tk.END)

    def tampilkan_catatan(self, event):
        sel = self.listbox.curselection()
        if not sel:
            return
        key = self.listbox.get(sel[0])
        isi = self.notes.get(key, "")
        # Tampilkan isi (read-only)
        self.text_isi.config(state="normal")
        self.text_isi.delete("1.0", tk.END)
        self.text_isi.insert(tk.END, isi)
        self.text_isi.config(state="disabled")

    def hapus_catatan(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showerror("Error", "Pilih catatan yang akan dihapus.")
            return
        key = self.listbox.get(sel[0])
        if messagebox.askyesno("Konfirmasi", f"Hapus catatan:\n{key}?"):
            # Hapus dari data dan UI
            del self.notes[key]
            self.listbox.delete(sel[0])
            # Bersihkan area teks
            self.text_isi.config(state="normal")
            self.text_isi.delete("1.0", tk.END)
            self.text_isi.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = CatatanHarianApp(root)
    root.mainloop()
