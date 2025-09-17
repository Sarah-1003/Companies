from owner import Owner
from company import Company
from department import Department

# Creating company Sarah & Lee"

Sarah_and_lee=Company("Sarah & Lee ")
Sarah_and_lee.addOwner(id=202010001,name="Sarah")
Sarah_and_lee.addOwner(id=202010002,name="Lee")

print(Sarah_and_lee)

d1=Department(Sarah_and_lee.title,dname="HR",empCount=40)
print(d1)


d2=Department(Sarah_and_lee.title,dname="Sales",empCount=60)
print(d2)

d3=Department(Sarah_and_lee.title,dname="IT", empCount=10)
print(d3)