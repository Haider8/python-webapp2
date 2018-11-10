# html_escaping.py

# User Instructions
# 
# Implement the function escape_html(s), which replaces
# all instances of:
# > with &gt;  #*************notice the commas**************
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically 
# render your escaped text as the corresponding symbols, 
# but the grading script will still correctly evaluate it.
# 

def escape_html(s):
    
    s = s.replace('&', '&amp;')
    s = s.replace('>', '&gt;')
    s = s.replace('<', '&lt;')
    s = s.replace('"', '&quot;')
    return s

# you can also use the inbuilt python function
# by importing the cgi module    
# cgi.escape(s, quote = True)  --> quote = True to escape quotes also
# it is always safer to use the builtin functions
# rather then making up your own functions
    
    

#print escape_html('>')             # when you write > , in the form field of html it should go as &gt;                       
#print escape_html('<')             # which is called escaping, browser will show it as >
#print escape_html('"')             # in the rendered html
#print escape_html("&")
#print escape_html('"hello, & = &amp;"')