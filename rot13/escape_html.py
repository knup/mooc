def escape_html(s):
	for (i,o) in (("&","&amp;"),
                 ("<","&lt;"), 
                 ('"',"&quote;"),
                 (">","&gt;")):
		s = s.replace(i,o)   
	return s

print escape_html('>')
