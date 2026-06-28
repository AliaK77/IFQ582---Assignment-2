### import flask and template for error handling
from flask import Flask,  render_template, Blueprint, request
from ..db.connection import cursor, connection

bp = Blueprint('scratch', __name__)

### scratch testing page
### @app.route('/scratch')
@bp.route('/scratch')
def scratch():
    cur = cursor() ### open a cursor to the db
    ###cur.execute("SELECT * FROM collection_items") ### run the query
    cur.execute("SELECT title FROM collection_items") ### run the query
    results = cur.fetchall() ### get all query results
    cur.close() ### close the cursor
    #return render_template('scratch.html', scratch=results) ### pass the data to the template to display
    return str(results) ### return the results as a string to the browser for initial testing -- worked OK
