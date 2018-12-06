#CREATED BY JUAN VALERIAN DELIMA
def cek_simbol(string):
   check = False
   for s in string:
      if s in "~!@#$%^&*()_+{}|':;<>?":
         check = True
   return check

def cek_later(string):
   check = False
   for s in string:
      if s in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ":
         check = True
   return check

def cek_number(string):
   check = False
   for s in string:
      if s in "0123456789":
         check = True
   return check

def main_program():
   repeat = True
   while repeat:
      password = input("Masukkan Password : ")
      if len(password) < 6:
         print("Password tidak boleh kurang dari 6 karakter")
         repeat =True
      else:
         if (cek_later(password) or cek_simbol(password)) and cek_number(password):
            print("Password Valid")
            coba = input("Ingin Coba Lagi ? (Y/N) : ")
            if coba == 'Y' or coba == 'y':
               repeat = True
            elif coba == 'N' or coba == 'n':
               repeat = False
         else:
            print("Password Tidak Valid")
            repeat =True

main_program()
