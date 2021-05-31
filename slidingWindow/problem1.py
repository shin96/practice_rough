#count the number of consonent.
#input n, string, 
#output count of consonants

n = input()
string = input().strip()
result = 0
vowels = ['a', 'e', 'i', 'o', 'u', ' '] #a        b        f        e //20
for char in string: 
    if not (char.lower() in vowels):
        result += 1

print(result)