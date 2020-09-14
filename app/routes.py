from flask import render_template, request, redirect, url_for, jsonify
from app import app, models, db

Destination = models.Destination

# Count the number of countries in the destination list
def count_countries(destinations):
    count = 0
    countries = []
    for destination in destinations:
        if destination.country not in countries:
            count += 1
            countries.append(destination.country)
    return count

# Get all destinations that have not been visited yet
def get_future(destinations):
    future = []
    for destination in destinations:
        if destination.visited == False:
            future.append(destination)
    return future

# Get the first of the future destinations
def get_next_destination(destinations):
    for destination in destinations:
        if destination.visited == False:
            return destination
    return None

# HOME PAGE
@app.route('/')
def index():
    title = 'Home'
    destinations = Destination.query.all()
    if len(destinations) >= 3:
        recent_destinations = destinations[-3:]
    else:
        recent_destinations = destinations
    next_destination = get_next_destination(destinations)
    return render_template("index.html", background_image='background_1.jpg', heading='Plan Your Travel', 
                            description='Hold memories of places you have been, are and will be to', 
                            main_button='/destination/', main_button_name='All Destinations',
                            title=title, recent_destinations=recent_destinations, next_destination=next_destination,
                            no_countries=count_countries(destinations), no_destinations=len(destinations))

# GET / ADD NEW DESTINATIONS
@app.route('/destination/', methods=['GET'])
def view_destinations():
    if (request.method == "GET"):
        destinations = Destination.query.all()
        destinations = destinations[::-1]
        return render_template('destinations.html', background_image='background_3.jpg', heading='Destinations',
                                description='All your travel history and future plans', title='Destinations', 
                                main_button_name='Add Destination', destinations=destinations)

# GET detail of a destination
@app.route('/destination/<int:id>', methods=['GET'])
def view_details(id):
    if request.method == "GET":
        destination = Destination.query.filter_by(id=id).first()
        description = destination.get_date() + ', ' + destination.country
        if destination.image_names != '':
            background_image = destination.image_names.split()[0]
        else:
            background_image = 'hero_1.jpg'
        return render_template('view_destination.html', background_image=background_image, heading=destination.name, 
                            description=description, main_button_name='Edit Destination', 
                            title=destination.name, destination=destination)

# GET / CREATE a new destination
@app.route('/plan/', methods=['GET', 'POST'])
def view_plan():
    if request.method == "GET":
        destinations = Destination.query.all()
        return render_template("plan.html", background_image='background_2.jpg', heading='Edit Your List', 
                                description='Add, remove and edit your destination list', 
                                main_button_name='Add Destination', 
                                title='Plan', destinations=destinations)
    elif request.method == "POST":
        # Get data from form fields
        name = request.form.get('name')
        country = request.form.get('country')
        date = request.form.get('date')
        month = request.form.get('month')
        year = request.form.get('year')
        caption = request.form.get('caption')
        
        # Create a new Destination item from the given data
        new_item = Destination(name=name, caption=caption, image_names='background_4.jpg', 
                                date=date, month=month, year=year, country=country)
        
        # Add and commit the changes to the database
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('view_destinations'))

# EDIT / DELETE a destination
@app.route('/plan/<int:id>', methods=['DELETE', 'POST'])
def edit_destination(id):
    if request.method == "DELETE":
        destination = Destination.query.filter_by(id=id).first()
        
        # Check if Destination exists
        if destination != None:
            msg = {
                'message': 'Delete successful'
            }
            db.session.delete(destination)
            db.session.commit()
            return jsonify(msg), 200
        
        # If it does not exist
        msg = {
            'message': 'Destination not found'
        }
        return jsonify(msg), 204
    elif request.method == "POST":
        # Get data from form fields
        name = request.form.get('name')
        country = request.form.get('country')
        date = request.form.get('date')
        month = request.form.get('month')
        year = request.form.get('year')
        caption = request.form.get('caption')

        destination = Destination.query.filter_by(id=id).first()
        if (destination != None):
            # Update the destination with given data
            destination.name = name
            destination.country = country
            destination.date = date
            destination.month = month
            destination.year = year
            destination.caption = caption

            # Update the change to database
            db.session.add(destination)
            db.session.commit()
        return redirect(url_for('view_details', id=id))