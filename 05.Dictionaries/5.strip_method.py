sherlock = '''  Mr. SherlockHolmes, who was usually
 very late in the mornings, save upon
 those not infrequent occasions when he
 was up all night, was seated at the break
fast table. I stood upon the hearth-rug and picked
 up the stick which our visitor had left behind him
 the night before. It was a fine, thick piece of wood,
 bulbous-headed, of the sort which is known as a
 “Penang lawyer.” Just under the head was a broad
 silver band nearly an inch across. “To James Mor
timer, M.R.C.S., from his friends of the C.C.H.,” was
 engraved upon it, with the date “1884.” It was just
 such a stick as the old-fashioned family practitioner
 used to carry—dignified, solid, and reassuring.
 “Well, Watson, what do you make of it?”
 Holmes was sitting with his back to me, and I
 had given him no sign of my occupation.
 “HowdidyouknowwhatIwasdoing? Ibelieve
 you have eyes in the back of your head.”   '''
 
 
 
new_words = sherlock.split(' ')
 
# =============================================================================
# print(new_words)
# =============================================================================


for i in range(len(new_words)):
    new_words[i] = new_words[i].strip('\n')
    
print(new_words)