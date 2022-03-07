import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        res= requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(res)
        data={
            '[IP]':res.get('query'),
            '[Int prov]':res.get('isp'),
            '[Org]':res.get('org'),
            '[Country]':res.get('country'),
            '[Region number]':res.get('region'),
            '[Region Name]':res.get('regionName'),
            '[City]':res.get('city'),
            '[ZIP]':res.get('zip'),
            '[Lat]':res.get('lat'),
            '[Lon]':res.get('lon'),
        }

        for k,v in data.items():
            print(f'{k} : {v}')

        area=folium.Map(location=[res.get('lat'),res.get('lon')]) 
        area.save=(f'{res.get("query")}_{res.get("city")}.html' ) 
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    preview_text= Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip=input('Please enter a target IP: ')
    get_info_by_ip(ip=ip)

if __name__ =='__main__':
   main() 
