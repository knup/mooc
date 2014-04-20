def remove_html_markup(s): 
	tag = False
	quote = False
	out = ""

	for c in s:
		#assert not tag
		#print 'c = %c, tag = %r, quote = %r' % (c, tag, quote)  
		if c == '<' and not quote:
			tag = True
		elif c == '>' and not quote:
			tag = False
		elif (c == '"' or c == "'") and tag:
			#or has a lower precedence than and
			#assert False
			quote = not quote 
		elif not tag:
			out = out + c
	return out

print remove_html_markup('<b>foo</b>') 
print remove_html_markup('<em>foo</em>') 
print remove_html_markup('<a href="foo.html">foo</a>') 
print remove_html_markup('<a href="">foo</a>') 
print remove_html_markup('<a href=">">foo</a>')
print remove_html_markup('<b>"foo"</b>')
print remove_html_markup('"<b>foo</b>"')
print remove_html_markup('<"b">foo</"b">') 
print remove_html_markup("'foo'") 
print remove_html_markup('"foo"') 
