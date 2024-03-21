import sys
import markdown

if sys.argv[1] == "markdown":
    with open(sys.argv[2]) as f:
        contents = f.read()
        html_contents = markdown.markdown(contents)

    with open(sys.argv[3], 'w') as f:
        f.write(html_contents)