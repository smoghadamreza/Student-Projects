def convert_distance(miles):
    km = miles * 1.6
    result = "{miles} miles equals {km} km".format(miles=miles, km=km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 kmkm


def nametag(first_name, last_name):
	return("{first_name} {last_name}.".format(first_name = first_name, last_name = last_name[0]))

print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."



def is_palindrome(input_string):
    reverse_string = ""
    new_string = input_string.lower().replace(" ","")
    for n in range(1, len(new_string)+1):
        reverse_string += new_string[-n]
    if new_string == reverse_string:
        return True
    return False
print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak"))
print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True