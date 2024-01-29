"""
Aplikasi pendeteksi gempa
"""

def extraksi_data():
    """
Tanggal         : 29 Januari 2024,
Waktu           : 00:22:32 WIB
Magnitudo       : 5.3
Kedalaman       : 121 km
Lokasi          : 4.14 LS - 142.59 BT
Pusat Gempa     :129 km BaratDaya WEWAK-PNG
Potensi         :tidak berpotensi TSUNAMI
    :return:
    """
    hasil = dict()
    hasil['Tanggal'] = '29 Januari 2024'
    hasil['Waktu'] = '00:22:32 WIB'
    hasil['Magnitudo'] = 5.3
    hasil['Kedalaman'] = '121 KM'
    hasil['Lokasi'] = {'ls': 4.14, 'bt':142.59}
    hasil['Pusat_Gempa'] = '129 km BaratDaya WEWAK-PNG'
    hasil['Potensi'] = 'tidak berpotensi TSUNAMI'


    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal :{result['Tanggal']}")
    print(f"Waktu :{result['Waktu']}")
    print(f"Magnitudo :{result['Magnitudo']}")
    print(f"Kedalaman :{result['Kedalaman']}")
    print(f"Lokasi LS :{result['Lokasi']['ls']}, BT :{result['Lokasi']['bt']} ")
    print(f"Pusat_Gempa :{result['Pusat_Gempa']}")
    print(f"Potensi :{result['Potensi']}")



if __name__ == '__main__':
    print("aplikasi utama")
    result = extraksi_data()
    tampilkan_data(result)