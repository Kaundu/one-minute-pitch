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
    return render_template('sign.html', sign_form=form )    return render_template('sign.html', sign_form=form )

@main.route('/register', methods=["GET", "POST"])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
       user = User(email=form.email.data, username=form.username.data, password=form.password.data)
       db.session.add(user)
       db.session.commit()
       return redirect(url_for('auth.login'))
       title = 'New Account'
   return render_template('auth/register.html', registration_form=form)   return render_template('auth/register.html', registration_form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('.profile',uname=uname))
@main.route('/category/<int:id>')
def category(id):
    category = Category.query.get(id)
    pitches = Pitch.query.filter_by(category_id=id)
    
    

    title = f'{category.category_name} page'

    return render_template('category.html',title=title, category=category,pitches=pitches)
@main.route('/category/new', methods = ['GET','POST'])
# @login_required
def new_category():
    form = CategoryForm()
    
    if form.validate_on_submit():
        category_name = form.category_name.data

        # Updated review instance
        new_category = Category(category_name=category_name)

        # save review method
        new_category.save_category()
        return redirect(url_for('.index'))

    # title = 'new category'
    return render_template('new_category.html',category_form=form)
