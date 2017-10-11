## 1. Hypotheses 
The Null and alternative hypotheses are formulated correctly. Good Job!

Srikanth wanted to check do customers take the bicycles for longer rides than subscribers on average.

For the question raised, the Null hypothesis was set as:
*the average trip duration of 'customers' is the same or shorter than the average trip duration of 'subscribers' with a significance level of alpha = 0.05*

the alternative hypothesis was set as:
*the average trip duration of 'customers' is greater than the average trip duration of 'subscribers' with a significance level of alpha = 0.05*



## 2. Data
The data has the appropriate features (variables) to answer the question and was properly pre-processed to extract the needed values. Good Job!

Two needed variables is the user type and ride time per time.
One colunmn of the dataset is 'User Type', with two different values 'Customer' and 'Subscriber'. 
'Customer' means the customer pays per ride, while 'Subscriber' pay by weekly/monthly/yearly.
Another column is 'Trip Duration', which reveals the trip duration each ride.

Srikanth has extracted these two columns correctly and dropped all the irrelevant variables.
Then, he used filter and mean function to compare and plot the average trip duration of the two types of users.
From the plot, the assumption raised seemed to make sense.

## 3. Test
To test H0 given the type of data and the question asked, I prefer to choose t test or Z test.

The reason is that the hypothesis needs to be tested based on comparision between the means of two groups,
and the t test and Z test could be used to test that is there a difference between means of 2 samples that is approximately normally distributed. 

#### Comparision between t test and Z test:

We have no standard deviation valuation of the population, so the resulting test will not be an exact Z-test since the uncertainty in the sample variance is not accounted for,
which makes t test seems better than Z test.
However, it will still be a good approximation for Z test because the sample size is large enough —— the dataset of Srikanth has 726676 observations.

According to the article [How to choose the right statistical test?](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3116565/)
This question raised is applicaple to the Question 1, is there a difference between groups that are unpaired, and t test is suitable for numerical data of two unpaired groups.

![Figure](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3116565/figure/F0001/)
