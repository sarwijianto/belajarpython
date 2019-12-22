import pandas as wiji


class Informasi(object):
    inf = wiji.read_csv('kelas_2b/jadwal.csv')
    print("Info Keberangkatan Kapal:")
    print(inf)
