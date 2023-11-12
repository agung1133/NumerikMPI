from mpi4py import MPI
import numpy as np
import time

# Inisialisasi MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Panjang array
array_length = 100

# Bagi pekerjaan sesuai jumlah proses
local_array_length = array_length // size
local_array = np.random.rand(local_array_length)

# Memulai pengukuran waktu
start_time = time.time()

# Menjumlahkan elemen-elemen lokal
local_sum = np.sum(local_array)

# Menggunakan operasi reduksi untuk menghitung jumlah global
global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

# Menghentikan pengukuran waktu
end_time = time.time()

# Proses 0 mencetak hasil dan waktu eksekusi
if rank == 0:
    print("Hasil penjumlahan global:", global_sum)
    print("Waktu eksekusi: {:.4f} detik".format(end_time - start_time))