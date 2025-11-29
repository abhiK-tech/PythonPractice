list_of_cloud= ["aws","azure","gcp","ibm"] #list of cloud
print(list_of_cloud)  

list_of_cloud.append("oracle") #append a new cloud at the end
print(list_of_cloud)

list_of_cloud.insert(1,"alibaba") #insert a new cloud on specific index
print(list_of_cloud)

print(len(list_of_cloud)) #number of clouds

for cloud in list_of_cloud: #iteration of cloud
    print("")
    print(cloud)