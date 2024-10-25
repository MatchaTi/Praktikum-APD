def inputString(prompt):
    while True:
        try:
            userInput = input(prompt).strip()
            if not userInput:
                raise ValueError("Input tidak boleh kosong")
            return userInput
        except ValueError as e:
            print(e)

def inputInteger(prompt):
    while True:
        try:
            data = input(prompt).strip()
            if not data.isnumeric():
                raise ValueError("Input tidak boleh kosong atau berupa huruf")
            return int(data)        
        except ValueError as e:
            print(e)


def inputFloat(prompt):
    while True:
        try:
            data = input(prompt).strip()
            if not data or data.isalpha():
                raise ValueError("Input tidak boleh kosong atau berupa huruf")
            return float(data)        
        except ValueError:
            print("Input harus berupa angka desimal yang valid")


# data = inputString("Masukkan nama mahasiswa: ")
# print(f"Nama mahasiswa: {data}")

# data = inputInteger("Masukkan angka: ")
# print(f"Angka yang dimasukkan: {data}")

# data = inputFloat("Masukkan angka: ")
# print(f"Angka yang dimasukkan: {data}")

# try:
#     angka  = int(input("Masukkan angka : "))
#     if not angka.isnumeric():
#         raise ValueError("angka tida boleh kosong ")
# except ValueError as e:
#     print(e)
# else:
#     print('Input berhasil')
# finally:
#     print('Program selesai')

# def get_non_empty_integer():
#     while True:
#         try:
#             user_input = input("Masukkan angka integer: ").strip()  # Menghapus spasi di awal/akhir
#             if not user_input.isnumeric():  # Cek jika input kosong
#                 raise ValueError("Input tidak boleh kosong!")
#             number = float(user_input)  # Coba ubah input menjadi integer
#             return number
#         except ValueError as e:
#             print(e)

# angka = get_non_empty_integer()
# print(f"Angka integer yang dimasukkan: {angka}")






