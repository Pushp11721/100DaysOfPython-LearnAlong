word_per_page=0
pages=int(input("Number of pages : "))
# word_per_page == int(input("Number of words per page : "))
word_per_page=int(input("Number of words per page : "))

#Use print statement to find error
print(f"pages = {pages}")
print(f"word per page = {word_per_page}")

total_words=pages*word_per_page
print(total_words)