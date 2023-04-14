from pygle import network

def getCoordinates(bssid):
    """
    Takes a given BSSID and returns the coordinates as a tuple.

    You will have to set up your user and password for WiGLE in the pygle configuration file
    """

    # Formats bssid into AA:AA:AA:AA:AA for WiGLE query
    formatted = "".join(
        [f"{bssid[i:i + 2]}:" for i in range(0, len(bssid), 2)]
    )[:-1]

    print("Searching WiGLE.net:", formatted)

    data = network.search(netid=formatted)

    print(data)
    print()

    try:
        return data['results'][0]['trilat'], data['results'][0]['trilong']
    except:
        print("Invalid BSSID, BSSID not found on WiGLE.net, or too many queries today")




