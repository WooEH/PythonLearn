ID = int(input())
Name= input()

Major = "Software"

if (ID%100)>=50:
    Major = "History"

print("ID : %d"%ID)
print("Name : %s"%Name)
print("Major : %s"%Major)