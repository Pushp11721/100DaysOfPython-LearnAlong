#Reproduction of bugs -- When a bug does not act on every situation,
#or we can cay say it acts only for a certain condition these types of bugs are difficult to debug.

from random import randint
dice_image=["1","2","3","4","5","6"]
#dice_num=randint(1,6) -- changing it to randint(0,5) to follow proper indexing of list
dice_num=randint(0,5)
print(dice_image[dice_num])
