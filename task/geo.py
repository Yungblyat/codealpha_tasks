import requests
import folium

def get_geolocation(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    data = response.json()
    if data['status'] == 'success':
        return data
    else:
        raise Exception("Unable to fetch geolocation data")

def create_map(latitude, longitude, location_name):
    map_obj = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], popup=location_name).add_to(map_obj)
    return map_obj

def main():
    ip = '1.208.115.255'
    geo_data = get_geolocation(ip)
    
    latitude = geo_data['lat']
    longitude = geo_data['lon']
    location_name = f"{geo_data['city']}, {geo_data['regionName']}, {geo_data['country']}"
    
    map_obj = create_map(latitude, longitude, location_name)
    map_obj.save('E:\\codealpha_tasks\\task\\geolocation_map.html')
    print(f"Map saved as 'geolocation_map.html'")

if __name__ == "__main__":
    main()
