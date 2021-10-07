import random
import array
 
# maximum length of password needed
# this can be changed to suit your password length
MAX_LEN = 12
 
# declare arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
UPLPCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                      'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                      'z''A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                      'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                      'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                      'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
 
# combines all the character arrays above to form one array
COMBINED_LIST = DIGITS + UPLPCASE_CHARACTERS + SYMBOLS
print(COMBINED_LIST)
 
# randomly select REQUIRED LENGTH from each character set above
rand_digit1 = ''.join(random.choice(DIGITS) for i in range (2))
rand_digit2= ''.join(random.choice(DIGITS) for i in range (2))
rand_upperlower1 = ''.join(random.choice(UPLPCASE_CHARACTERS) for i in range(2))
rand_upperlower2 = ''.join(random.choice(UPLPCASE_CHARACTERS) for i in range(2))
rand_upperlower3 = ''.join(random.choice(UPLPCASE_CHARACTERS) for i in range(2))
rand_symbol1 = ''.join(random.choice(SYMBOLS) for i in range(1))
rand_symbol2 = ''.join(random.choice(SYMBOLS) for i in range(1))
 
# combine the character randomly selected above

temp_pass_list = list(rand_symbol1 + rand_upperlower1 + rand_digit1 + rand_upperlower2 + rand_digit2 + rand_upperlower3 + rand_symbol2 ) 
random.choice(temp_pass_list)
print(temp_pass_list)
 
# traverse the temporary password array and append the chars
# to form the password
password = ""
for x in temp_pass_list:
        password = password + x
         
# print out password
        print(password)

