### REF: IFQ582-5.8
### import blueprint / route template
from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from hashlib import sha256
from ..forms import RegisterForm, LoginForm
from ..db.user import check_for_user, add_user

bp = Blueprint('auth', __name__)


@bp.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Hash the password
            assert form.password.data
            form.password.data = sha256(form.password.data.encode()).hexdigest()
            # Check if the user already exists
            user = check_for_user(form.email.data, form.password.data)
            if user:
                flash('User already exists', 'error')
                return redirect(url_for('main.register'))
            # User does not exist; create them
            add_user(form)
            flash('Registration successful!')
            return redirect(url_for('main.login'))

    return render_template('register.html', form=form)


@bp.route('/login/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Get hashed form of the submitted password
            assert form.password.data
            form.password.data = sha256(form.password.data.encode()).hexdigest()
            # Compare with our database data
            user = check_for_user(form.email.data, form.password.data)
            if not user:
                flash('Invalid username or password', 'error')
                return redirect(url_for('main.login'))

            # Store full user info in session
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