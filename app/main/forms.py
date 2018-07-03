class SignForm(FlaskForm):

    username = StringField('username',validators=[Required()])
    password = StringField('password', validators=[Required()])
    submit = SubmitField("submit")