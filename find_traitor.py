followers = open("followers.txt", 'r')
following = open("following.txt", 'r')

name = []
for each in followers.readline():
    if(each != '[' and each != ']'):
        name.append(each)
    
names = ("".join(name)).split(',')

followers_names = []
for each in names:
    followers_names.append(each.strip().replace("'", ""))

name = []
for each in following.readline():
    if(each != '[' and each != ']'):
        name.append(each)

names = []  
names = ("".join(name)).split(',')

following_names = []
for each in names:
    following_names.append(each.strip().replace("'", ""))

print("Your Followers: " + str(len(followers_names)))
print("Your Following: " + str(len(following_names)))
print()

for following_name in following_names:
    if following_name not in followers_names:
        print(following_name)