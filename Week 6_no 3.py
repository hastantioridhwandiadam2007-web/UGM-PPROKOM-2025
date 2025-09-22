set_A = {20,30,40,50,60}
set_B = {25,30,35,40,45}
set_C = {30,40,50,70,80}
set_D = {40,50,60,90,100}

irisan = set_A & set_C & set_D
print(irisan)
gabungan = (set_A | set_B) - set_D
print(gabungan)
selisih_simetris = set_B ^ set_C
print(selisih_simetris)
kombinasi = (set_A | set_B) - (set_C & set_D)
print(kombinasi)