Name: Lisa Robinson  
Date: December 1st, 2023   
Course: Foundations of Programming-Python  
Assignment: Assignment 08  
https://github.com/Lisa-jr-batista/IntroToProg-Python-FinalAssignment
# Creating Applications

---

## Introduction
We’ve made it to the end of the Foundations course! 
I feel like I’ve grown so much and learned a huge amount, especially since I started as a total beginner to everything 
coding and am leaving understanding quite a bit more about the practice. In our final few modules we really moved into more advanced ideas and how to organize and test our code. We also were tasked with creating a new program entirely from scratch. This assignment was very difficult because it did not immediately build on a prior one, as most of the other assignments did, and it requires each skill we covered to be displayed. While difficult, I am thrilled about the chance to work through these foundational ideas and am excited to problem-solve like a real coder. 

In Module 8 the focus was on applications and how they are designed, created, and tested. We started by covering code modules (not to be confused with our course modules) and how these modules can be called upon using the “import” command. This is a good way to stay organized and keep a larger application manageable. We then explored designing applications and the steps, diagrams, and implementation of multiple modules that are needed. Finally we worked with testing and quality assurance. 

In Module 9 we learned more about how to remove dependencies in our code so it runs more efficiently and can be used more flexibly. We also spent a lot of time learning about the different systems and strategies software engineers use in industry such as using SCRUM, markdown, Jupyter, and Matplotlib. 

---
## Writing the Initial Program
Starting this assignment I began by creating all the required files (excluding the test ones). I started by copy and pasting the starter file into “Assignment08.py” and then created: “main.py,” “data_classes.py,” “processing_classes.py,” and “presentation_classes.py.” At this point, only the assignment08 file has anything in it, the rest are waiting to be written. 
 


<figure>

![Figure1.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure1.png)
<figcaption>Figure 1: creating needed files for the program (no test files yet)</figcaption>
</figure>



I went into each of the created files and added in the correct script header and changelog. In past assignments, I didn’t always update my change log accordingly so I worked to update the log with each day and change I make to keep this final assignment as true to a real world program as possible. Figure 2 shows an example of one of the script headers, in this case the data_classes file. 

<figure>

![Figure2.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure2.png)
<figcaption>Figure 2: Script header for data classes module </figcaption> 
</figure>

Now I started to move the data from the starter file into the correct modules. I started with the data. This included the constants, variables, Person and Employee classes. Figure 3 shows those elements in the data_classes file. Figure 3 also shows the error I ran into almost immediately where I needed to import the date command from the python library in order for one of the commands in the “employee” class to run correctly. I added that import at the top of the script under the header. 


<figure>

![Figure3.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure3.png)
<figcaption>Figure 3: Adding constants, variables, and data classes to the correct file </figcaption> 
</figure>

Next I went through the remaining starter file and copied and pasted the needed code to the correct modules. In the processing_classes file I needed to import JSON to resolve an error in the File Processor class and in the presentation_classes file I had to import “Employee” from the data_classes file. This creates a module dependency between the files that at the time of this writing (Dec. 1st, Module 8), we have not learned how to correct. Figure 4 shows the import from data_classes. 


<figure>

![Figure4.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure4.png)
<figcaption> Figure 4: Importing the employee code from data_classes file in the presentation_classes module</figcaption> 
</figure>

Now I am ready to transfer the program code from the starter file to the main.py and correct all the import errors. At this point I chose to import the information using the “from-import” method as I thought that would be more efficient than creating aliases and renaming each part of the script that needed it. Figure 5 shows these import commands, including some that are not called on in data_classes. 
 

<figure>

![Figure5.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure5.png)
<figcaption> Figure 5: Import commands in the main file so the script will run.</figcaption> 
</figure>

I paused here and created the needed JSON file: “EmployeeRatings.json” and added in the correct formatting and data so the program wouldn’t error out and attempted my first run. SO MANY ERRORS. Figure 6 shows those initial mistakes to be corrected. Luckily after reading through the error messages, I was able to quickly pinpoint that they all connected to not adding the “Employee” import from data_classes in the processing_classes script. After making this change, I was able to run through the program from the main.py file, add new employee data, save that data to the JSON file, and exit the program– YAY. 
 

<figure>

![Figure6.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure6.png)
<figcaption> Figure 6: All the errors on the first run of main.py with imports to other modules.</figcaption> 
</figure>

---
## Unit Testing - Data Classes
Moving into the testing portion of the program was a bit scary as this was a new skill in module 08, and I still feel very unsure when it comes to fully understanding the testing code. It was nice that I completed the lab for testing before I tackled this part of the assignment so it was still fresh. I started by creating a new testing file: “test_data_classes” and copy and pasted the script header from my lab. I added in the unittest import and luckily was able to copy and paste the Person class test directly from my lab (in both assignment 08 and the lab the attributes for a person were the same). Figure 7 shows the code at this point. 


<figure>

![Figure7.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure7.png)
<figcaption> Figure 7: Test_data_classes.py with imports and class “testperson” code</figcaption> 
</figure>

