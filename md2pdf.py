
import sys
import os

# check command-line args
if len(sys.argv) != 2:
    print 'usage python %s link_file' % sys.argv[0]
    exit()

# read link file
with open( sys.argv[1] ) as READ:
    txt = READ.read()

# process link file
links = map( lambda x: x.strip() , txt.split('\n') )
links = filter( lambda x: x != '' , links )

# processing data
cnt = 0
LINE = '\n%s\n' % ('=' * 80)

for link in links:
    base_name = 'lab%02d' % cnt

    md_name   = base_name + '.md'
    html_name = base_name + '.html'
    pdf_name  = base_name + '.pdf'

    print LINE
    print 'Link %d -> %s -> %s -> %s' % (cnt, md_name, html_name, pdf_name)
    print LINE

    command1 = 'wget %s -O %s'       % (link, md_name)
    command2 = 'grip %s --export %s' % (md_name, html_name)
    command3 = 'wkhtmltopdf %s %s'   % (html_name, pdf_name)

    os.system( command1 )
    os.system( command2 )
    os.system( command3 )

    cnt += 1

