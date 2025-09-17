from owner import Owner
owner=Owner()

print(owner)

owner.name='Sarah Salah'
print(owner)
try:

    owner1=Owner(id=202140002,name="Kanggg")

except ValueError as e:
    print(f"Error:{e}")
