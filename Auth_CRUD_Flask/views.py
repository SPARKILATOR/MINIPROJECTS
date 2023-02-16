from flask import Blueprint,render_template,request,flash,jsonify,redirect
from flask_login import login_required,current_user
from .models import Manage, User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        amount = request.form.get('amount')
        if len(note) < 1:
            flash('Note too short', category='error')
        elif len(amount) < 1:
            flash('Enter Amount', category='error')
        else:
            new_manage = Manage(data=note, amount=amount, user_id = current_user.id)
            db.session.add(new_manage)
            db.session.commit()
            
            flash('Note Added !!' , category='success')
    allNote = Manage.query.all()
    alluser = User.query.all()
    return render_template("home.html", user=current_user, allNote = allNote, alluser = alluser)

@views.route('/delete/<int:id>')
@login_required
def delete(id):
    note = Manage.query.filter_by(id=id).first()
    db.session.delete(note)
    db.session.commit()

    return redirect('/')


'''@views.route('/show')
def show():
    allNote = Manage.query.all()

    return render_template('show_data.html', allNote = allNote)'''

'''@views.route('/delete-note', methods = ['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Manage.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})'''


