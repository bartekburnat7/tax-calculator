# __TAX Calculator__

Tax Calculator is a tool that by anyone that is curious how much tax they would be paying on a given amount. I wanted to create an application that could be used by companises in the real world or a handy tool that individuals could use. This calculator is made for the UK users as each country has their own TAX bands and requirements, but this could be added in the future.

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

I tested the application by entering in different type of data

- numbers: 123, 999999, 3.14 , 2000.11111
- text: hello, jhon, bye1234
- special characters: @, £, %, ^

### __Bugs__

- From my testing I have not found any bugs with the application so far

### __Validator Testing__

- There was no major errors returned by the https://pep8ci.herokuapp.com/ validifier

## Deployment

I deployed the application to a cloud based platfor heroku which enables you to interact with the app througha console:

- Step-by-step guide:
    - Connect github and find the repository name youi want to deploy
    - In settings add the Python then NodeJs in the buildpack section
    - Scroll down to the bottom of "Deploy" and hit the "Deploy Branch"
    - The application will now be deployed and when done you will be able to open it by clicking the "open app" button on the top rights

## __Credits__

- Websites I've used:
    - https://www.geeksforgeeks.org/
    - https://stackoverflow.com/