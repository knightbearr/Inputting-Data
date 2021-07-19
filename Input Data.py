banyak = int(input('Banyak data: '))

nilaiDenganNama = {}

for i in range(banyak):
  inputNama = input('Masukan nama: ')
  inputNilai = int(input('Masukan nilai: '))

  nilaiDenganNama[inputNilai] = nilaiDenganNama.get(inputNilai, []) + [inputNama]

nilaiSorted = sorted(list(nilaiDenganNama.keys()))

nilaiTerendah, nilaiTertinggi = nilaiSorted[0], nilaiSorted[-1]

print(f'Nilai tinggi diperoleh : {nilaiDenganNama[nilaiTertinggi]} nilai dengan nama tertinggi {nilaiTertinggi}')

print(f'Nilai terendah diperoleh : {nilaiDenganNama[nilaiTerendah]} nilai dengan nama tertinggi {nilaiTerendah}')

print(nilaiDenganNama)
