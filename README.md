# __TAX Calculator__

https://tax-calculator-3-f7d403fba15a.herokuapp.com/

Tax Calculator is a tool that by anyone that is curious how much tax they would be paying on a given amount. I wanted to create an application that could be used by companies in the real world or a handy tool that individuals could use. This calculator is made for the UK users as each country has their own TAX bands and requirements, but this could be added in the future.

![Am i responsive](/images/am_i_responsive.png)

## __How to use__

The tool works as followed. You are welcomed with a message which ask you to enter your name, after you have prompted your name and hit enter you will be taken to the next step. You will now be asked to input your annual income in British Pounds which you would like to calculate. Then the application automatically finds your TAX Band and proceeds to give you the exact amount how much TAX you will need to pay for this amount.

## __Features__

- __Welcome Message__
    - You are greeted with a welcoming message which explains to the user that this application should only be used to calculate tax within the uk.

![Welcome](/images/python_welcome.png)

- __TAX Band Detection__
    - The software will automatically put you in the right TAX bracket so that your income gets calculated correctly.
    - It accepts any amount and returns the tax amount you would need to pay to the user with the associated Tax Band.

![tax bands](/images/tax_band.png)

- __Type Handler__
    - The program tests first if you input a float type value, if you have not then there is a "Value Error" returned. After this ValueError the program tests if its either a number value or any other value for example text. If a value other than a number is input, then it wont be accepted and you will get a warning and you will have to input your Yearly Income again. If the Input type is in fact a number, the program will begin the calculation.

![Type](/images/false_value.png)

### __Future Features__

- The user can choose what country they would like to calculate tax.
- A breakdown of tax per month or week
- Option to save or share your results

## __Testing__

I tested the application by entering different type of prompts into the tax calculating input to check if the application handles the data accordingly and doesn't return any unexpected errors that would break the code. These are the following inputs I have used to test the code:

- numbers: 123, 999999, 3.14 , 2000.11111
- negative numbers: -123
- text: hello, john, bye1234
- special characters: @, £, %, ^
- blank inputs

The first input takes the name of the user and should only except alphabetical characters. Any other type of input should raise a value error and prompt you to re enter your name.

![text number](/images/tax_num.png)![text special character](/images/tax_special.png)
![blank text input](/images/tax_blank.png)![text and number](/images/tax_text_num.png)

From my testing I found that the first input works as expected and doesn't except any of the following values and raise a value error on each. I consider this as a PASS. I then run the same exact tests on the second input for the users earnings prompt. This input should only accept numerical values, float values that are in the positive and raise a value error if the data doesn't match the criteria.

![text](/images/tax_text_2.png)![special](/images/tax_special_2.png)
![blank num](/images/tax_blank_2.png)![negative number](/images/tax_negative_num.png)

The user earnings input works as expected and doesn't raise any unexpected errors that would break the code. The application passed all the tests and I can strongly say that the code is ready to be submitted.

### __Bugs__

- From my testing I have not found any bugs with the application.

### __Validator Testing__

- I decided to use the pep8 CI Python Linter which you can find at https://pep8ci.herokuapp.com/ . After scanning the run.py file the application returned two errors regarding the length of two lines as they were over the recommended limit.

![Error](/images/pep8_error_message.png)![code](/images/pep8_validator_error.png)

I solved this problem by separating the input message into two variables named: text_one and text_two, which i then called later inside the while loop. This significantly shortened the length of the print function and fixed the pep8 errors.

![solved code](/images/pep8_solved.png)

## __Deployment__

I deployed the application to a cloud based platform heroku which enables you to interact with the app through console:

- Step-by-step guide:
    - Connect github and find the repository name you want to deploy
    - In settings add the Python then NodeJs in the build pack section
    - Scroll down to the bottom of "Deploy" and hit the "Deploy Branch"
    - The application will now be deployed and when done you will be able to open it by clicking the "open app" button on the top right

## __Credits__

- Websites I've used:
    - https://www.geeksforgeeks.org/
    - https://stackoverflow.com/