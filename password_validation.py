#CREATED BY JUAN VALERIAN DELIMA
#the algorithm is made by juan

def create_lists(kata):
   new_arr = []
   for kata1 in kata:
      for huruf in kata1:
         new_arr.append(huruf)
   return new_arr

def sorting_kata(password): 
   arr = create_lists(password)
   for index in range(1, len(password)):
      current_word = arr[index]
      index_kata = index
      while index_kata > 0 and arr[index_kata - 1] > current_word:
         arr[index_kata] = arr[index_kata - 1]
         index_kata -= 1
      arr[index_kata] = current_word
   return arr
      
def pencarian_huruf(password, cari): #teknik rekursif
   arr = sorting_kata(password)
   if len(arr) == 0:
      return False
   else:
      split_word = len(arr) // 2
      if arr[split_word ] == cari:
         return True
      else:
         if cari < arr[split_word]:
            return pencarian_huruf(arr[:split_word], cari)
         else:
            return pencarian_huruf(arr[split_word + 1:], cari)

def cek_simbol(password):
   sym = "~!@#$%^&*()_{}'|:;"
   lists_sym = create_lists(sym)
   check = False
   for simbol in range(len(lists_sym)):
      if pencarian_huruf(password, lists_sym[simbol]) != check:
         check = True
   return check

def cek_kata(password):
   words = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
   lists_wrd = create_lists(words)
   check = False
   for word in range(len(lists_wrd)):
      if pencarian_huruf(password, lists_wrd[word]) != check:
         check = True
   return check
         

def cek_angka(password):
   numbers = "0123456789"
   list_num = create_lists(numbers)
   check = False
   for angka in range(len(list_num)):
      if pencarian_huruf(password, list_num[angka]) != check:
         check = True
   return check

def program_utama():
   ulang = False
   while not ulang:
      password = input("Masukkan Password : ")
      if len(password) < 6:
         print("Panjang password harus lebih dari 6!")
         ulang = False
      else:
         if (cek_kata(password) or cek_simbol(password)) and cek_angka(password):
            print("Password Valid!")
            coba = input("Ulangi Program ? Y/N : ")
            if coba == 'Y' or coba == 'y':
               continue
            else:
               if coba == 'N' or coba == 'n':
                  ulang = True
         else:
            print("Password Tidak Valid!")


program_utama()

               
