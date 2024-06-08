# Assignment 2: Choose Your Own Adventure

Hi Margo, for your second assignment I will keep it very open-ended to give you a lot of creative freedom. The story can be about whatever you want it to be but each section should follow this general idea.

## Expectations:
- Each part of the story should be broken up into a function
- You should pass the previous input to the next function using parameters
- The story should be at least 3 sections long
- You can take inputs in any way but I recommend integers.
- You can also have multiple choices that lead to the same outcome.

## Help:
- You may want to print out multiple lines at once. You can do this using multiple print statements or combining them into one string using \n.
  - Ex-  "Hello\nThis is a new line\nThis is a new line"
- You may realize that you will need one function per part of the story.

## Example:
I have only included one example here to leave it very open to you.
> Where would you like to go?  
> 1- The Movies  
> 2- The Grocery Store  
> 3- The Zoo  
> Enter your choice here: **2**

Here is an example code structure:

```python
    def one(a):
        if a == 1:
            two(1)
        elif a == 2:
            two(2)
        #continue with the same pattern
```