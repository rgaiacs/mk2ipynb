# Markdown2IPythonNotebook
# Copyright (C) 2013  Raniere Silva
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import logging

def setup(ipynb):
    """
    Setup the ipynb.

    :param ipynb: the ipynb structure in memory
    :type ipynb: dict
    """
    # TODO Add option to the name of ipynb
    ipynb['metadata'] = {'name': 'simple'}
    ipynb['nbformat'] = 3
    ipynb['nbformat_minor'] = 0
    ipynb['worksheet'] = [{'cells': [], 'metadata': dict()}]

def parse_line_code(line):
    """
    Parse one line of code in markdown
    """
    # line is code
    if(line.startswith('    >>>')):
        return 1
    # line is markdown
    else:
        return 0

def run(i, o):
    """
    Run the conversion from markdown to IPython Notebook.

    :param i: the input file
    :type i: str
    :param o: the output file
    :type o: str
    """
    
    ipynb = dict()  # the variable that will store the ipynb in memory
    setup(ipynb)
    with open(i, 'r') as fi:
        old_lstatus = None
        old_empty_line = None
        for l in fi.readlines():
            if(l == '\n'):
                old_empty_line = True
            else:
                lstatus = parse_line_code(l)
                if(old_lstatus is not None):
                    if (old_lstatus == lstatus):
                        if(lstatus == 1):
                            source += l.replace('    >>> ', '')
                        elif(lstatus == 0):
                            source += l
                    else:
                        if(lstatus == 1):
                            # code
                            c = {"cell_type": "code",
                                 "collapsed": False,
                                 "input": source,
                                 "language": "python",
                                 "metadata": {},
                                 "outputs": [],
                                 "prompt_number": None}
                            source = l.replace('    >>> ', '')
                        elif(lstatus == 0):
                            # markdown
                            c = {"cell_type": "markdown",
                                 "metadata": {},
                                 "source": source}
                            source = l
                        ipynb['worksheet'][0]['cells'].append(c)
                        old_lstatus = False
                        old_lstatus = lstatus
                else:
                    old_lstatus = lstatus
                    if(lstatus == 1):
                        source = l.replace('    >>> ', '')
                    elif(lstatus == 0):
                        source = l
    # For the last part
    if(lstatus == 1):
        # code
        c = {"cell_type": "code",
             "collapsed": false,
             "input": source,
             "language": "python",
             "metadata": {},
             "outputs": [],
             "prompt_number": None}
    elif(lstatus == 0):
        # markdown
        c = {"cell_type": "markdown",
             "metadata": {},
             "source": source}
    ipynb['worksheet'][0]['cells'].append(c)
    # The options for json.dumps are need to pretty print.
    with open(o, 'w') as fo:
        json.dump(ipynb, fo, indent=4, sort_keys=True)

