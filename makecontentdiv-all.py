import markdown

names = ["sfs-Intro",
        "sfs-Installation",
        "sfs-editors",
        "sfs-text",
        "sfs-media",
        "sfs-data-intro",
        "sfs-data-text",
        "sfs-data-stcharts",
        "sfs-data-pyplot",
        "sfs-data-altair",
        "sfs-data-plotly",
        "sfs-data-bokeh",
        "sfs-data-vega-lite",
        "sfs-dashboard-layouts",
        "sfs-conclusion"]

for name in names:
    print(name)
    with open(f'./{name}.md', 'r') as reader:
        md = reader.read()
    html = markdown.markdown(md, extensions=['fenced_code'])
    o = open(f'./{name}.div','w')
    o.write(html)
    o.close()