from pprint import pprint
import re
import sys

def sub_headings(markdown: str) -> str:
    return re.sub(r'#{1,3}\s*(.+)', lambda match: f'<h1>{match.group(1)}<\\h1>', markdown)

def sub_bold_and_italic(markdown: str) -> str:
    def replace_match(match):
        delimiter = match.group(1)
        text = match.group(2)
        if delimiter == '**':
            return f'<b>{sub_bold_and_italic(text)}</b>'
        elif delimiter == '*':
            return f'<i>{sub_bold_and_italic(text)}</i>'

    return re.sub(r'(\*\*|\*)(.+?)\1', replace_match, markdown)

def sub_enumerated_list(markdown: str) -> str:
    intermediate = re.sub(r'((\d+\.\s*.*\n)+)', lambda match: f'<ol>\n{match.group(1)}</ol>\n', markdown)
    return re.sub(r'\d+\.\s*(.*)', lambda match: f'<li>{match.group(1)}</li>', intermediate)

def sub_url_link(markdown: str) -> str:
    def replace_match(match):
        start = match.group(1)
        text  = match.group(2)
        link  = match.group(3)

        if start == '!':
            return f'<img src="{link}" alt="{text}"/>'
        else: # start == nothing
            return f'<a href="{link}">{text}</a>'

    return re.sub(r'(!?)\[(.*)\]\((.*)\)', replace_match, markdown)

def main(filepath: str):
    with open(filepath, 'r') as file:
        content = file.read()
        with open(filepath + ".txt", 'w') as res:
            res.write(sub_url_link(sub_enumerated_list(sub_bold_and_italic(sub_headings(content)))))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 markdown-to-html.py <markdown-file>")

    main(sys.argv[1])
