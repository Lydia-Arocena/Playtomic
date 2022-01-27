import pandas as pd
from config import matches_list
from folium import Map, Icon, Marker

def get_infoclub(matches_list):
    """
    This function transform a json into a df.
    Args: matches_list (list)
    Return: df.
    """

    dicc={"club_id":[], "club_name":[],"city":[],"Latitud":[], "Longitud":[]}
    for i in range (len(matches_list)):
        dicc['club_id'].append(matches_list[i]['club_info'][0]['club_id']) 
        dicc['club_name'].append(matches_list[i]['club_info'][0]['club_name']) 
        dicc['city'].append(matches_list[i]['club_info'][0]['city']) 
        dicc['Latitud'].append(matches_list[i]['club_info'][0]['coordinate_geo']['coordinates'][1]) #lat
        dicc['Longitud'].append(matches_list[i]['club_info'][0]['coordinate_geo']['coordinates'][0]) #lng
    clubs_info=pd.DataFrame(dicc)
    
    return clubs_info


def map(matches_list):
    """
    This functions return a map with all clubs.
    Args: matches_list (list)
    Return: Folium map.
    """
    clubs= get_infoclub(matches_list)
    clubs_info= clubs.drop_duplicates()
    
    map_club = Map(location = [40.4994927, -3.7131068], zoom_start = 2)
    for i,row in clubs_info.iterrows():
        dicc = {"location": [row["Latitud"], row["Longitud"]], "tooltip": row["club_name"]}
        
        if row["city"] == 'Madrid':
            icono = Icon(color = "green",
                        prefix="fa",
                        icon="star",
                        icon_color="black"
            )
        elif row["city"] != 'Madrid':
            icono = Icon(color = "orange",
                        prefix="fa",
                        icon="star",
                        icon_color="black")
            
            
        mark = Marker(**dicc, icon=icono)
        mark.add_to(map_club)
            
    return map_club


def get_users(matches_list):
    """
    This function transform a json into a df.
    Args: matches_list (list)
    Return: df.
    """

    dicc={"user_id":[], "registration_date":[],"price":[], "currency":[]}
    for i in range (len(matches_list)):
        dicc['user_id'].append(matches_list[i]["registered_users"][0]['user_id']) 
        dicc['registration_date'].append(matches_list[i]["registered_users"][0]['registration_date']) 
        dicc['price'].append(matches_list[i]["registered_users"][0]['price']["amount"]) 
        dicc['currency'].append(matches_list[i]["registered_users"][0]['price']["currency"])
    users=pd.DataFrame(dicc)
    
    return users