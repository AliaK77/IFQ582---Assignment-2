### import flask and blueprint / route template
from flask import Blueprint, render_template, flash, request, url_for, redirect, app
from flask_login import current_user
from wtforms import form
from project.db.admin_db import get_collection_items, get_user_role
from project.forms import UpdateItemForm, UpdateRoleForm
from project.models.user import User
from ..db.setup import mysql
from ..wrappers import only_admins

bp = Blueprint('admin', __name__)

#Route for the admin page
@bp.route('/admin', methods=['GET', 'POST'])
#@only_admins
def admin_dashboard():
    form = UpdateItemForm()
    db_items = get_collection_items()
    db_users = get_user_role()
    return render_template('admin.html', title='Admin', form=form, users=db_users, items=db_items)

@bp.route('/admin/add_item', methods=['GET', 'POST'])
def add_item():
    form = UpdateItemForm()
    if form.validate_on_submit():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO collection_items (title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (form.title.data, form.description.data, form.image_link.data.filename if form.image_link.data else None, form.item_category.data, form.cultural_group.data, form.sensitivity_notes.data, form.review_status.data, form.access_level.data))
        mysql.connection.commit()
        cur.close()
        flash('Item added successfully!', 'success')
        return redirect(url_for('admin.admin_dashboard'))
    return render_template('add_item.html', form=form,)


@bp.route('/admin/update_role/<int:user_id>', methods=['POST'])
def update_user_role(user_id):
    new_role = request.form.get('new_role')
    
    if new_role is not None:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE library_staff SET is_admin = %s WHERE user_ID = %s", (new_role, user_id))
        mysql.connection.commit()
        cur.close()
        flash('User role updated successfully!', 'success')
    
    return redirect(url_for('admin.admin_dashboard'))


@bp.route('/admin/manage_item/<int:item_id>', methods=['POST'])
def manage_item(item_id):
    action = request.form.get('action')
    if action == 'delete':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM collection_items WHERE item_id = %s", (item_id,))
        mysql.connection.commit()
        cur.close()
        flash('Item deleted successfully!', 'success')
    elif action == 'update':
        # need to figure this out
        flash('Update functionality not implemented yet.', 'info')
    return redirect(url_for('admin.admin_dashboard'))