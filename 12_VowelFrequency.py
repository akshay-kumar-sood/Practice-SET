# VOwel Frequency Analyzer

sentence=input("ENter a sentence : ")
cnt=0
sentence=sentence.lower()

for i in sentence:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' ):
        cnt+=1

print(f"Total vowel present is {cnt} ")
