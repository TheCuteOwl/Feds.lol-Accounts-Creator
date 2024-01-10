import requests
import json
import random
import string
from urllib.parse import urlparse, urlunparse

num = int(input('How many account you want to generate -> '))

def generate_random_number_string():
    random_number = random.randint(1, 20)
    return str(random_number)
for x in range(num):
    used_numbers = set()
    url_update_social = "https://feds.lol/api/biolink/manage/socials/create"
    url_register = "https://feds.lol/api/auth/register"
    url_update_pfp = "https://feds.lol/api/biolink/manage/media/profilepicture"
    url_update_bio = "https://feds.lol/api/biolink/manage/media/bio"
    url_update_background = "https://feds.lol/api/biolink/manage/media/background"
    url_update_name = "https://feds.lol/api/biolink/manage/media/name"
    url_update_discord = "https://feds.lol/api/biolink/manage/media/discord"

    def generate_random_string(length):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for i in range(length))

    def generate_random_email():
        return f"{generate_random_string(8)}@{generate_random_string(10)}.bzt"

    def image(formatx,formaty):
        base_url = f"https://picsum.photos/{formatx}/{formaty}"
        response = requests.get(base_url)
        
        final_url = response.url
        return final_url

    def generate_random_payload():
        random_user_api_url = "https://randomuser.me/api/"
        
        response = requests.get(random_user_api_url)
        if response.status_code == 200:
            data = response.json()
            user_info = data["results"][0]
            
            return {
                "email": generate_random_email(),  
                "username": user_info["login"]["username"],
                "password": generate_random_string(10),
                "link": generate_random_string(15),
            }
        else:
            print(f"Failed to fetch data from {random_user_api_url}")
            return None

    with open("config.json", "r") as config_file:
        config_data = json.load(config_file)

    def save_to_file(filename, data, mode='a'):

        with open(filename, mode) as file:
            file.write(data + '\n')

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr-FR,fr;q=0.9",
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "Origin": "https://feds.lol",
        "Pragma": "no-cache",
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }

    print("Registering the account")
    payload_register = generate_random_payload()
    response_register = requests.post(url_register, json=payload_register, headers=headers)

    print("Account Registered:", response_register.status_code)

    if response_register.status_code == 200:
        generated_token = response_register.cookies.get("token")
        headers["Cookie"] = f"token={generated_token}"
        
        if config_data["profile_picture_url"] == 'random':
            pfp = image('500','500')
            payload_update_pfp = {"pfp": pfp}
        else:
            payload_update_pfp = {"pfp": config_data["profile_picture_url"]}
            
        response_update_pfp = requests.post(url_update_pfp, json=payload_update_pfp, headers=headers)
        
        print("Adding profile picture!")

        
        
        payload_update_bio = {"bio": config_data["bio_content"]}
        response_update_bio = requests.post(url_update_bio, json=payload_update_bio, headers=headers)
        
        print("Adding Custom Bio")

        
        if config_data["background_url"] == 'random':
            pfp = image('1920','1080')
            payload_update_background = {"bg": pfp}
        else:
            payload_update_background = {"bg": config_data["background_url"]}
            
        print('Background Added! ')
            
            
        response_update_background = requests.post(url_update_background, json=payload_update_background, headers=headers)
        
        print('Background Added! ')


        payload_update_name = {"name": payload_register['username']}
        response_update_name = requests.post(url_update_name, json=payload_update_name, headers=headers)
        
        print('Custom Username added!')
        
        how_many_fake_websites = config_data.get("how_many_fake_website", 1)

        if str(how_many_fake_websites).lower() == 'random':
            how_many_fake_websites = random.randint(1, 15)
        else:
            how_many_fake_websites = int(how_many_fake_websites)

        used_numbers = set()

        for _ in range(how_many_fake_websites):
            if config_data["website_id"] == 'random':
                new_number = generate_random_number_string()
                while new_number in used_numbers:
                    new_number = generate_random_number_string()
                used_numbers.add(new_number)
                
                payload_update_social = {"site": new_number}
            else:
                payload_update_social = {"site": config_data["website_id"]}

            if config_data["website_username"] == 'random':
                payload_update_social["link"] = payload_register['username']
            else:
                payload_update_social["link"] = config_data["website_username"]

            print("Added a connection!")
            response_update_name = requests.post(url_update_social, json=payload_update_social, headers=headers)


        print(f"{how_many_fake_websites} connections added!")
        
        
        if 'discord_id' in config_data and config_data['discord_id']:
            payload_update_discord = {"discordId":config_data['discord_id']}
            response_update_name = requests.post(url_update_discord, json=payload_update_discord, headers=headers)
            print('Added Discord')
        else:
            pass

            
        save_to_file("generated.txt", f"{{'email': '{payload_register['email']}', 'username': '{payload_register['username']}',  'password': '{payload_register['password']}', 'link': '{payload_register['link']}', 'token': '{generated_token}'}}")
        
        print("Account fully changed!")
        
        
    else:
        print("Registration failed.")
