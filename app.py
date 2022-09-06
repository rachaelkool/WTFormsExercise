from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "jenkinz21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def show_pets():
    """View a list of all pets."""
    pets = Pet.query.all()
    return render_template('all_pets.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Create a new pet."""
    form = AddPetForm()

    if form.validate_on_submit():
        name=form.name.data
        species=form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data
        available=form.available.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')

    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Edit an existing pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')

    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)



        
   
        