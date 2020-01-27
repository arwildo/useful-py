#!/bin/python3
import requests

def internet():

    connection = None

    try:
        r = requests.get("https://google.com")
        r.raise_for_status()
        connection = True

    except:
        connection = False

    finally:
        return connection


print(internet())
