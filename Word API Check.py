import requests
from wordsegment import load, segment
load()
import time

""" 
Billy Knight - March 2022 

This module will split a one word input from a user, 
and check to see if all works can be segmented into 
a word dictionary. 

1. A check will be made for an internet connection. 
2. All words will be checked using an online word API.

THIS MODULE IS NOT VIABLE AS RESULTS WILL VARY.

e.g. 'applepie' will be segmented into ['apple']['pie']
     whereas 'keyring' will not be segmented ['keyring'].
     
A minimum of two valid words must be returned for the result to be correct.
"""
def main():

    try:
        # Define some variables first.
        check_internet = "Checking Internet Connection...\n"
        user_input = ""
        word = ""
        dict_returned = False
        url = ""
        output = ""
        verdict = ""
        reply = {}

        def connected_to_the_internet():
            try:  # See if we are connected to the internet.
                url = "https://www.google.co.uk"
                print(check_internet)
                timeout = 5
                time.sleep(3)
                request = requests.get(url, timeout=timeout)
                return True  # Connected to the Internet
            except (requests.ConnectionError, requests.Timeout) as exception:
                return False  # No Internet Connection.
            finally:
                pass
        try:
            if connected_to_the_internet():  # We can use the online word API.

                # Get the user input.
                user_input = input("Please Key In A Word To Check: ")

                # Break up the user input into segments (if possible).
                word_list = segment(user_input)

                # Loop through each segment and run it through the word API.
                for word in word_list:

                    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
                    response = requests.get(url)
                    reply = response.json()

                    """ 
                    Type(reply) Returned: 
                    'list' = word exists with definition. 
                    'dict' = word was not found with a definition. 
                    """
                    if type(reply) is dict: dict_returned = True

                # Deliberate the verdict.
                if len(word_list) > 1: # Word can possibly be segmented.
                    if dict_returned:
                        verdict = f"\'{user_input}\' cannot be segmented into a word dictionary. {word_list}"
                    else:
                        verdict = f"\'{user_input}\' can be segmented into a word dictionary. {word_list}"
                else: # Word cannot be segmented.
                    verdict = f"\'{user_input}\' cannot be segmented into a word dictionary. {word_list}"

                print(verdict)

            else:
                print("You Are Not Connected To The Internet.\n"
                      "Unable To Access The Online Word API.\n"
                      "Please Check Your Internet Connection And Try Again.")

        except Exception as e:
            print(e)

        finally:
            pass

    except Exception as e:
        print(e)

    finally:
        pass

if __name__=='__main__': main()
