from playsound import playsound
print("Enter Your Choice::")
print("A-Alone\n")
print("O-on my way\n")
print("AA-Alone.pt\n")
print("S-Spacemelody\n")
print("F-Fadded\n")
print("Enter Choice::\n")
c=input()
if(c=='A' or c=='a') :
    playsound('C:\\Users\\Admin\\Music\\English Songs\\Alone.mp3')
if(c=='O' or c=='o') :
    playsound('C:\\Users\\Admin\\Music\\English Songs\\Onmyway.mp3')
if (c=="AA" or c=="aa"):
    playsound('C:\\Users\\Admin\\Music\\English Songs\\Alone.pt.mp3')
if (c=='s' or c=='S'):
    playsound('C:\\Users\\Admin\\Music\\English Songs\\Spacemelody.mp3')
if (c=='f' or c=="F"):
    playsound('C:\\Users\\Admin\\Music\\English Songs\\Fadded.mp3')
input()