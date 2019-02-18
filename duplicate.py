



def Remove(names):
    print("Activity 5 List Deduplicator Function\n")
    print("Initial List of Names\n ['mary','mary','bill','sam','maria','kahn','bill','barry','george','hank','belinda','maria','karthik']\n")

    print("List of unique names after running through the de-duplicator program")


    final_list = []
    for num in names:
        if num not in final_list:
            final_list.append(num)
    return final_list



names = ['mary','mary','bill','sam','maria','kahn','bill','barry','george','hank','belinda','maria','karthik']

print(Remove(names))


