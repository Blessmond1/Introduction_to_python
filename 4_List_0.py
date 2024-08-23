myTechList = ["Python", "Javascript", "Java","ReactJs","C++","PHP","Bootstrap"]
myTechList2 = ["AWS"]

# Adding a new technology

myTechList.append("HTML")

# print a technology in index 2
print (myTechList[2])

#insert a new technology
myTechList.insert(2, "C")
myTechList.insert( 5, "Cybersecurity")

# extend the technology
myTechList.extend(myTechList2)

#remove the technology
myTechList.remove("Cybersecurity")

#pop the technology
myTechList.pop(2)

#delete the technology
del(myTechList[6])


# print the length of the technology
print (len(myTechList))



print (myTechList)