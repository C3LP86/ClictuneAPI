import json
import requests
import argparse

PARSER = argparse.ArgumentParser(description='Add and detele URL in CLictune Account')

PARSER.add_argument("-add", "--addURL", action="store_true", help="Add URL in Clictune Account")
PARSER.add_argument("-del", "--deleteURL", action="store_true", help="Delete URL in Clictune Account")

ARGS = PARSER.parse_args()

DATA_LIST = []
USER_ID = "USERID"
API_KEY = "API KEY"

if hasattr(ARGS, 'help'):
    PARSER.print_help()
    exit()

if ARGS.addURL:
    with open("URL_AddLinks.txt", 'r') as URL:
        with open("Name_AddLinks.txt", 'r') as NAME:
            URL_FILE = URL.readlines()
            NAME_FILE = NAME.readlines()
            
            for i in range(len(URL_FILE)):
                url = "https://www.clictune.com/Links_api/create_link?user_id={}&api_key={}&url={}&name={}".format(USER_ID, API_KEY, URL_FILE[i].strip(), NAME_FILE[i].strip())

                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    extract_data = data.get("shortenedUrl")
                    DATA_LIST.append(
                        {
                            "url": extract_data,
                            "name": NAME_FILE[i]
                        }
                    )
            
                else:
                    raise ValueError(f"echec & mat : status code --> {response.status_code}")
            
            for data_entry in DATA_LIST:
                print("")
                print(f"URL = {data_entry['url']} + Name = {data_entry['name']}")

if ARGS.deleteURL:
    
    with open('DeleteLinks.txt', 'r') as FILE:
        DELETE_URL_FILE = FILE.readlines()
        
        for i in range(len(DELETE_URL_FILE)):
            url = "https://www.clictune.com/Links_api/delete_link?user_id={}&api_key={}&url={}".format(USER_ID, API_KEY, DELETE_URL_FILE[i].strip())

            response = requests.get(url)   

            if response.status_code == 200:
                data = response.json()
                extract_data = data.get("shortenedUrl")
                DATA_LIST.append(
                    {
                        "url": extract_data
                    }
                )
            
            else:
                raise ValueError(f"echec & mat : status code --> {response.status_code}")
            
        for data_entry in DATA_LIST:
            print("")
            print(f"l'URL {data_entry['url']} à bien été delete")