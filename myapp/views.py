from django.shortcuts import render
from django.http.response import HttpResponse
import requests
from bs4 import BeautifulSoup
 
def index_template(request):
    recipeList = []
    # for i in range(1, 10):
    #     recipeList = []
    #     # url = f"https://cookpad.com/recipe/72622{i}"
        
        
    #     page = requests.get(url)
        
    #     soup = BeautifulSoup(page.content, "html.parser")
    #     title=soup.select("h1.recipe-title")
    #     if(title):
    #         print(title[0].text)
    #         # 'title': title[0].text
    #     for i in soup.find_all("span", class_="name"):
    #         recipeList.append(i.text)
    #     # 'recipeList': recipeList

    url = f"https://cookpad.com/recipe/726221"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    title=soup.select("h1.recipe-title")[0].text
    for i in soup.find_all("span", class_="name"):
        recipeList.append(i.text) 
    description=soup.select("div.description_text")[0].text
    
    myapp_data = {
    'app': 'Django',
    'num': range(1,10),
    'title': title,
    'recipeList': recipeList,
    'description': description,
    }
    
    
    return render(request, 'index.html', myapp_data)