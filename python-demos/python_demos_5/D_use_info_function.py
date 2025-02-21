# from greetings_functions import display_info
from A_greetings_functions import display_info as display

# display_info('Cherina', 7, favourite_place="Your bed")
display('Cherina', 7, favourite_place="Your bed")

anagha_info = 'Anagha', 9, 'Reading', 'Mumbai'
display(anagha_info[0], anagha_info[1],  anagha_info[2], anagha_info[3])

# unpacking
# used when we call the function
display(*anagha_info)
