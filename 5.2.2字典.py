voted={}
def check_votre(name):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name]=True
        print("let them vote")


check_votre("tom")
check_votre("mike")
check_votre("mike")
voted.get('wa')
print(voted)



