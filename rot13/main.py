#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

form="""
<form method="post">
	<h2>Enter some code to ROT13:</h2>
	<br>
	<textarea type="text" style="height: 100px; width: 400px;" name="text">%(rot13_string)s</textarea>
	<br>
	<input type="submit">
</form>
"""

class Rot13(webapp2.RequestHandler):

	def get(self):
		self.write_form()

	
	def post(self):
		def rot13_func(s):
			def escape_html(s):
				return cgi.escape(s, quote = True)

			mutable_string = ""
			for c in s:
				if(ord(c) >= 97 and ord(c) <= 122):
					#perform rot13 on a-z	
					mutable_string += chr(((ord(c) - ord('a')+13) % 26)+ord('a'))
				elif(ord(c) >= 65 and ord(c) <= 90):
					#perform rot13 on A-Z
					mutable_string += chr(((ord(c) - ord('A')+13) % 26)+ord('A'))
				else:
					mutable_string += escape_html(c)
			return mutable_string

		rot13_request = self.request.get('text')
		print 'rot13_request is:'
		rot13_request
		rot13_output = ""
		rot13_output += rot13_func(rot13_request)
		print 'rot12_output is: '
		print rot13_output
		self.write_form(rot13_output)

	def write_form(self,rot13_string=""):
		self.response.out.write(form % {"rot13_string":rot13_string})


app = webapp2.WSGIApplication([
	('/unit2/rot13',Rot13)
], debug=True)
