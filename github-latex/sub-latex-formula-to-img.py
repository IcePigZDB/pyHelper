import sys
import re
# $$ formula $$
interline_tag = '<!-- $${}$$ -->\n<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?{}</div>'
interline_pattern = '\$\$\n*(.*?)\n*\$\$'
# $ formula $
inline_tag= '<!-- ${}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math={}">'
inline_pattern = '\$\n*(.*?)\n*\$'

def replace_tex(content):
	def dashrepl(matchobj, tag):
		formular = matchobj.group(1)
		return tag.format(formular, formular)

	content = re.sub(interline_pattern, lambda mo: dashrepl(mo, interline_tag), content)
	content = re.sub(inline_pattern, lambda mo: dashrepl(mo, inline_tag), content)

	return content

if __name__=='__main__':
	assert len(sys.argv) > 1, "Error: need filename as a argument"
	filename = sys.argv[1]
	with open(filename, mode='r',encoding='utf-8') as f:
		content = f.read()
	with open(filename, mode='w',encoding='utf-8') as f:
		f.write(replace_tex(content))