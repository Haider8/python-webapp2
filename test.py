import webapp2
import month
import day
import year
import html_escaping
import make_rot
import signup_valid

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

signup = """
    <!DOCTYPE html>

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
            %(error_user)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
            %(error_pass)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">
            %(error_verify)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>
          <td class="error">
            %(error_mail)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
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


class UserRegister(webapp2.RequestHandler):
    def write_signup(self, username="", email="", error_user="", error_pass="", error_verify="", error_mail=""):
        self.response.out.write(signup % {'username': html_escaping.escape_html(username),
                                          'email': html_escaping.escape_html(email),
                                          'error_user': error_user,
                                          'error_pass': error_pass,
                                          'error_verify': error_verify,
                                          'error_mail': error_mail})

    def get(self):
        self.write_signup()

    def post(self):
        user = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        username_verify = signup_valid.valid_username(user)
        email_verify = signup_valid.valid_email(email)
        password_verify = signup_valid.valid_password(password, verify)

        if not username_verify:
            if email_verify and password_verify:
                self.write_signup(user, email, "That's not a valid username.")
            elif email_verify and not password_verify:
                if len(password) < 3:
                    self.write_signup(user, email, "That's not a valid username.", "That wasn't a valid password.")
                else:
                    self.write_signup(user, email, "That's not a valid username.", "", "Your passwords didn't match.")
            elif not (email_verify and password_verify):
                if len(password) < 3:
                    self.write_signup(user, email, "That's not a valid username.", "That wasn't a valid password.", "", "That's not a valid email.")
                else:
                    self.write_signup(user, email, "That's not a valid username.", "", "Your passwords didn't match.", "That's not a valid email.")
            elif password_verify and not email_verify:
                self.write_signup(user, email, "That's not a valid username.", "", "", "That's not a valid email.")

        elif username_verify:
            if email_verify and password_verify:
                self.redirect("/unit2/welcome")
            elif email_verify and not password_verify:
                if len(password) < 3:
                    self.write_signup(user, email, "", "That wasn't a valid password.")
                else:
                    self.write_signup(user, email, "", "", "Your passwords didn't match.")
            elif not (email_verify and password_verify):
                if len(password) < 3:
                    self.write_signup(user, email, "", "That wasn't a valid password.", "", "That's not a valid email.")
                else:
                    self.write_signup(user, email, "", "Your passwords didn't match.", "That's not a valid email.")
            else:
                self.write_signup(user, email, "", "", "", "That's not a valid email.")


class Welcome(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Welcome")


                

app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler), ('/unit2/rot13', Rot13), 
                                ('/unit2/signup', UserRegister), ('/unit2/welcome', Welcome)], debug=True)
                          
                              