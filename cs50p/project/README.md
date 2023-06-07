# PASSWORD GENERATOR
## Youtube video:
<https://youtu.be/stEURVQxAUI>
## Description:
### - General description:
This is program is a random password generator that uses a combination of letters, numbers, and symbols. User can either choose an automatically generate password or customize the generation parameters.
### - 'get_type()' function
This function checks if the input string t matches the pattern "^yes|no$", and returns the input string if it does. If the input string does not match the pattern, the function raises a ValueError exception.

### - "generate()" function
This funciton generates a random sample of leng characters by concatenating the input strings alpha, alpha_upper, numbs, and symb, and then using the random.sample() function to randomly choose leng characters from this concatenated string. The returned list contains the randomly selected characters.

### - get_parameter() function
This function prompts the user to enter a value for a specific parameter based on the integer i(that in the main function a for is traveling acroos all the parameters (letters, numbers, symbols and lenght)  that the user need to put in this function, when them call the no option). It uses regular expressions to validate the user input for certain parameter types and raises a ValueError exception if the input fails the validation. The function returns the validated user input if it passes validation.


## Requirements
The program runs on Python and does not requiere any external library.
## Usage
To use the program, is simpler tha run the file 'password_generator.py'. You will be asked uf you want to aumatically genereta a password or customize the generation parameters. If yoy choose the customization, you will be asked for the desire letters, numbers, symbols and lenght tat will be used in the generation. Else, if you choose to automatically generate a password, you will be shown a twelve random character password.
## Credits
This proyect was developed by Daniel Avila García
## Contact
if you have any further questions or suggestions, you can contact the author via mail: daavilaga@unal.edu.co | da.avila.ga@gmail.com





