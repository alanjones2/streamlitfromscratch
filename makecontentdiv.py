import markdown

#names = ["StreamlitFromScratch0""StreamlitFromScratch1""StreamlitFromScratch2""StreamlitFromScratch3""StreamlitFromScratch4"]
name = "./deploytocloud/deploytocloud"
with open(f'./{name}.md', 'r') as reader:
    md = reader.read()

#file = io.open('data.txt','r', encoding='utf-16-le')

html = markdown.markdown(md, extensions=['fenced_code'])
o = open(f'./{name}.div','w')
o.write(html)

o.close()