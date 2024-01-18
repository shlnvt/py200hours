weight = float(input('Masukkan berat badan (dalam kg):'))
height = float(input('Masukkan tinggi badan (dalam satuan cm):'))
liters_need = -2.097 + (0.1069 * height) + (0.2466 * weight)

print(f"Kebutuhan harian air minum jika berat badan {weight} dan tinggi {height} yaitu sebesar {liters_need} liter")