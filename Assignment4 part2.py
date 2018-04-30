
# question 1
S = [(2*x+1) for x in range(0,51)]
# print(S)

# question 2
# S = {3*x | 0<x<5}

# question 3
Spongebob = {'fname':'Spongebob','lname':'Squarepants','age':32,'color':'yellow','sex':'male','employ':'fry_cook','species':'sponge'}
patrick = {'fname':'Patrick','lname':'Star','age':29,'color':'red','sex':'male','employ':'unemployed','species':'starfish'}
Krabs = {'fname':'Krusty','lname':'Krab','age':76,'color':'blu','sex':'male','employ':'owner and founder of the Krusty Krab','species':'Crab'}
Sandy = {'fname':'Sandy','lname':'Cheeks','age':45,'color':'brown','sex':'female','employ':'scientist and martial artist','species':'squirrel'}
Plankton ={'fname':'Sheldon J.','lname':'Plankton','age':76,'color':'green','sex':'male','employ':'owners and founders of the Chum Bucket','species':'copepod'}
# combining residents together
resident = {'spongebob':Spongebob,'patrick':patrick,'mr.krabs':Krabs,"sandy":Sandy,'plankton':Plankton}
choice=input("Which character are you finding: ").lower()


# printing function
print ("\"I'm",resident[choice]['fname'],resident[choice]['lname']+'! I\'m',resident[choice]['age'],"years old and I'm the",resident[choice]['color']+'est',resident[choice]['species'],"in Bikini Bottom!\"")
