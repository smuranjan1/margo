# Hi Margo!

## Here is your first assignment: Rock Paper Scissors

### Important things I forgot to teach you!!!!
**Along with >, <, <=, >=, ==, there is also != which means does not equal.**  
**You can have multiple statements in one if condition using *and* / *or. They do exactly what you think.***  
Example:
```python
    if number > 4 and number < 8:
        print("This number is greater than 4 but less than 8")
    elif number != 3 or number != 5:
        print("This number doesn't equal 3 or 5")
    elif number == 4 or number == 5 or number == 7:
        print("Last case")
```
***Make sure to pay attention to the fact that you have to write number both times***  

Remember to do git pull to get this instructions file on your computer. If you want to view the file like you can on GitHub, right-click the file and hit Open Preview.

All assignments I send will include a list of expectations, you can think of these as requirements that your code should be able to so. I will also include an example output so you can match the format. Please feel free to message me whenever you have any questitons.

Expectations:
- The user can input Rock Paper or Scissors, anything else should print an error
- The second user can also Rock Paper or Scissors, anything else should print an error
- If either output is an error, no result should print
- The game should output who won, make sure to account for all cases including draws

Help:
- try to split the code up into one or two functions called from the main function (rememeber returning)
- You may need to nest if statements or use Booleans to keep track of your errors
- use google or your sister if you need help (google first because you learn just by googling)

Example Outputs: (Bold Text is User Input)
> User 1 Enter Rock, Paper, or Scissors: **Rock**  
> User 2 Enter Rock, Paper, or Scissors: **Paper**  
> User 2 Wins!

> User 1 Enter Rock, Paper, or Scissors: **Scissors**  
> User 2 Enter Rock, Paper, or Scissors: **Paper**  
> User 1 Wins!

> User 1 Enter Rock, Paper, or Scissors: **Scissors**  
> User 2 Enter Rock, Paper, or Scissors: **Scissors**  
> Draw!
  
> User 1 Enter Rock, Paper, or Scissors: **Apple**  
> Error: Enter Rock, Paper, or Scissors Only  
> User 2 Enter Rock, Paper, or Scissors: **Scissors** 

> User 1 Enter Rock, Paper, or Scissors: **Apple**  
> Error: Enter Rock, Paper, or Scissors Only  
> User 2 Enter Rock, Paper, or Scissors: **Chicken**  
> Error: Enter Rock, Paper, or Scissors Only  