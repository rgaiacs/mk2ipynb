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

import logging
import mk2ipynb.convert

def main():
    import argparse

    parser = argparse.ArgumentParser(
            description='Convert markdown files into IPython Notebook')
    parser.add_argument('-i', '--input', type=str, required=True,
            help='input file')
    parser.add_argument('-o', '--output', type=str,
            help='output file')
    parser.add_argument('-l', '--log', type=str,
            help='log file')

    args = parser.parse_args()

    if (not args.input.endswith('.mk')):
        print('The input file must be a Markdown file ending with \'.mk\'')
        return 1
    else:
        if (not args.output):
            args.output = args.input.replace('.mk', '.ipynb')
        if (not args.log):
            args.log = args.input.replace('.mk', '.log')

    logging.basicConfig(filename=args.log, filemode='w',  level=logging.INFO)

    logging.info('Started')
    mk2ipynb.convert.run(args.input, args.output)
    logging.info('Finished')
