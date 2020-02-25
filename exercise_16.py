# Password Generator
# weak (1-3) medium (4-6) strong ()

import random

passw = ['write', 'a', 'password', 'generator', 'python', 'creative', 'mix']
num = list(str(range(0, 10)))
symbols = ['!', '@', '#', '$', '%', '&', '*']

pass_gen = passw + symbols + num

i = 0
strength = input('How strong you want your password: ')
if strength == 'weak':
    i = random.randint(1, 3)
elif strength == 'medium':
    i = random.randint(4, 6)
elif strength == 'strong':
    i = random.randint(7, 9)
gen_pass = random.sample(pass_gen, i)

print(''.join(gen_pass))
