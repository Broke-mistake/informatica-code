# lijsten
ALPHABET   = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
rotor_plug = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ROTOR_SET1 = ['e','k','m','f','l','g','d','q','v','z','n','t','o','w','y','h','x','u','s','p','a','i','b','r','c','j']
ROTOR_SET2 = ['a','j','d','k','s','i','r','u','x','b','l','h','w','t','m','c','q','g','z','n','p','y','f','v','o','e']
ROTOR_SET3 = ['b','d','f','h','j','l','c','p','r','t','x','v','z','n','y','e','i','w','g','a','k','m','u','s','q','o']
ROTOR_SET4 = ['e','s','o','v','p','z','j','a','y','q','u','i','r','h','x','l','n','f','t','g','k','d','c','m','w','b']
ROTOR_SET5 = ['v','z','b','r','g','i','t','y','u','p','s','d','n','h','l','x','a','w','m','j','q','o','f','e','c','k']
REFLECTOR  = ['e','j','m','z','a','l','y','x','v','b','w','f','c','r','q','u','o','n','t','s','p','i','k','h','g','d']

# variabelen
rotor_left = ROTOR_SET1
rotor_center = ROTOR_SET2
rotor_right = ROTOR_SET3
rotor_end = REFLECTOR   
rotor_left_index = 0 # 0 - 25
rotor_center_index = 0
rotor_right_index = 0

# strings
# string_input = "jhuuuefdyoelnibowkjqunxqlv".replace(" ", "").lower() #jhuuuefdyoelnibowkjqunxqlv
string_input = "ijhs".replace(" ", "").lower() 

# ALPHABET.index(rotor_right[(cur_index + rotor_right_index) % 26]) zegt op de hoeveelste plaats de letter van de rotor, 
# in het alphabet zit, dus de B van de rotor it op de 1 plaats in het alphabet
# en dat is dus cur_index, die voer je in de rotor in + de draai van de rotot 

string_output = []

for char in string_input:
    cur_index = rotor_plug.index(char)
    print(f" {rotor_plug.index(char)}")
    print(f" {rotor_right[(cur_index + rotor_right_index) % 26]}")
    cur_index = ALPHABET.index(rotor_right[(cur_index + rotor_right_index) % 26])
    print(cur_index)
    
    
    cur_index = ALPHABET.index(rotor_center[(cur_index + rotor_center_index) % 26])
    print(f"rotor_center: {ALPHABET[cur_index]}")

    cur_index = ALPHABET.index(rotor_left[(cur_index + rotor_left_index) % 26])
    print(f"rotor_left: {ALPHABET[cur_index]}")
    # fout
    cur_index = ALPHABET.index(rotor_end[cur_index])
    print(f"rotor_end: {ALPHABET[cur_index]}")
    # fout
    cur_index = rotor_left.index(ALPHABET[(cur_index) % 26])
    print(f"rotor_left:  {rotor_left[cur_index]}")

    cur_index = rotor_center.index(ALPHABET[(cur_index - rotor_left_index) % 26])
    print(f"rotor_center:{rotor_center[cur_index]}")

    cur_index = rotor_right.index(ALPHABET[(cur_index - rotor_center_index) % 26])
    print(f"rotor_right: {rotor_right[cur_index]}")

    cur_index = ALPHABET.index(rotor_plug[cur_index - rotor_right_index])
    print(f"plug: {ALPHABET[cur_index]}")

    string_output.append(ALPHABET[cur_index])

    rotor_right_index +=1
    if rotor_right_index >= 26:
        rotor_right_index = 0
        rotor_center_index +=1
        if rotor_center_index >= 26:
            rotor_center_index = 0
            rotor_left_index += 1
    

print("".join(string_output))
print(f"rotor_left_index = {rotor_left_index}")
print(f"rotor_center_index = {rotor_center_index}")
print(f"rotor_right_index = {rotor_right_index}")
