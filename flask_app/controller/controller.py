from flask_app import app
from flask import render_template, redirect,request, session, flash
from flask_app.models.models import Email




@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create', methods=['POST'])
def create():
    is_valid = Email.validator(request.form)
    if not is_valid:
        return redirect ('/')

    # if not Email.validate_email(request.form):
    #     return redirect('/')
    email = request.form["email"]
    flash(f"The email address you entered {email} is a VALID email address! Thank you!")
    Email.create(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    emails = Email.get_all()
    return render_template('success.html', emails = emails)

@app.route('/delete/<int:id>')
def delete(id):
    Email.delete({'id':id})
    return redirect('/success')