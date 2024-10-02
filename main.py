#
from FumoEncryptAndDecrypt import fumo_encryption
from FumoEncryptAndDecrypt import fumo_decryption
# from FumoEncryptAndDecrypt import fumo_validation
import pandas.io.clipboard as cb

if  __name__ == "__main__":
    print("This is a fumo language translator running in console environment.")
    quitSign = ''
    while True:
        print("*" * 80)
        print("What do you want to do for now")
        print("[1]/[e] : Translate normal sentences into fumo language.")
        print("[2]/[d] : Translate fumo language into normal sentences.")
        # print("[3]/[v] : Validate whether fumo is running normally.")
        print("[q]/[Q] : Quit this fumo translator and dance with fumo.")
        quitSign = input("Your choice:_\b")

        if quitSign == "q" or quitSign == "Q":
            break
        elif quitSign == "1" or quitSign == "e":
            print("*" * 80)
            encrypt_string = input("Type your normal sentence below\n(Or you want to double-fumolize your sentence type your fumo-ed sentence below)\n")
            encrypted_string = fumo_encryption(encrypt_string)
            cb.copy(encrypted_string)
            print("*" * 80)
            print("Your result has been copied to the clipboard!")
            print("Here is your result:", encrypted_string)
            ConfirmChecker = input("(Press [Enter] to return to the main menu)")
        elif quitSign == "2" or quitSign == "d":
            print("*" * 80)
            decrypt_string = input("Type your fumo-ed sentence below\n")
            decrypted_string = fumo_decryption(decrypt_string)
            cb.copy(decrypted_string)
            print("*" * 80)
            print("Your result has been copied to the clipboard!")
            print("Here is your result", decrypted_string)
            ConfirmChecker = input("(Press [Enter] to return to the main menu)")
        # elif quitSign == "3" or quitSign == "v":
        #     fumo_validation()
        #     ConfirmChecker = input("(Press [Enter] to return to the main menu)")
        else:
            print("Not a choice fumo translator expected!")
            ConfirmChecker = input("(Press [Enter] to return to the main menu)")
    
    print("Thanks for using this!")

