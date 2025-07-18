#Greetings
print("Welcome to the secret auction program.")

def dict_appending():
    more=True
    # Create an empty dict
    bids = {}
    while more:
        # Ask for name
        name = input("What is your name : ")
        # Ask for bid
        bid = int(input("What's your bid : "))
        bids[name]=bid
        ask = input("Are there any other bidders? 'Yes' or 'No' : ").lower()
        print("\n"*100)
        if ask == "no":
            more = False
    return bids

def winner(bids):
    name=""
    amount=0
    for i in bids:
        if bids[i]>amount:
            name=i
            amount=bids[i]
    name_list=[]
    for i in bids:
        if bids[name]==bids[i]:
            name_list.append(i)
    return name_list

def amount(bids):
    amount=0
    for i in bids:
        if bids[i]>amount:
            amount=bids[i]
    return amount
bids_dict=dict_appending()
winner_name=winner(bids_dict)
winning_amount=amount(bids_dict)
# print(winning_amount)
# print(winner_name)
final_winner=', '.join(winner_name)
output_string=f"The winner : {final_winner}\nWith a bid amount : {winning_amount}"
print(output_string)
