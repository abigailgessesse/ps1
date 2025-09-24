# Question 1

Try to take full advantage of [Markdown](https://www.google.com/url?q=https%3A%2F%2Fguides.github.com%2Ffeatures%2Fmastering-markdown%2F) so that your answers are clearly and beautifully formatted!


0. **Textbook exercise 2.1**
1. **Textbook exercise 2.2** (parts 1, 2, and 3)

---

### **Textbook Exercise 2.1**

#### 1. We’ve seen that `n = 42` is legal. What about `42 = n`?  
    Not legal.  

#### 2. How about `x = y = 1`?  
    Not legal.

#### 3. In some languages, every statement ends with a semi-colon `;`. What happens if you put a semi-colon at the end of a Python statement?  
    It will ignore it, but you generally shouldn't put one as it is not required in Python.

#### 4. What if you put a period at the end of a statement?  
    There will be a syntax error.

#### 5. In math notation, you can multiply `x` and `y` like this: `x y`. What happens if you try that in Python?  
    It will not recognize it as multiplication of two separate variables. You must do x * y.


# Question 2A

With Python, we can use math operators to perform calculations. For example, we can add two numbers together using the `+` operator, or multiply two numbers together using the `*` operator.

Before we try that, let's first try to put it into english how to do this.

#### EXAMPLE: Calcuate and return the volume of a sphere given its radius.

##### The volume of a sphere with radius  𝑟  is  4/3π𝑟3 . 

    Answer: 
    The volume can be a variable `volume` and the function can return the value of `volume`.
    We can use the math module to get the value of pi.
    The formula is the same thing as 4/3 multiplied by pi multiplied by  the radius to the power of 3
    This can be written as `volume = 4/3 * math.pi * radius ** 3`

 #### Your Turn: Return the total wholesale cost of `copies` copies.
    
 ##### Suppose the cover price of a book is  $24.95 , but bookstores get a  40%  discount. 
 ##### Shipping costs  $3  for the first copy and 75 cents for each additional copy.

    Answer:
    The total wholesale cost can be a variable 'totalCost' and the number of copies will be the variable 'copies'
    Use the formula: totalCost = (3 + 0.75 * (copies - 1)) * (0.6 * 24.95) 
    This will automatically charge the 3 dollars for the first copy shipping, then charge 0.75 for the rest of the copies shipping.
    Then it'll simply charge the cover price, after the 40% discount.
    **One important thing to note**: If the number of copies ordered is 0, an additional if statement will be needed under that states: "if 
    copies is less than 1, update the totalCost to equal 0."
