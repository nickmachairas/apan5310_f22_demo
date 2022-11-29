from flask import render_template

from app import app, db
from app.forms import NewCaseForm
from app.models import LawFirms


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/newcase', methods=['GET', 'POST'])
def newcase():
    form = NewCaseForm()
    if form.validate_on_submit():
        law_firm_name = form.law_firm_name.data
        law_firm_lead = form.law_firm_lead.data
        new_law_firm = LawFirms(firm_name=law_firm_name, lead=law_firm_lead)
        db.session.add(new_law_firm)
        db.session.commit()
    return render_template("newcase.html", form=form)

@app.route('/lawfirms', methods=['GET', 'POST'])
def lawfirms():
    law_firms = LawFirms.query.all()
    return render_template("lawfirms.html", law_firms=law_firms)
