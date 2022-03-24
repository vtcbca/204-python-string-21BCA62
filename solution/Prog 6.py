s=input("Enter any string:")
l=len(s)
print("symmetrical string" if s[0:l//2]+s[l//2:] else "Asymmetrical string")
