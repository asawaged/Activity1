from statistics import mean

def display_title():
   print("The Test Scores program")
   print("Enter -999 to quit")


def main():
   display_title()
   grades = getScores()
   grade = mean(grades)
   abcGrade = getGrade(grade)
   print("\nScores:          ",grades)
   print("Total:           ",sum(grades))
   print("Number of Scores: ",len(grades))
   print("Average Score:   ",grade)
   print ("Letter grade:   ",abcGrade)
   print("\nBye!")



def getScores():
   grades = []
   while True:
      grade = int(input("Enter test scores: "))
      if grade == -999: return grades
      grades.append(grade)
      for grade in grades:
         if grade < 0 or grade >= 101:
            print("Enter a grade 0 through 100. Score discarded. Try again.")
            grades.remove(grade)


def getGrade(grade):
   best = 100
   if grade >= best - 8:
      return 'A'
   elif grade >=  best - 12:
      return 'B+'
   elif grade >= best - 18:
      return 'B'
   elif grade >= best - 22:
      return 'C+'
   elif grade >= best - 30:
      return 'C'
   elif grade >= best - 40:
      return 'D'

   else:
      return 'F'

main()