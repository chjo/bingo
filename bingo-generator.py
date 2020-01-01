#!/usr/bin/env python

import random
import math
import os

########################
# Settings
in_file_name = "sample_terms.txt"
cards = 12
########################

current_workdir = os.path.dirname(os.path.realpath(__file__))
in_file_path = os.path.join(current_workdir, in_file_name)
out_file_path = "{}.html".format(os.path.splitext(in_file_path)[0])

# read in the bingo card_entries
in_file = open(in_file_path, "r")

card_entries = [line.strip() for line in in_file.readlines()]

in_file.close()


# Generates an HTML table representation of the bingo card for card_entries
def generate_card(card_entries, pagebreak=True):
    # ts = card_entries[:12] + ["FREE SPACE"] + card_entries[12:24]
    if pagebreak:
        res = '<table class="newpage">\n'
    else:
        res = "<table>\n"
    for i_row in range(5):
        res += "\t<tr>\n"

        for i_col in range(5):
            single_entry = card_entries[i_col][i_row].split(" ", 1)
            res += (
                "\t\t<td>"
                + "<b>{}</b><br>{}".format(single_entry[0], single_entry[1])
                + "</td>\n"
            )

        res += "\t</tr>\n"
    res += "</table>\n"
    return res


# XHTML4 Strict, y'all!
head = (
    '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\n'
    '<html lang="en">\n<head>\n'
    '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n'
    "<title>Bingo Cards</title>\n"
    '<style type="text/css">\n'
    "\tbody { font-size: 14px; }\n"
    "\ttable { margin: 40px auto; border-spacing: 2px; }\n"
    "\t.newpage { page-break-after:always; }\n"
    "\ttr { height: 90px; }\n"
    "\ttd { text-align: center; border: thin black solid; padding: 10px; width: 90px; }\n"
    "</style>\n</head>\n<body>\n"
)

out_file = open(out_file_path, "w")
out_file.write(head)

n_card_entries = len(card_entries)
number_terms_per_column = math.floor(n_card_entries / 5)
terms_b = card_entries[0:number_terms_per_column]
terms_i = card_entries[number_terms_per_column : number_terms_per_column * 2]
terms_n = card_entries[2 * number_terms_per_column : 3 * number_terms_per_column]
terms_g = card_entries[3 * number_terms_per_column : 4 * number_terms_per_column]
terms_o = card_entries[4 * number_terms_per_column :]

for i in range(cards):

    shuffled_bingo_terms_list = [
        random.sample(terms_b, len(terms_b))[:5],
        random.sample(terms_i, len(terms_i))[:5],
        random.sample(terms_n, len(terms_n))[:5],
        random.sample(terms_g, len(terms_g))[:5],
        random.sample(terms_o, len(terms_o))[:5],
    ]

    if ((i + 1) % 2) == 0:
        out_file.write(generate_card(shuffled_bingo_terms_list))
    else:
        out_file.write(generate_card(shuffled_bingo_terms_list, False))

out_file.write("</body></html>")
out_file.close()
