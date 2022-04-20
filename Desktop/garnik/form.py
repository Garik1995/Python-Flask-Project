from wtforms import Form, StringField, validators, IntegerField, PasswordField, SubmitField, RadioField


class Registration(Form):
    name = StringField("Name", [validators.length(min=3, max=10), validators.DataRequired()])

    surname = StringField("Surname", [validators.length(min=3, max=15), validators.DataRequired()])

    gender = RadioField('Gender', [validators.DataRequired()], choices=[('Male', 'Male'), ('Female', 'Female')])

    age = IntegerField("Age", [validators.DataRequired()])

    email = StringField("Email", [validators.length(min=5, max=30), validators.Email(), validators.DataRequired()])

    password = PasswordField("Password",
                             [validators.length(min=5, max=30), validators.DataRequired(),
                              validators.EqualTo("confirm", message="Password must mateh")])
    confirm = PasswordField()
    submit = SubmitField("Registration")


class LoginForm(Form):
    email = StringField("Email", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    login = SubmitField("Login Now")


class ChangePasswordForm(Form):
    oldPassword = PasswordField("Password", [validators.DataRequired()])
    newPassword = PasswordField("Password",
                                [validators.length(min=5, max=30), validators.DataRequired(),
                                 validators.EqualTo("confirm", message="Password must mateh")])
    password = SubmitField("Update Password")
    confirm = PasswordField()


class Update(Form):
    name = StringField("Name", [validators.length(min=3, max=10), validators.DataRequired()])
    surname = StringField("Surname", [validators.length(min=3, max=15), validators.DataRequired()])
    age = IntegerField("Age", [validators.DataRequired()])
    update = SubmitField("Save Changes")
