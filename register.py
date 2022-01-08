from login import Registration

a = Registration()
fal = True

while fal:
    if a.new_login():
        password = a.new_password()
    else:
        print("Login faqat harflardan iborat bo`lsin!")
        continue
    password2 = a.confirm_password()
    if password.isalpha() and password2.isalpha():
        print("Parol faqat raqamlardan iborat bo`lsin!")
    elif password == password2:
        a.data_base()
        print("Done!")
        fal = False
    else:
        print("Parol tasdiqlanmadi!")


    
