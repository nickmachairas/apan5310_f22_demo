from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewCaseForm(FlaskForm):
    investigation_title = StringField('Case Title', validators=[DataRequired()])
    ad_investigation_number = StringField('AD Investigation Numbers 731-TA-')
    ad_country = StringField('AD Investigation Countries')
    cvd_investigation_number = StringField('CVD Investigation Numbers 701-TA-')
    cvd_country = StringField('CVD Investigation Countries')
    commodity_code = StringField('Scope HTS (0000.00.00.00)')
    petitioner_firm_name = StringField('Petitioner Companies or Coalition Name')
    law_firm_name = StringField('Petitioner Law Firm')
    law_firm_lead = StringField('Petitioner Lead Counsel')
    submit = SubmitField('Submit')