I was not as lucky with the second data class: “Employee.” I went ahead and copied the code from my lab for “teststudent” but had to modify and add code to this function as it had the additional attributes of review date and review rating. After modifying the code as shown in figure 8, I was able to run the test up to this point with success. I then modified some of my values to cause a failure, which also worked! So the next challenge was figuring out how to test the review date and rating attributes individually. 


<figure>

![Figure8.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure8.png)
<figcaption> Figure 8: Employee test code - this test passed</figcaption> 
</figure>

I decided to start with the review rating as that felt similar to the lab example of GPA because I could raise a value error. I started by modifying the lab code for GPA so it would work with the review rating. After I did the first line, I realized that it seemed like there were two potential errors I might run into, a situation where the user would type a string instead of an integer or where they type an integer that is outside of the expected 1-5 range. So I decided to add another level to the review rating test by adding another value error check. Figure 9 shows my new code for this step. 

<figure>

![Figure9.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure9.png)
<figcaption> Figure 9: Review rating test to check that the value error is raised in both potential user mistakes for this attribute</figcaption> 
</figure>

Now when I went to try to work with the date format, I actually discovered this code was really straightforward and just another assert raises (Value Error) call. I added that code for the date format and ran the test again with success. Figure 10 shows this code and the passed tests. It was at this point that I knew I wanted to edit some of the starter code so that it clearly told the user the correct formatting when they entered in a new employee to try to avoid some of these errors. 

<figure>

![Figure10.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure10.png)
</figure>

<figure>

![Figure10a.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure10a.png)
<figcaption> Figure 10: Test for the review date formatting and successful run
</figcaption> 
</figure>

## Unit Testing - Processing Classes
My next step is working through the testing for the processing classes. Unlike with data classes, I did not have a lab to work through these, just the class recording and Arya’s video demo. To work through this portion and my tests for the presentation classes, I coded with Arya’s demo and copied his code as he worked. This allowed me to pause and correct as needed to ensure I was writing the correct commands. I started with the script header like normal and then created a temporary file so my test would not corrupt my actual data. Figure 11 shows the set up of that file and the closing of it. 

<figure>

![Figure11.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure11.png)
<figcaption> Figure 11: setting up the temporary file for processing classes tests
</figcaption> 
</figure>

While following along with Arya was incredibly helpful, it was not foolproof. The demo was using different data than assignment 08 and Arya likes to use the “first_name”, “last_name” formatting structure while our starter code for assignment 08 uses “FirstName”, “LastName”. These are minor issues, but when your syntax is wrong in Python, literally nothing will work. After adding in all the code I followed in the demo, I failed both tests and was drowning in a sea of red text. Figure 12 shows those early errors.  

<figure>

![Figure12.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure12.png)
<figcaption>Figure 12: All the errors with the testing of the processing classes. 
 </figcaption> 
</figure>

This was quite the mountain to overcome. I was able to address the first error fairly easily. In the demo, the call “read_data_from_file” did not match what I needed to use in the assignment “read_employee_data_from_file.” Easy fix. However, I ran into a headache after that point because I could not figure out why it still was not running correctly. Figure 12 above shows a bit of the error message that was throwing the most problems. The error kept directing me to the “processing_classes” module and the actual function I was testing. Figure 13 shows that function.  

<figure>

![Figure13.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure13.png)
<figcaption> Figure 13: The read employee data from file function I am attempting to test – major errors happening that need to be addressed. 
</figcaption> 
</figure>

This function code looks a lot different from the code we worked with in the lab and module 8. I wondered if it was due to some error handling we will work on in Module 9 which is why it did not look familiar. I eventually realized that I needed to match arguments in my test to the number of arguments in the function. So it reads: def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee) – This function has THREE arguments and when I attempted to run my test using the demoed code, I only had ONE. I was able to update the call in my test class so it matched the function’s parameters. This means I needed to list a file name (self.temp_file_name), a needed to return a list ([ ]), and I had to give the type of employee (Employee). Now my test ran correctly. 
So after spending an embarrassing amount of time trying to figure out why my read data from file test was not working correctly, I immediately realized what was wrong with my write data to file test. 

<figure>

![Figure14.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure14.png)
<figcaption> Figure 14: The code to call the write_employee_data_to_file with my mistake. 
</figcaption> 
</figure>


<figure>

![Figure15.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure15.png)
<figcaption> Figure 15: The function I am trying to test. 
</figcaption> 
</figure>

I simply needed to switch around the two parameters in my test call so it had the file name (self.temp_file_name) first and the list (sample_data) second. Making this quick formatting change allowed the test to run correctly. Now I wanted to move into testing some of the error handling that is present in the read and write functions, but after playing around with the code I struggled to accurately test the FileNotFound error and decided to come back to it after Module 9 was introduced. After module 9, I returned to the processing classes tests and was able to correctly create a test for the FileNotFound errors. An interesting troubleshooting strategy I employed was actually using ChatGPT to figure out why my code was not working correctly. I copied my function for the test and asked the AI what was wrong with it, and Chat was able to break down what I was doing wrong and how to fix it. After updating my code using the AI’s suggestions, I was able to successfully run the test! Figure 16 shows my new code. 

