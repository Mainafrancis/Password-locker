# Password-locker
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

## Contributors
1. Francis Mwangi

## Technologies Used
1. Python3


## Dependencies
For the application to run, the following requirements have to be met:
1. One must have at least python3 installed on their device.
2. Install pip

## Set up Instructions
To have the following application in your application follow the following steps:
1. Clone this repository onto the desired location on your local machine using "git clone https://github.com/Mainafrancis/Password-locker.git" in your terminal.
2. Navigate to the location of the application on your terminal
3. Create a virtual environment in the same directory and run <code>pip install -r requirements.txt</code>
4. Run "chmod +x run.py"
5. Run "./run.py"

## Application Description
The application makes use of two classes, the user class and the credentials class. Inside the user class lies a method to instantiate an object or rather instance of the user class. The object contains the user name and the password. The user is then saved. This information will be used when logging in to the user's account

Next is the credentials class where the same happens in terms of instance of the credential where all the data about the credential is taken in such as: 
- The name of the account
- The username used in the account
- The email used to login to the account
- The password of the account

This data is passed onto an array and is saved there. The user can add as many credentials as needed and when they need to see them they can choose to view all their credentials at once or search for a specific credential and view only its own data.

## Future Improvements
In the future I intend to make the app have a single permanent storage for its data and that it does not loose all data once a user logs out of the application.

## Contact Information
In case of any queries or suggestions, you can reach me through the following handles:
1. Phone: 0710029966
2. Git-hub: Maina francis
3. Twitter: @youngkendrick
4. LinkedIn: Francis Maina
5. email: mainaf471@gmail.com

## Licence Information
MIT License

Copyright (c) [2022] [Francis Mwangi Maina]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
