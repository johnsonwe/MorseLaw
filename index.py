from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from main import search, convertToMorseCode

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'stuff'


class UrlLink(FlaskForm):
    searchbox = StringField("Search Term:", validators=[DataRequired()])
    submit = SubmitField('Search')


@app.route('/', methods=['GET', 'POST'])
def divide():
    form = UrlLink()
    morseCode = None
    if form.validate_on_submit():
        text = form.searchbox.data
        law = search(text)
        morseCode = convertToMorseCode(law)
    return render_template('index.html', form=form, morsecode=morseCode)


if __name__ == '__main__':
    app.run()
