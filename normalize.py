#!/usr/bin/python3

import re
from pprint import pprint

class Normalize(object):



	area_codes = {
		# http://www.allareacodes.com/area_code_listings_by_state.htm
		'Alabama': [205, 251, 256, 334, 938],
		'Alaska': [907],
		'Arizona': [480, 520, 602, 623, 928],
		'Arkansas': [479, 501, 870],
		'California': [209, 213, 310, 323, 408, 415, 424, 442, 510, 530, 559, 562, 619, 626, 650, 657, 661, 707, 714, 747, 760, 805, 818, 831, 858, 909, 916, 925, 949, 951],
		'Colorado': [303, 719, 720, 970],
		'Connecticut': [203, 475, 860],
		'Delaware': [302],
		'District of Columbia': [202],
		'Florida': [239, 305, 321, 352, 386, 407, 561, 727, 754, 772, 786, 813, 850, 863, 904, 941, 954],
		'Georgia': [229, 404, 470, 478, 678, 706, 762, 770, 912],
		'Hawaii': [808],
		'Idaho': [208],
		'Illinois': [217, 224, 309, 312, 331, 618, 630, 708, 773, 779, 815, 847, 872],
		'Indiana': [219, 260, 317, 574, 765, 812],
		'Iowa': [319, 515, 563, 641, 712],
		'Kansas': [316, 620, 785, 913],
		'Kentucky': [270, 502, 606, 859],
		'Louisiana': [225, 318, 337, 504, 985],
		'Maine': [207],
		'Maryland': [240, 301, 410, 443],
		'Massachusetts': [339, 351, 413, 508, 617, 774, 781, 857, 978],
		'Michigan': [231, 248, 269, 313, 517, 586, 616, 734, 810, 906, 947, 989],
		'Minnesota': [218, 320, 507, 612, 651, 763, 952],
		'Mississippi': [228, 601, 662, 769],
		'Missouri': [314, 417, 573, 636, 660, 816],
		'Montana': [406],
		'Nebraska': [308, 402],
		'Nevada': [702, 775],
		'New Hampshire': [603],
		'New Jersey': [201, 551, 609, 732, 848, 856, 862, 908, 973],
		'New Mexico': [505, 575],
		'New York': [212, 315, 347, 516, 518, 585, 607, 631, 646, 716, 718, 845, 914, 917, 929],
		'North Carolina': [252, 336, 704, 828, 910, 919, 980],
		'North Dakota': [701],
		'Ohio': [216, 234, 330, 419, 440, 513, 567, 614, 740, 937],
		'Oklahoma': [405, 539, 580, 918],
		'Oregon': [458, 503, 541, 971],
		'Pennsylvania': [215, 267, 412, 484, 570, 610, 717, 724, 814, 878],
		'Rhode Island': [401],
		'South Carolina': [803, 843, 864],
		'South Dakota': [605],
		'Tennessee': [423, 615, 731, 865, 901, 931],
		'Texas': [210, 214, 254, 281, 325, 361, 409, 430, 432, 469, 512, 682, 713, 806, 817, 830, 832, 903, 915, 936, 940, 956, 972, 979],
		'Utah': [385, 435, 801],
		'Vermont': [802],
		'Virginia': [276, 434, 540, 571, 703, 757, 804],
		'Washington': [206, 253, 360, 425, 509],
		'West Virginia': [304, 681],
		'Wisconsin': [262, 414, 608, 715, 920],
		'Wyoming': [307],

		'American Samoa': [684],
		'Guam': [671],
		'Puerto Rico': [787, 939],
		'Virgin Islands': [340]
	}

	abbreviations = {
		# http://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations
		# First value is the canonical USPS code for the state
		'Alabama': ['al', 'ala '],
		'Alaska': ['ak', 'alas'],
		'Arizona': ['az', 'ariz'],
		'Arkansas': ['ar', 'ark '],
		'California': ['ca', 'cf', 'calif', 'cal', 'cali'],
		'Colorado': ['co', 'cl', 'colo', 'col'],
		'Connecticut': ['ct', 'conn'],
		'Delaware': ['de', 'dl', 'del'],
		'District of Columbia': ['dc', 'washington dc', 'wash dc'],
		'Florida': ['fl', 'fla', 'flor'],
		'Georgia': ['ga'],
		'Hawaii': ['hi', 'ha'],
		'Idaho': ['id', 'ida'],
		'Illinois': ['il', 'ill', 'ills'],
		'Indiana': ['in', 'ind'],
		'Iowa': ['ia', 'ioa'],
		'Kansas': ['ks', 'ka', 'kans', 'kan'],
		'Kentucky': ['ky', 'ken',' kent'],
		'Louisiana': ['la'],
		'Maine': ['me'],
		'Maryland': ['md'],
		'Massachusetts': ['ma', 'mass '],
		'Michigan': ['mi', 'mc', 'mich '],
		'Minnesota': ['mn', 'minn'],
		'Mississippi': ['ms', 'miss '],
		'Missouri': ['mo'],
		'Montana': ['mt', 'mont '],
		'Nebraska': ['ne', 'nb', 'nebr', 'neb '],
		'Nevada': ['nv', 'nev'],
		'New Hampshire': ['nh'],
		'New Jersey': ['nj'],
		'New Mexico': ['nm', 'n mex', 'new m'],
		'New York': ['ny', 'n york'],
		'North Carolina': ['nc', 'n car'],
		'North Dakota': ['nd', 'n dak', 'nodak'],
		'Ohio': ['oh', 'o'],
		'Oklahoma': ['ok', 'okla'],
		'Oregon': ['or', 'oreg', 'ore'],
		'Pennsylvania': ['pa', 'penn', 'penna'],
		'Rhode Island': ['ri', 'ri and pp', 'r isl'],
		'South Carolina': ['sc', 's car'],
		'South Dakota': ['sd', 's dak', 'sodak'],
		'Tennessee': ['tn', 'tenn'],
		'Texas': ['tx', 'tex'],
		'Utah': ['ut'],
		'Vermont': ['vt'],
		'Virginia': ['va', 'virg'],
		'Washington': ['wa', 'wn', 'wash'],
		'West Virginia': ['wv', 'wva', 'w virg'],
		'Wisconsin': ['wi', 'ws', 'wis', 'wisc'],
		'Wyoming': ['wy', 'wyo'],

		'American Samoa': ['as'],
		'Guam': ['gu'],
		'Puerto Rico': ['pr'],
		'Virgin Islands': ['vi']
	}



	def __init__(self):
		pass


	def area_code_in_state(self, state, code):

		if isinstance(code, str):
			if code.isdigit():
				code = int(code)
			else:
				raise TypeError("code must be an integer or numeric string")

		return code in self.area_codes[state]



	def canonical_state(self, abbreviation):

		abbreviation = re.sub('[^a-z ]', '', abbreviation.lower())

		for k,v in self.abbreviations.items():
			if abbreviation == k.lower() or abbreviation in v:
				return k

		return False



def main():
	n = Normalize()

	print("Testing...")

	assert n.area_code_in_state('Indiana', 219)==True
	assert n.area_code_in_state('Indiana', 351)==False
	assert n.canonical_state('in')=='Indiana'
	assert n.canonical_state('in')!='Washington'

	print("Done!")

	return True



if __name__ == '__main__':
	main()
