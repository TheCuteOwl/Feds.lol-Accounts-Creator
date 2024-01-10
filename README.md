
## Feds.lol Account Generator

Don't forget to star if you like this project !

This Python script is designed to automate the account generation process on the Feds.lol platform. It leverages the Feds.lol API to register accounts, update profile details, and establish connections. Below are the key features and functionalities of this account generator

Why did I want to make that :

I saw this repository from imvast and saw "Feds.lol is better" so I tried to bot this website and well, it is trash too, no protection at all

Features:

```
Dynamic Account Generation:

The script prompts the user to input the number of accounts to generate.
Utilizes the RandomUser.me API to obtain random user data for account creation.
Profile Customization:

Allows customization of profile details such as profile picture, bio content, and background image. 
Supports both random and predefined values for profile customization.
Connection Establishment:

Establishes connections to fake websites as specified in the configuration.
The number of connections can be set randomly or predefined in the configuration.
Discord Integration:

Optionally adds Discord information to the generated accounts.

The Discord ID can be configured in the config.json file.

```

Configuration File:

Utilizes a config.json file for easy customization.
Users can tailor various parameters like profile picture URLs, bio content, and more.
Usage:
Clone the Repository:

```
git clone https://github.com/TheCuteOwl/Feds.lol-Accounts-Creator.git
cd Feds.lol-Accounts-Creator-main
```
Install Dependencies:

```
pip install -r requirements.txt
```
Run the Script:

```
python account_generator.py
```
Follow the prompts to specify the number of accounts to generate.

Configuration:

```
Modify the config.json file to customize the account generation process. Tailor profile picture URLs, bio content, background URLs, and more to suit your preferences.
```

Dependencies:
```
Requests
```
License:
This project is licensed under the MIT License.

Contributions:
Contributions are welcome! Fork the repository and create a pull request with your improvements.

Author:
TheCuteOwl
