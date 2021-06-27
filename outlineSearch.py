
# -*- coding: utf-8 -*-

"""Search outline knowledge base.
Synopsis:
    filter
    <trigger> [filter]"""

from albert import *
import os
import json
import requests
import time


__title__ = "outline"
__version__ = "0.4.1"
__triggers__ = "ou"
__authors__ = "Jeecabs"
__prettyname__ = "Outline"
__dependencies__ = ["requests"]

iconPath = os.path.dirname(__file__) + "/outline.svg"

configPath = os.path.dirname(__file__) + "/config.json"


def getConfig():
    try:
        with open(configPath) as jsonFile:
            configFile = json.load(jsonFile)
            jsonFile.close()

        endPoint = configFile['endPoint']
        apiKey = configFile['apiKey']

        # This means the user forgot to change the config file value's from the default
        if endPoint == "https://" or apiKey == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX":
            return None, None


        return apiKey, endPoint

    except Exception as e:
        print("Runtime error")
        print(e)
        return None, None


def handleQuery(query):
    results = []

    if query.isTriggered and query.string.strip():

        # avoid rate limiting
        time.sleep(0.15)
        if not query.isValid:
            return

        item = Item(
            id=__prettyname__,
            icon=iconPath,
            completion=query.rawString,
            text=__prettyname__,
            actions=[]
        )

        apiKey, endPoint = getConfig()

        # If getConfig method returns None it can be assumed the config is faulty
        if apiKey == None:
            return Item(
                id=__prettyname__,
                icon=iconPath,
                completion=query.rawString,
                text=__prettyname__,
                actions=[],
                subtext="Incorrect config file"
            )

        if len(query.string) >= 4:

            try:
                api_response = requests.post(endPoint+'/api/documents.search', data=json.dumps({"query": query.string}), headers={"Authorization": f'Bearer {apiKey}',
                                                                                                                                  "Content-Type": "application/json", })
                json_response = json.loads(api_response.content)

                for document in json_response["data"]:
                    results.append(Item(
                        id=__prettyname__,
                        icon=iconPath,
                        text=document["document"]["title"],
                        subtext=document["context"].replace(r"\<\/?b\>/g", ''),
                        actions=[
                            UrlAction("View document", f'{endPoint}{document["document"]["url"]}')]
                    )
                    )

                if len(results) == 0:
                    item.subtext = "No matching documents :("
                    return item

            except Exception as err:
                print(err)
                print("Troubleshoot internet connection")
                item.subtext = "Connection error"
                return item

    return results
