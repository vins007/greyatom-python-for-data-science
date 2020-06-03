# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
loan_status = data['Loan_Status'].value_counts()
print(loan_status['Y'])
loan_status.plot(kind='bar')
plt.show()
#Creating a new variable to store the value counts
#step 2

property_and_loan = data.groupby(['Property_Area','Loan_Status'])

property_and_loan = property_and_loan.size().unstack()

#Plotting bar plot

property_and_loan.plot(kind='bar')
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()
# Step 2
#Plotting an unstacked bar plot




#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot

education_and_loan = data.groupby(['Education','Loan_Status'])

education_and_loan = education_and_loan.size().unstack()

#Plotting bar plot

education_and_loan.plot(kind='bar')
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column

graduate = data[data['Education']== 'Graduate']
#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education']=='Not Graduate']

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density',label='Graduate')

#Plotting density plot for 'Graduate'

not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')
plt.legend()
#For automatic legend display


# Step 5
#Setting up the subplots
fig , (ax_1,ax_2,ax_3) = plt.subplots(3,1)

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])

#Setting the subplot axis title
plt.title(' Applicant Income')


#Plotting scatter plot


ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])

#Setting the subplot axis title

plt.title(' Applicant Income')

#Creating a new column 'TotalIncome'

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

#Plotting scatter plot

ax_3.scatter(data['TotalIncome'],data['LoanAmount'])



#Setting the subplot axis title
plt.title(' Total Income')



