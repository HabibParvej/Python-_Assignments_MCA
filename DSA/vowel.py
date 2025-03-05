class Frequency:
    def countVowel(self):
        s = input("Enter a string: ")
        vowels = "aeiouAEIOU"
        freq = {}  

        for char in s:
            if char in vowels:
                if char not in freq:
                    freq[char] = 1  
                else:
                    freq[char] += 1 
        print(freq)

ob1 = Frequency()
ob1.countVowel()

