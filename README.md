# python-challenge
As part of my submission for Module 3 - Python Challenge, I have submitted the below:
- pybank directory, containing resources used, code, and txt file out from the code
- pypoll directory, containing resources used, code, and txt file out from the code

# Code source 
The following code was provided from the bootcamp tutor, to aid in calculating and printing the percentages of votes received by the candidates in the pypoll activity. 

  #the below code was used to calculate the percentage of votes received by each candidate: 
    percentages = {key: round((val / len(voterID)*100),3) for key, val in votes.items()}

  #the below code was used to print both the number and percentage of votes received by each candidate: 
    output_2=(f"{key}: {percentages[key]}% ({val})\n")
