counties = ["Arapohoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

Temperature = int(input("What is the temperature outside? "))

if Temperature> 80:
    print("turn on the A/C")
else:
    print("Open the Windows")


Score=int(input("What is the exam score?"))




Score = 95
if Score >= 90:
    print("your grade is A")
else:
    if Score >= 80:
        print("your grade is B")
    else:

        if Score >=70:
            print("your grade is C")
        else:
            if Score >=60:
                print("your grage is D")
            else:
                print("your grade is F")



score=int(input("What is your test score? "))

if score >= 90:
    print("your grade is A")
elif score >= 80:
    print("your grade is B")
elif score >=70:
    print("your grade is C")
elif score >=60:
    print("your grage is D")
else:
    print("your grade is F")


numbers = [0, 1, 2, 3, 4, 5]
for num in numbers:
    print(num)

abc = input("what is your name?")
print(abc)

counties = ["Arapohoe","Denver","Jefferson"]
for i in range(len(counties)):
    print(counties[i])

counties_tuples=("Arapohoe","Denver","Jefferson")
for i in range(len(counties_tuples[i])):
    print(counties_tuples[i])

for i in len(counties_tuples):
    print(counties_tuples[i])

for county in counties_tuples:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)


for county in counties_dict.values():
    print(county)

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for i in voting_data:
    print(i)

for i in len(voting_data):
    print(voting_data[i])

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for county in range(len(voting_data)):
    print(county)

for county_dict in voting_data:  

     print(county_dict.values())


for county_dict in voting_data:

     print(county_dict['registered_voters'])

for county_dict in voting_data:

     for key, value in county_dict.items():

         print(value)

my_vote = int(input("How many votes did you get in election? "))
tot_vote = int(input("what is the total votes in the election? "))
percentage_vote = (my_vote/tot_vote)*100
print("i received " + str(percentage_vote) + " % of the total votes.")
print(f'I recieved {my_vote/tot_vote * 100} % of the total votes')
