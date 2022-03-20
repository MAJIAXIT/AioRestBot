import requests
import json
import SwitchDto

switchTypeDict = {
    "clicky": "1",
    "linear": "2",
    "tactile": "3",
}


def GetAll():
    """Get all switches from server"""
    answer = ""
    try:
        jsonData = (requests.get(
            "http://194.67.119.148:8080/switches/getAll")).json()
        if jsonData:
            for switch in jsonData["switchesList"]:
                answer += "Id: " + str(switch["id"]) + "\n"
                answer += "Name: " + switch["name"] + "\n"
                answer += "Price: " + str(switch["price"]) + "\n"
                answer += "Colour: " + switch["colour"] + "\n"
                answer += "Switch Type: " + switch["switchType"] + "\n" + "\n"
    except:
        answer = "Somethings wrong"
    finally:
        return answer


def GetById(switchId):
    """Get switch by id from server"""
    answer = ""

    try:
        request = requests.get(
            "http://194.67.119.148:8080/switches/getById/" + str(switchId))
        if request:
            jsonData = request.json()

            answer += "Id: " + str(jsonData["id"]) + "\n"
            answer += "Name: " + jsonData["name"] + "\n"
            answer += "Price: " + str(jsonData["price"]) + "\n"
            answer += "Colour: " + jsonData["colour"] + "\n"
            answer += "Switch Type: " + jsonData["switchType"]

        else:
            answer = "There is no switch with id: " + switchId
    except:
        answer = "Something is wrong"
    finally:
        return answer


def DeleteById(switchId):
    """Delete by id from server"""
    try:
        request = requests.delete(
            "http://194.67.119.148:8080/switches/deleteById/" + str(switchId))
        if request:
            answer = "Switch with id: " + switchId + " deleted successfully"
        else:
            answer = "There is no switch with id: " + switchId
    except:
        answer = "Something is wrong"
    finally:
        return answer


def InsertOne(switchName, switchPrice, switchColour, switchTypeId):
    """Insert new switch to server"""
    switch = SwitchDto.Switch(switchName, switchPrice,
                              switchColour, switchTypeId)

    try:
        response = requests.post(
            "http://194.67.119.148:8080/switches/insertOne", json=switch.__dict__)
        if response:
            answer = "Insert success!"
    except:
        answer = "Something is wrong!"
    finally:
        return answer


def UpdateById(switchId, switchName, switchPrice, switchColour, switchTypeId):
    """Update switch on server by id"""

    try:
        request = requests.get(
            "http://194.67.119.148:8080/switches/getById/" + str(switchId))
        if request:
            pass
        else:
            return "There is no switch with id: " + switchId
    except:
        return "Something is wrong"

    switch = SwitchDto.Switch(switchName, switchPrice,
                              switchColour, switchTypeId)

    try:
        response = requests.post(
            "http://194.67.119.148:8080/switches/updateById/" + str(switchId), json=switch.__dict__)
        if response:
            answer = "Update success!"
    except:
        answer = "Something is wrong!"
    finally:
        return answer
