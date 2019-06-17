import t_to_s as t2s
import s_to_t as s2t
a=input("enter \n1 for text to speech \n2 for speec to text\n")
while(a):
	if a=="1":
		t2s.text2speech(input("enter the text "))
		
	elif a=="2" :
		print(s2t.recognize())
	else:
		print("invalid input")
	a=input("enter \n1 for text to speech \n2 for speec to text\n")
print("shutting down")
