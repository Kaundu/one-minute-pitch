class SignForm(FlaskForm):

    username = StringField('username',validators=[Required()])
    password = StringField('password', validators=[Required()])
    submit = SubmitField("submit")    submit = SubmitField("submit")

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    """
    class to create a form to create category
    """
    category_name = StringField('Pitch Category',validators=[Required()])
    submit = SubmitField('Create')
