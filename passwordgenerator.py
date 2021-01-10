#password generator :)))))))
import random
random_list = """ 
	soap
	hallowed
	maniacal
	aloof
	squeak
	sudden
	certain
	quarrelsome
	wide
	club
	beg
	hesitant
	shy
	functional
	boundless
	crash
	wholesale
	cuddly
	ignore
	sofa
	signal
	happen
	book
	repeat
	bite
	slave
	intelligent
	ready
	adorable
	giddy
	herb
    carry
    future
    soak
    mold
    lunch
    ride
    coup
    formal
    wealth
    reconcile
    earthquake
    grief
    soul
    acid
    prey
    arm
    unfair
    offender
    scrape
    motorcycle
    glue
    encourage
    orbit
    compartment
    bind
    senior
    term
    taxi
    car
    threaten
    blade
    sensitive
    seed
    session
    unlikely
    hilarious
    shaft
    deep
    improve
    neglect
    direct
    hunter
    family
    pick
    sigh
    advocate
    copy
    able
    example
"""
random_list_letters = """
A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z
"""
random_symbol = """
@ % + / \ ! # $ ? ¿ ¡ [ ] : . \( )\  ^ | ~  = ; & * 
""" 
random_list_numbers = """
0 1 2 3 4 5 6 7 8 9
"""
def random_word(w):
	return random.choice(w.split())

def main():
	print("""
	1- weak password (1 uppercase, , contain some numbers, no symbols.)
	2- secure password (includes random symbols, numbers and uppercase.)
	""")
	
	security = int(input("Select a security of the password: \n"))
	if security == 1:
		weak_password()
	elif security == 2:
		strong_password()
	else:
		print("invalid number, please choose 1 or 2")
		main()

def weak_password():
	x = str(random_word(random_list))
	t = str(random_word(random_list_letters))
	y = str(random.randint(0,99))
	z = str(random.randint(1,99))
	password = x + y + t + z
	print("your new password is:\n ", password[(int(random.randint(1,3)))].upper() + password[1::])
	print("Do you want to re-do your password? y/n ")
	yn = str(input())
	while yn == "y":
		weak_password()
		print("do you want to re-do your password? y/n ")
		str(input())
	else:
		print("Do you want to exit program? y/n ")
		yn = str(input())
		if yn == "y":
			exit(0)
		else:
			main()

def strong_password():
	charlong = int(input("How long will the password be? \n"))
	i = 1
	total = 0
	password = []
	if charlong > 0: 
		while i < charlong:
			for _ in range(2):
				password.append(random_word(random_list_letters))
				password.append(random_word(random_list_numbers))
				password.append(random_word(random_symbol))
			i+= 1
		for _ in range(3):
			password.extend(random_word(random_list_numbers))
		for _ in range(2):
			password.append(random_word(random_list_letters))		
		for t in password:
			total += 1
		while total != charlong:
			password.pop(random.randint(1,10))
			total -= 1
	password = ''.join(password)
	print(password, "\n")
	print("Do you want to re-do your password? y/n \n")
	yn = str(input())
	while yn == "y":
		strong_password()
		print("Do you want to re-do your password? y/n \n ")
		str(input())
	else:
		print("Do you want to exit program? y/n")
		yn = str(input())
		if yn == "y":
			exit(0)
		else:
			main()
main()
