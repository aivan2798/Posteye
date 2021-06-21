#*plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()
knwn_emotions=["Group Rage","Group Apprehension","Group Distress","Group Dejection","Group Surprise","Group Fondness"]
#emotions_count={"Group Rage":0,"Group Apprehension":0,"Group Distress":0,"Group Dejection":0,"Group Surprise":0,"Group Fondness":0}
emotions_count={}
emotions_in=["Group Rage","Group Rage","Group Rage","Group Surprise"]
x=0
round_1=True
for emotions in knwn_emotions:
  #emotions_count[emotions]=emotions_count[emotions]+1
  emotions_count[emotions]=0

for emotions in emotions_in:
    emotions_count[emotions]=emotions_count[emotions]+1
  #print(emotions_count[emotions])
print(list(emotions_count.keys()))