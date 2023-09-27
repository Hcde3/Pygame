def all_upper(my_list):
    return [x.upper() for x in my_list]
space = ("""














""")
pts = 0
p = 1
lvs = 3
guesses = []
countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Ivory Coast', 'Djibouti', 'Democratic Republic of the Congo', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Republic of the Congo', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe' ]
countries = all_upper(countries)
print("54 Countries to be guessed.")
while p == 1:
    guess = input("Guess an African Country: ")
    guess = guess.upper()
    if guess in guesses:
        print(space)
        print("Already Guessed")
    elif guess in countries:
        pts += 1
        print(space)
        print("Correct")
        print(pts,"Points")
        guesses.append(guess)
    if not guess in countries:
        if guess == "ALLD":
            pts = 54
        else:
            lvs -=1
            print(space)
            print("Incorrect")
            print(lvs,"Lives Left")
    remaining = 54 - pts
    print(remaining,"Countries remaining.")

    if lvs == 0:
        p = 0
        win = 0
    if pts == 54:
        p = 0
        win = 1
if win == 1:
    print("Congrats you got them all")
if win == 0:
    print("You ran out of lives :(")
    
    