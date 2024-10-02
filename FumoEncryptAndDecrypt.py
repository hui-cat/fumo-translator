#fumo语加密解密
#由于python中已经有了字典的实现且键对键读取时间复杂度与哈希表接近
#在考量以后选择使用字典以空间换时间以加快fumo语的加密速度

#2024.10.2注：可能由于fumo_encrypt_table内存在键值或数值重复或base64的编码问题，目前fumo语存在解密和加密的内容不一致的现象
#目前已尝试出"asdf"加密后变为"asgf"的问题（而且是概率性出现,在输入"asdfasdf"进行加密解密后结果为"asgfasdf"）
#因此在后续的完善中可能把base64编码更换为其他编码

import base64

fumo_encrypt_table = { # ascii字符对应fumo语格式为fumo + 特殊字符
    #Numbers
    '0' : 'fumo-',
    '1' : 'Fumo-',
    '2' : 'fUmo-',
    '3' : 'fuMo-',
    '4' : 'fumO-',
    '5' : 'FUmo-',
    '6' : 'FuMo-',
    '7' : 'FumO-',
    '8' : 'fUMo-',
    '9' : 'fUmO-',
    #Lowercase letter
    'a' : 'fuMO-',
    'b' : 'FUMo-',
    'c' : 'FUmO-',
    'd' : 'FuMO-',
    'e' : 'FUMO-', #这里有个顶针编码的时候精神涣散漏了一个"fUMO-"
    'f' : 'fumo.',
    'g' : 'Fumo.',
    'h' : 'fUmo.',
    'i' : 'fuMo.',
    'j' : 'fumO.',
    'k' : 'FUmo.',
    'l' : 'FuMo.',
    'm' : 'fumO.',
    'n' : 'FUmo.',
    'o' : 'FuMo.',
    'p' : 'FumO.',
    'q' : 'fUMo.',
    'r' : 'fUmO.',
    's' : 'fuMO.',
    't' : 'FUMo.',
    'u' : 'FUmO.',
    'v' : 'fUMO.',
    'w' : 'FUMO.',
    'x' : 'fumo,',
    'y' : 'Fumo,',
    'z' : 'fUmo,',
    #UpperCase letter
    'A' : 'fumo+',
    'B' : 'Fumo+',
    'C' : 'fUmo+',
    'D' : 'fuMo+',
    'E' : 'fumO+',
    'F' : 'FUmo+',
    'G' : 'FuMo+',
    'H' : 'FumO+',
    'I' : 'fUMo+',
    'J' : 'fUmO+',
    'K' : 'fuMO+',
    'L' : 'FUMO+',
    'M' : 'fumo|',
    'N' : 'Fumo|',
    'O' : 'fUmo|',
    'P' : 'fuMo|',
    'Q' : 'fumO|',
    'R' : 'FUmo|',
    'S' : 'FuMo|',
    'T' : 'FumO|',
    'U' : 'fUMo|',
    'V' : 'fUmO|',
    'W' : 'fuMO|',
    'X' : 'FUMo|',
    'Y' : 'FUmO|',
    'Z' : 'fUMO|',
    #Symbols
    '`' : 'fuMo,',
    '~' : 'fumO,',
    '!' : 'FUmo,',
    '@' : 'FuMo,',
    '#' : 'FumO,',
    '$' : 'fUMo,',
    '%' : 'fUmO,',
    '^' : 'fuMO,',
    '&' : 'FUMo,',
    '*' : 'FuMO,',
    '(' : 'FuMO,',
    ')' : 'fUMO,',
    '-' : 'FUMO,',
    '_' : 'fUMo,',
    '=' : 'Fumo;',
    '+' : 'fUmo;',
    '[' : 'fuMo;',
    ']' : 'fumO;',
    '{' : 'FUmo;',
    '}' : 'FuMo;',
    '\\' : 'FumO;',
    '|' : 'fUMo;',
    ';' : 'fUmO;',
    ':' : 'fuMO;',
    '"' : 'FUMo;',
    "'" : 'FuMO;',
    ',' : 'fUMO;',
    '<' : 'FUMO;',
    '.' : 'fumo/',
    '/' : 'Fumo/',
    '?' : 'fUmo/',
    #不知道在UTF-8加上base64编码后生成字符串会不会出现转义符号，故暂时不对此进行编码
    #改天做个字符编码生成器算了......
    '\0' : 'fuMo/'
}

#转换解码字典
fumo_decrypt_table = dict(zip(fumo_encrypt_table.values(), fumo_encrypt_table.keys()))

#Fumo加密解密的主程序
#单独开了一个文件为后面web移植做准备
def fumo_encryption(encrypt_string):

    if not isinstance(encrypt_string, str):
        return "FUMO requires a string to translate, not a dance to wave!"
    
    temp_strencode = encrypt_string.encode("UTF-8")
    base64Encrypt = base64.b64encode(temp_strencode)
    str_base64 = base64Encrypt.decode('UTF-8')

    result="" 
    for i in str_base64:
        result += fumo_encrypt_table[i]

    return result


def fumo_decryption(decrypt_string):

    if not isinstance(decrypt_string, str):
        return "FUMO requires a string to translate, not a dance to wave!"
    
    str_base64 = ''
    for i in range(0,len(decrypt_string),5):
        decrypt_key = decrypt_string[i:i+5]
        str_base64 += fumo_decrypt_table[decrypt_key]

    temp_strencode = str_base64.encode("UTF-8")
    base64Decrypt = base64.b64decode(temp_strencode)
    result = base64Decrypt.decode("UTF-8")
    return result
    

#不知为何原因，验证方法无法通过编译，故暂时将其注释
#其功能为检查fumo_decrypt_table与fumo_encrypt_table中是否存在重复字符
# def fumo_validation():
#     encrypt_value_list = list(fumo_encrypt_table.values())
#     encrypt_key_list = list(fumo_encrypt_table.keys())
#     decrypt_value_list = list(fumo_decrypt_table.values())
#     decrypt_key_list = list(fumo_encrypt_table.keys())

#     encrypt_key_errors = []
#     encrypt_value_errors = []
#     decrypt_key_errors = []
#     decrypt_value_errors = []

#     for i in encrypt_key_list:
#         print("Checking encryption key:",i)
#         if encrypt_key_list.count(i) > 1:
#             print("encrypt key error:" + i)
#             encrypt_key_errorscrypt_key_errors.append(i)

#     for i in encrypt_value_list:
#         print("Checking encryption value:",i)
#         if encrypt_value_list.count(i) > 1:
#             print("encrypt value error:" + i)
#             encrypt_value_errors.append(i)

#     for i in decrypt_key_list:
#         print("Checking encryption key:",i)
#         if decrypt_key_list.count(i) > 1:
#             print("decrypt key error:" + i)
#             decrypt_key_errors.append(i)

#     for i in decrypt_value_list:
#         print("Checking encryption value:",i)
#         if decrypt_value_list.count(i) > 1:
#             print("decrypt value error:" + i)
#             decrypt_value_errors.append(i)

#     print("*" * 80)
#     print("Result:")
#     print("Encryption: ", len(encrypt_key_errors) , " key errors, " , len(encrypt_value_errors) , " value errors.")
#     print("Error keys: ", encrypt_key_errors , " Error Values: " , encrypt_value_errors)
#     print("Decryption: ", len(decrypt_key_errors) , " key errors, " , len(decrypt_value_errors) , " value errors.")
#     print("Error keys: ", decrypt_key_errors , " Error Values: " , decrypt_value_errors)
