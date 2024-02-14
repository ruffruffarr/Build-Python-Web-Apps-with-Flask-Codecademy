#SET UP THE FLASK APP 
#1 import the Flask class
from flask import Flask

#11 import the helper.py dictionary
from all_animals import pets
#print(pets)

#2 create an instance 
app = Flask(__name__)

#CREATE THE INDEX ROUTE 
#4 use the route decorator to bind the URL path
@app.route('/')
#3 define a function 
def index ():
  #5 add text elements to the page 
  #6 add an unordered list
  #10 add <a> element within each <li> element
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href='/animals/dogs'>Dogs</a></li>
    <li><a href='/animals/cats'>Cats</a></li>
    <li><a href='/animals/rabbits'>Rabbits</a></li>
  </ul>
  '''
#8 use the route decorate to bind it to a URL path
@app.route('/animals/<pet_type>')
#9 update the animals() function to take a parameter

#CREATE THE ANIMALS ROUTE
#7 create individual pages for each animal type
def animals(pet_type):
  html = '<h1>List of {}</h1>'.format(pet_type)
  #12 before return statement, create a for loop. For each element in the list of pets in the pet dictionary, concatenate the string to html 
  html+='<ul>'
  #16 for each index and pet in pets dict of pets type, give a li linking to its individual page
  #enumerate() is needed to give each one an index and str() to turn it into a string type
  for index, pet in enumerate(pets[pet_type]):
    html += f"""<li><a href="/animals/{pet_type}/{str(index)}">{pet["name"]}</a></li>"""
  return html

#CREATE THE PET ROUTE
#13 new function to create indiv pages for each pet
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  #14 
  pet = pets[pet_type][pet_id]
  #15 show pet name
  #17 add img, pet description, pet breed and age
  html = f"""<h1>{pet["name"]}</h1>
              <img src="{pet["url"]}"></img>
              <p>{pet["description"]}</p>
              <ul>
              <li>Breed: {pet["breed"]}</li>
              <li>Age: {pet["age"]}</li>
              <ul>
              """
  return html

  
  
