
import html

def clean_input(value):
    return html.escape(value, quote=True)

