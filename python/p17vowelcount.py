#17. Create a class VowelCounter with a method count_vowels that returns the count
#of vowels in a given string. What will be the output of
class VowelCounter:
  def countVowels(self,str):
    count=0
    for ch in str.lower():
      if ch in "aeiou":
        count+=1
    return count
s=VowelCounter()
print("Total Vowels in string is:",s.countVowels("AdityaChavan"))