
from django.shortcuts import render
import urllib.request
import json
from .models import countries_all,provinces
# Create your views here.





def test(request):

    special_c=None
    if request.method =='POST':
        city=request.POST['p'].replace( ' ', '+')
        
        src=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+
                                   city+'&units=metric&appid=6b9e8050535315b284765445681e7864').read()
        l_of_d=json.loads(src)
        
        
        data1={
            "country_code":str(l_of_d['name']),
            "coordinate":str(l_of_d['coord']['lon'])+' ,'+str(l_of_d['coord']['lat']),
            "temp":str(l_of_d['main']['temp'])+' °C ',

        }
        countries=countries_all.objects.all()
    
        special_c=None
        for country in countries:
            if city.lower() == country.name.lower():
                
                special_c=country
                
                break
      
    else:
        special_c=None
        data1={}
    
    

    
    

    m=data1
    context={
        'data':data1,
        'm':m,
        'country_info':special_c
    }
    return render(request,'test.html',context)

def add_prov(request):
   
    url='https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_titlecase.json'
    responce=urllib.request.urlopen(url)
    l_of_d=json.loads(responce.read().decode())
    
    country = countries_all.objects.get(name='United States')

    for state in l_of_d:
        name = state['name']
        
        c = provinces(country_name=country, province_name=name)
        c.save()

    context={}
    return render(request,'home.html',context)

    

 

      
        

    
   