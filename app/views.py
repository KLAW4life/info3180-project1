"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from app.forms import PropertyForm
from app.models import PropertyPortfolio


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Kerene Wright")

@app.route('/property/create', methods=['POST','GET'])
def property():
    
    form = PropertyForm()
    if form.validate_on_submit():
        photo = form.photo.data
        title = form.title.data
        description = form.description.data
        bedroom = form.bedroom.data
        bathroom = form.bathroom.data
        price = form.price.data
        type = form.type.data
        location = form.location.data

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_property = PropertyPortfolio(title, description, bedroom, bathroom, price, type, location, filename) 
        db.session.add(new_property)
        db.session.commit()    
        flash('Property Information Successfully Added!', 'success')
        return redirect(url_for('properties'))
    
    flash_errors(form)
    return render_template('new_property.html', form=form)

@app.route('/properties')
def properties():
    property = PropertyPortfolio.query.all()
    return render_template('properties.html', property=property)

@app.route('/property/<property_id>')
def view_property(property_id):
    this_property = PropertyPortfolio.query.filter_by(id=property_id).first()
    return render_template('specific_property.html', property=this_property)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
