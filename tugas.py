import numpy as np

# Buat matriks kosong 10x50
matrix = np.zeros((10, 50), dtype=int)

# Fungsi bantu untuk menggambar garis vertikal dan horizontal
def draw_letter_block(matrix, letter, col):
    if letter == 'T':
        matrix[0, col:col+5] = 1
        matrix[:, col+2] = 1
    elif letter == 'A':
        matrix[0, col+1:col+4] = 1
        matrix[1:, col] = 1
        matrix[1:, col+4] = 1
        matrix[4, col:col+5] = 1
    elif letter == 'M':
        matrix[:, col] = 1
        matrix[:, col+4] = 1
        for i in range(3):
            matrix[i, col+1+i] = 1
            matrix[i, col+3-i] = 1
    elif letter == 'S':
        matrix[0, col:col+5] = 1
        matrix[4, col:col+5] = 1
        matrix[9, col:col+5] = 1
        matrix[1:4, col] = 1
        matrix[5:9, col+4] = 1
    elif letter == 'I':
        matrix[0, col:col+5] = 1
        matrix[1:9, col+2] = 1
        matrix[9, col:col+5] = 1
    elif letter == 'L':
        matrix[:, col] = 1
        matrix[9, col:col+5] = 1

# Gambar huruf-huruf "TAMSIL" dengan spasi antar huruf
letters = ['T', 'A', 'M', 'S', 'I', 'L']
for i, letter in enumerate(letters):
    draw_letter_block(matrix, letter, i * 8)  # 5 kolom huruf + 3 kolom spasi

# Tampilkan hasil matriks
for row in matrix:
    print(" ".join(str(x) for x in row))
