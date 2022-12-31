import markdown

with open('StreamlitFromScratch1.md', 'r') as reader:
    md = reader.read()


html = markdown.markdown(md, extensions=['fenced_code','codehilite'])

header = """
<html>
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/main.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

    <link rel="stylesheet" href="styles.css">
</head>
<body>
"""
foot="""
</body>
</html>
"""
o = open('test.html','w')
o.write(header+html+foot)

o.close()