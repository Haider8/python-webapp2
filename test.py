import webapp2
import month
import day
import year
import html_escaping
import make_rot

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

        

app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler), ('/unit2/rot13', Rot13)],
                              debug=True)