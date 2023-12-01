# Louie Cawood - MoJ Assessment - 01/12/2023
 
## Test 1
The test_1.py contains the code to validate log messages. Running this script indicates the success of the pre-written tests. Some sample log messages are provided in 'sample.log'. 

## Test 2
The test_2.py contains the code to create a csv file containing data about people and their respective courts based on distance and preference. Inside the 'main' block, I pass in the provided 'people.csv' file and create a 'court_data.csv' file. 

## Test 3
The test_3.py contains code to sum the numbers in a date given in string format. Alongside this, 'my_tests_task_3.py' contains unit test to check that my function in test_3.py works as intended.

## Other
I made use of the pandas library in test 2 for two reasons. Firstly, pandas is a nice library to work with in Python, and secondly, pandas seemed a useful tool to use because I felt that working with the data in a tabular format would be most appropriate. 

Lastly, one thing to note is that there is a slight delay when running test_2.py. This is due to the fact that for each person (and postcode) a new API request is made and it takes time to contact the server and get a response. Perhaps in future I would look to find another approach to this problem if I had to make several thousand API requests.