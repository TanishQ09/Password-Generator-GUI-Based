import random

def rand_pass_all(name, contact,age, date, month, year):
    s1 = str(contact)
    s2 = str(age)
    s3 = str(date)
    s4 = str(month)
    s5 = str(year)
    s = []
    s.extend(name)
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    s.extend(s5)
    random.shuffle(s)
    plen = random.randint(8,16)
    pass_code = ("".join(s[0:plen]))
    return pass_code

def rand_name_symbol(name,num):
    s1 = ["@","#","$","%","&","<",">"]
    mid = len(name)//2
    pass_code = (name[0:mid]+random.choice(s1)+name[mid:]+random.choice(s1)+str(num)+random.choice(s1))
    return pass_code

def name_mid_num(name, num):
    name_len = len(name)
    mid = int(name_len/2)
    pass_code = (name[:mid]+str(num)+name[mid:])
    return pass_code

def name_end_num(name, num):
    pass_code = (name+str(num))
    return pass_code

def name_begin_num(name, num):
    pass_code = (str(num)+name)
    return pass_code

def Ldig_name_Fdig(name, num):
    second = int(num%10)
    num/=10
    first = int(num%10)
    pass_code = (str(second)+name+str(first))

def Fdig_name_Ldig(name, num, num2):
    second = int(num%10)
    num/=10
    first = int(num%10)
    sec = int(num2%10)
    num2/=10
    fir = int(num2%10)
    pass_code = (str(first)+name+str(second))
    return pass_code

