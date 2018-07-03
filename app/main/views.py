# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # categories = Category.get_categories(id)
    categories = Category.query.all()

    title = 'Home'

    return render_template('index.html', title = title, categories = categories )
   
@main.route('/sign/', methods=['GET','POST'])
def sign():
    form = SignForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User(username = username , password = password)
        return redirect(url_for('.sign'))
    return render_template('sign.html', sign_form=form )