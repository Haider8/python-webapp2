import webapp2
import month
import day
import year
import html_escaping
import make_rot
import signup_valid
import jinja2
import os


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

form = """
<form method="post">
    What is your birthday?

    <br>

    <label> Month
        <input type="text" name="month" value="%(month)s">
    </label>
    
    <label> Day    
        <input type="text" name="day" value="%(day)s">
    </label>
    
    <label> Year    
        <input type="text" name="year" value="%(year)s">
    </label>    
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>    
"""

rot = """
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text" value="" style="height: 100px; width: 400px;">%(text)s</textarea>     
      <br>
      <input type="submit">
    </form>
  </body>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {'error': error,
                                        'month': html_escaping.escape_html(month),
                                        'day': html_escaping.escape_html(day),
                                        'year': html_escaping.escape_html(year)})

    def get(self):
        #self.response.headers['Content-type'] = 'text/plain'
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month_valid = month.valid_month(user_month)
        day_valid = day.valid_day(user_day)
        year_valid = year.valid_year(user_year)

        if not (month_valid and day_valid and year_valid):
            self.write_form("That doesn't look valid to me, friend.",
                            user_month, user_day, user_year)
        else:
            self.redirect("/thanks") 


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks, that's a totally valid day!")

class Rot13(webapp2.RequestHandler):
    def write_rot(self, text=""):
        self.response.out.write(rot % {'text': text})

    def get(self):
        self.write_rot()

    def post(self):
        text = self.request.get('text')
        rot13_text = make_rot.rot_func(text)
        escape_rot13_text = html_escaping.escape_html(rot13_text)
        self.write_rot(escape_rot13_text)


class UserRegister(BaseHandler):
    def get(self):
        self.render("signup.html")

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username=username,
                      email=email)

        if not signup_valid.valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        elif not signup_valid.valid_password(password, verify):
            if len(password) < 3:
                params['error_password'] = "That wasn't a valid password."
            else:
                params['error_verify'] = "Your passwords didn't match."
            have_error = True

        elif not signup_valid.valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.render('signup.html', **params)
        else:
            self.redirect('/unit2/welcome?username=' + username)


class Welcome(BaseHandler):
    def get(self):
        username = self.request.get('username')
        if signup_valid.valid_username(username):
            self.render('welcome-page.html', username=username)
        else:
            self.redirect('/unit2/signup')


app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler), ('/unit2/rot13', Rot13), 
                                ('/unit2/signup', UserRegister), ('/unit2/welcome', Welcome)], debug=True)
                          
                              