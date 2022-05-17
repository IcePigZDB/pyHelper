import sys
import re
from urllib.parse import quote
# $$
# formula
# $$
interline_tag = '\n<img src="https://render.githubusercontent.com/render/math?math={}" class="ee_img tr_noresize" eeimg="1">\n'
# https://www.zhihu.com/equation?tex={}
# http://latex.codecogs.com/gif.latex?{}
interline_pattern = '\$\$\n*((.|\n)*?)\n*\$\$' # (.|\n) . or \n
# $formula$
inline_tag = '<img src="https://render.githubusercontent.com/render/math?math={}" class="ee_img tr_noresize" eeimg="1">'
inline_pattern = '\$\n*(.*?)\n*\$'

def replace_tex(content):
	def dashrepl_quote(matchobj, tag):
		formular = matchobj.group(1)
		formular = quote(formular) # quote & to %26 in $$ x&= a+1$$, otherwise, thers will be error when render with githubusercontent.com
		return tag.format(formular, formular)

	content = re.sub(interline_pattern, lambda mo: dashrepl_quote(mo, interline_tag), content)
	content = re.sub(inline_pattern, lambda mo: dashrepl_quote(mo, inline_tag), content)

	return content

if __name__=='__main__':
	assert len(sys.argv) > 1, "Error: need filename as a argument"
	filename = sys.argv[1]
	with open(filename, mode='r',encoding='utf-8') as f:
		content = f.read()
	with open(filename, mode='w',encoding='utf-8') as f:
		f.write(replace_tex(content))