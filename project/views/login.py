### REF: IFQ582-5.8
### import blueprint / route template
from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from hashlib import sha256
from flask_login import login_user, current_user
from project.forms import LoginForm
from project.db.setup import mysql
from project.db.user import check_for_user, add_public_user, add_library_staff
from project.models.user import User

bp = Blueprint('login', __name__)


@bp.route('/login/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM user WHERE email = %s", (form.email.data,))
         row = cur.fetchone()
         cur.close()


             # Get hashed form of the submitted password
        assert form.password.data
        form.password.data = sha256(form.password.data.encode()).hexdigest()
             # Compare with our database data
        user = check_for_user(form.email.data, form.password.data)
        if not user:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login.login'))



             # Store full user info in session

             # TODO: store is_admin, is_elder, is_staff in the session
            # For use by route decorator functions

        session['user'] = {
                 'firstname': user.first_name,
                 'surname': user.last_name,
                 'email': user.email,
                 'phone': user.phone,
             }
        session['logged_in'] = True
        flash('Login successful!')
        return redirect(url_for('main.index'))

    return render_template('login.html', form=form)


#@bp.route("/login", methods=['GET', 'POST'])
#def login():
#    if current_user.is_authenticated:
#        return redirect(url_for('main.home'))   
#    form = LoginForm()
#    if form.validate_on_submit():
#        cur = mysql.connection.cursor()
#        cur.execute("SELECT * FROM user WHERE email = %s", (form.email.data,))
#        row = cur.fetchone()
#        cur.close()

#        if row:
#           if row['password'] == hashed_input:
#                user = User(**row)
#                login_user(user, remember=form.remember.data)
#               flash('You have been logged in!', 'success')
#                next_page = request.args.get('next')
#                return redirect(next_page) if next_page else redirect(url_for('main.home'))
#        else:
#            flash('Login Unsuccessful. Please check email and password', 'danger')
#    return render_template('login.html', title='Login', form=form)