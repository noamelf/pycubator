import re
def _do_code_blocks(text):
    """Process Markdown `<pre><code>` blocks."""
    code_block_re = re.compile(r'''
        (?:\n\n|\A\n?)
        (               # $1 = the code block -- one or more lines, starting with a space/tab
          (?:
            (?:[ ]{%d} | \t)  # Lines must start with a tab or a tab-width of spaces
            .*\n+
          )+
        )
        ((?=^[ ]{0,%d}\S)|\Z)   # Lookahead for non-space at line-start, or end of doc
        # Lookahead to make sure this block isn't already in a code block.
        # Needed when syntax highlighting is being used.
        (?![^<]*\</code\>)
        ''' % (4, 4),
        re.M | re.X)
    return code_block_re.sub(replace, text)

def replace(match):
    txt = match.group(1) 
    _outdent_re = re.compile(r'^(\t|[ ]{1,%d})' % 12, re.M)
    txt1 = _outdent_re.sub('',txt)
    return '\n```python\n{}\n```\n'.format(txt1)
import sys
fn = sys.argv[1]
with open(fn) as f:
    print(_do_code_blocks(f.read()))

