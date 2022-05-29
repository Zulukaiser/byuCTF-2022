# byuCTF 2022 Miscellaneous FunFact

In the challenge Fun Fact we were provided with an obfuscated python script. If we take a closer look at the script we see the import of the base64 module a string variable with some non human-readable text an the last line executes the base64 decoded string.
So the first thing we should do is to get the string human-readable, to understand what is being executed at the end.
If we decode the base64 string, we get a new script in a single line. If we make a new line, where the *\n* is (except for inside the strings), we can reconstruct the layout of the script and can understand the logic better.
We can have a look at the logic now.
We see in the *main()* function, that we are prompted to make an user input. There are 3 cases what the script does in response to the user input, every input, other than 1, 2 or 3 will loop back to the input prompt. If we input 1, we get to the function *option_one()*, which prints out "Just kidding, it's not that easy".
So option one won't help us. If we input 2, we get a random fact about ocean cratures. This option won't help us either. Now if we put 3 as our user input, we get to an interesting function, which asks for another user input. There now is an array, that gets XORed and a key is generated from the random array. The user input gets now encrypted with the key and some maths. The program compares the encrypted user input with a string and if they match, we get the output "Success!" if they don't match, we get the output "Try again".
After understanding the code, it's safe to say, that the user input in the function *option_three()* is our flag and we have to reconstruct it.
First thing we can do is get the contents of random_array. The contents aren't random, so we can follow the logic and reconstruct it's contents. Let's look at the *xor()* function.
The *xor()* function gets 2 strings as attributes, string a and string b, and introduces another varaible called key which also is the return varaiable, so it's the value that the variable **random_array** gets. Now we have a while loop, that appends to the key list with some xor logic. We can copy this function and let it run with the attributess that are provided within the **random_array = xor(a, b)** call and print the key at the end of the while loop.
We get a list:
```python
random_array = [35, 28, 10, 3, 18, 21, 65, 8, 23, 65, 31, 28, 64, 83, 72, 29, 9, 73, 21, 82, 17, 3, 27, 89, 83, 6, 6, 18, 90, 22, 74, 0, 2, 20, 31, 76]
```
We can now have a look at the other_random_array variable. Basically this variable is a list with the characters [a-z][A-Z][0-9] ordered and looks like this:
```python
other_random_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c']
```
the encryption key follows the logic **other_random_array[random_array[0] + random_array[8]]** which is **other_random_array[35+23]**
so we can get the character which is stored in key

**other_random_array[58] = 'W'**

**key = 'W'**

Now that we know the key we can make our own function *decode()*, that Brute-Forces the right user input one character at a time.
Our function *decode()* should have the encrypted variable, which essentially is the string our encrypted flag gets compared to, a list where we store our input data characters in.
We can iterate through our encrypted string one character at a time and do the same xor logic like we do in the encryption process. We need a while loop which runs while our xor logic with the key doesn't return the character in the encrypted variable and our iterable is less than 128, so we won't get an infinite loop if we have some false code. Than we can append the iterabel outside of our nested loop to the inputdata list. After we've gone through the whole encrypted variable, we can return our solution, as we convert our contents of the inputdata list to characters and join them together in a string. The whole logic should look like this:
```python
def decode():
    encrypted = 'g%4c$zc%dz4gg;'
    inputdata = []
    for x in encrypted:
        i=0
        while chr(i ^ 87) != x and i < 128:
            i = i + 1
        inputdata.append(i)
    solution = "".join([chr(x) for x in inputdata])
    return solution
```
Now we have to call our *decode()* function in *main()* and we can retrive our flag.