<figure>

![Figure16.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure16.png)
<figcaption> Figure 16: FileNotFound error test. 
</figcaption> 
</figure>

After successfully running the test for FileNotFound I created a new test to see if the JSONDecodeError would be raised when the system was presented with invalid JSON. This was another exploration to understand how these tests work and where I was going wrong. The tests show how my original code might be faulty and helped me change it so it would run as expected. Figure 17(a and b) shows the test for the decode error and the new function in processing classes that it is testing. 

<figure>

![Figure17a.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure17a.png)
<figcaption>Figure 17a: Function in processing_classes to be tested
 </figcaption> 
</figure>


<figure>

![Figure17b.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure17b.png)
<figcaption> Figure 17b: Test to see if the error is raised correctly.
</figcaption> 
</figure>


## Unit Testing - Presentation Classes
As with the last two testing modules, I started by creating a new python file and added my script header and imported unittest. I then decided to test the two functions shown through the module 8 demo when I ask the user for input. The first is for a menu choice. Figure 18 shows the full code for the test_presentation_classes and the first function checks that when “3” is entered the corresponding sequence is called. The second function tests inputting employee data from the user. It uses the patch builtin and asserts that the tested input matches the temporary file. Both tests passed after some modification. The biggest challenge was the employee_type parameter. This didn’t exist in the labs or modules so it required me to do more work outside of the class to understand how to include it in my code correctly. 

<figure>

![Figure18.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure18.png)
<figcaption> Figure 18: test_presentation_classes functions. 
</figcaption> 
</figure>

---
## Mod09 - Removing Dependencies
After module 09 was introduced I went back into my code to eliminate some of the dependencies between classes. Thankfully my data_classes did not call on any other module, so I didn’t need to edit that code, but my processing_classes and my presentation_classes did call on the others. To correct this, I needed to change the times I called on “Employee” from the data_classes to [Object] and then add the exception error message I wanted. Figure 19 shows an example of this change by changing the list I was returning to a list of objects instead of the list of employees. I went through both classes and changed all the times I called on data_classes or another module. I left the import statement up at the top of my script until it grayed out (showing it was no longer being called on), and then deleted the import statement as well. I then tested my main.py code again and it continued to run correctly. 

<figure>

![Figure19.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure19.png)
<figcaption> Figure 19: Changing “employee” to list[object] in order to remove the dependency on other modules. 
</figcaption> 
</figure>


## Personalization
After finishing my code and checking that it runs, I decided to go back and add some personalization to the starter code. I do not feel confident enough to drastically change the code, but I really like that I was able to allow for hyphenated names in my earlier assignments. I wanted to try to replicate that again with this one and the inputted employee data. This turned out to be a good challenge as I could not just use the same code as in earlier projects. I attempted to use the same formatting as shown in figure 20 for input employee data function. I tried to use a double “try-except” block in order to raise a value error in the event that any character of the name was a digit. The issue I discovered is that because I have the Person class with the clear setter, this new code was redundant. 

<figure>

![Figure20.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure20.png)
<figcaption> Figure 20: attempting to use the same code I used in earlier assignments to stop numbers but allow special characters.
</figcaption> 
</figure>

This led me to the Person class in data_classes. After attempting to use the “if any” command again here with no success I went back to ChatGPT and posed my question to the AI. “How can I allow letters and hyphens but not numbers?” ChatGPT was able to point me in the right direction and that code is shown in figure 21. 

<figure>

![Figure21.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure21.png)
<figcaption> Figure 21: New last_name setter for the Person class
</figcaption> 
</figure>

The big change here is this code checks if all the characters entered in the last name are either alphabetic OR a hyphen OR left blank then it will allow the input to stand, otherwise it will raise the value error. After adding in this line of code, I retested my main.py and was able to add an employee with a hyphenated name! Success! 
My next piece of personalization happened in my presentation_classes. I really liked what a classmate had done in her assignment 07 when she created a while loop with her input function. This meant that rather than immediately raise an error when the incorrect value was placed for first name, last name or review date, it would loop back to the same input question and prompt the user to put in the correct formatting. I thought this was so cool and while a little tedious, I wanted to try it in my code. I rewatched Rubiya’s demo from week 8’s class and added three “while” loops to my presentation class. Figure 22 shows my code and how it works when run. 


<figure>

![Figure22a.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure22a.png)
<figcaption> </figcaption> 
</figure>

<figure>

![Figure22b.png](..%2F..%2F..%2FScreenshots%20for%20Final%2FFigure22b.png)
<figcaption> Figure 22: Updated while loops in presentation_classes to circle back and prompt users to enter in correct data.
</figcaption> 
</figure>
---
## Summary
In conclusion, I created a full multi-module application that reads current data, writes new input from the user, saves it to a JSON file, provides error handling, and tests the applications functions. I also went in to eliminate some of the dependencies between the modules and added some personalization to make the application more readable and user-friendly. I learned how important attention to detail is and how to better utilize resources when I do not have an answer. I am still learning why the code works the way it does and how to best explain what I am asking the code to do, but I am well on my way to being competent in python! 
