import argparse

# ascending order
IONIAN = [2, 2, 1, 2, 2, 2, 1]

# calculating mode intervals
MODES = []
MODES.append(IONIAN)

for i in range(1, 7):
	MODES.append(MODES[0][i:] + MODES[0][:i])

SCALES = {
	# modes
	"ionian":       MODES[0],
	"dorian":       MODES[1],
	"phrygian":     MODES[2],
	"lydian":       MODES[3],
	"mixolydian":   MODES[4],
	"aeolian":      MODES[5],
	"locrian":      MODES[6],

	# other scales; by no means complete
	"melodic_minor":    [2, 1, 2, 2, 2, 2, 1],
	"harmonic_minor":   [2, 1, 2, 2, 1, 3, 1],
	"diminished":       [2, 1, 2, 1, 2, 1, 2, 1],
	"whole_tone":       [2, 2, 2, 2, 2, 2],
	"blues":            [3, 2, 1, 1, 3, 2],
	"minor_pentatonic": [3, 2, 2, 3, 2],
	"major_pentatonic": [2, 2, 3, 2, 3],
	"hungarian_minor":  [2, 1, 3, 1, 1, 3, 1],
	"persian":          [1, 3, 1, 1, 2, 3, 1],
	"hirojoshi":        [2, 1, 4, 1, 4],
	"arabian":          [2, 2, 1, 1, 2, 2, 2],
	"scottish":         [2, 3, 2, 2, 3]

}

# synonyms
SCALES["major"] = SCALES["ionian"]
SCALES["natural_minor"] = SCALES["aeolian"] #this might not be correct

# with an offset of 0, the root is C
DEFUALT_NOTE_NAMES = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#Bb", "B"]
ROOT_OFFSETS = {
	"C": 0,
	"D": 2,
	"E": 4,
	"F": 5,
	"G": 7,
	"A": 9,
	"B": 11
}

# TODO: figure out how to name enharmonic notes
for k, v in list(ROOT_OFFSETS.items()):
	ROOT_OFFSETS[f'{k}#'] = (v + 1) % 12
	ROOT_OFFSETS[f'{k}##'] = (v + 2) % 12
	ROOT_OFFSETS[f'{k}b'] = (v - 1) % 12
	ROOT_OFFSETS[f'{k}bb'] = (v - 2) % 12

for i in range(len(DEFUALT_NOTE_NAMES)):
	ROOT_OFFSETS[DEFUALT_NOTE_NAMES[i]] = i




# Circle of 5ths
# an offset of 0 is the major scale
Co5s = [0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5]

## CHORDS
# with reference to the major scale, this list defines the number of accumulated
# semitones at each interval
# i.e., the root interval (I) is 0 semitones away from the root,
# the perfect 5th is 7 semitones away from the root


SEMITONE_TO_INTERVAL = {
	0: {"root"},
	1: {"b2", "b9"},
	2: {"2", "9"},
	3: {"#2", "b3", "#9"},
	4: {"3"},
	5: {"4", "11"},
	6: {"b5"},
	7: {"5"},
	8: {"#5"},
	9: {"6", "13"},
	10:{"b7"},
	11:{"7"}
}

#source: https://lotusmusic.com/chordtree.html
CHORD_SETS = {
	"5":            {"root", "5"}, # power chord
	"min6":         {"root", "b3", "5", "6"},
	"min6(add9)":   {"root", "b3", "5", "6", "9"},
	"min":          {"root", "b3", "5"},
	"min7":         {"root", "b3", "5", "b7"},
	"min9":         {"root", "b3", "5", "b7", "9"},
	"min11":        {"root", "b3", "5", "b7", "9", "11"},
	"min13":        {"root", "b3", "5", "b7", "9", "11", "13"},
	"min(maj7)":    {"root", "b3", "5", "7"},
	"dim(b3)":      {"root", "b3", "b5"},
	"dim7":         {"root", "b3", "b5", "6"},
	"min7(b5)":     {"root", "b3", "b5", "b7"}, # also called half diminished
	"aug":          {"root", "3", "#5"},
	"maj7(#5)":     {"root", "3", "#5", "7"},
	"dim3":         {"root", "3", "b5"},
	"maj7b5":       {"root", "3", "b5", "7"},
	"maj":          {"root", "3", "5"},
	"maj6":         {"root", "3", "5", "6"},
	"maj6(add9)":   {"root", "3", "5", "9"},
	"maj7":         {"root", "3", "5", "7"},
	"maj9":         {"root", "3", "5", "7", "9"},
	"maj11":        {"root", "3", "5", "7", "9", "11"},
	"maj13":        {"root", "3", "5", "7", "9", "11", "13"},
	"dom7":         {"root", "3", "5", "b7"},
	"dom9":         {"root", "3", "5", "b7", "9"},
	"dom11":        {"root", "3", "5", "b7", "9", "11"},
	"dom13":        {"root", "3", "5", "b7", "9", "11", "13"},
	"dom7(addb9)":  {"root", "3", "5", "b7", "b9"},
	"dom7(add#9)":  {"root", "3", "5", "b7", "#9"},
	"dom7(b5)":     {"root", "3", "b5", "b7"},
	"dom9(b5)":     {"root", "3", "b5", "b7", "9"},
	"dom11(b5)":    {"root", "3", "b5", "b7", "9", "11"},
	"dom13(b5)":    {"root", "3", "b5", "b7", "9", "11", "13"},
	"dom7(b5addb9)":{"root", "3", "b5", "b7", "b9"},
	"dom7(b5add#9)":{"root", "3", "b5", "b7", "#9"},
	"aug7":         {"root", "3", "#5", "b7"},
	"aug9":         {"root", "3", "#5", "b7", "9"},
	"aug11":        {"root", "3", "#5", "b7", "9", "11"},
	"aug13":        {"root", "3", "#5", "b7", "9", "11", "13"},
	"dom7(#5addb9)":{"root", "3", "#5", "b7", "b9"},
	"dom7(#5add#9)":{"root", "3", "#5", "b7", "#9"},

	"sus2":         {"root", "2", "5"},
	"sus4":         {"root", "4", "5"},
	"dom7sus4":     {"root", "4", "5", "b7"},
	"dom7sus2":     {"root", "2", "5", "b7"}
}

# 1st, 2nd, 3rd, 4th, 5th, 6th, 7th,
MAJOR_SEMITONE_INTERVALS = [0, 2, 4, 5, 7, 9, 11]

def note_from_semitone(st):

	return DEFUALT_NOTE_NAMES[st]
	# notes = []
	# for k, v in ROOT_OFFSETS.items():
	# 	if st == v:
	# 		notes.append(k)
	# return notes

def notes_to_semitones(notes):
	return [ROOT_OFFSETS[n] for n in notes]

def notes_in_scale(key_st, scale):
	notes_return = []
	if scale in SCALES:
		root_offset = key_st
		if 12 > root_offset >= 0:
			note_i = root_offset

			notes_return.append(note_i)
			for distance in SCALES[scale]:
				note_i = (note_i + distance) % 12
				notes_return.append(note_i)

		else:
			print(f"{key_st} is not a valid key")

	else:
		print(f"Entered scale {scale} not supported")

	return notes_return


def available_chords_from_notes(notes_st):
	return_chords = {}

	for i in range(len(notes_st)):
		# find the index in BASE_NOTES of the note at the root of the chord
		root_note_i = notes_st[i]


		semitone_differences = set()
		for note in notes_st:
			ind_diff = note - root_note_i
			if ind_diff < 0:
				ind_diff += 12
			semitone_differences.add(ind_diff)

		semitone_intervals = set()
		for diff in semitone_differences:
			semitone_intervals.update(SEMITONE_TO_INTERVAL[diff])

		if notes_st[i] not in return_chords:
			for k, v in CHORD_SETS.items():
				if v.issubset(semitone_intervals):
					return_chords[notes_st[i]] = return_chords.get(notes_st[i], [])
					return_chords[notes_st[i]].append(k)
	return return_chords

def available_scales_from_notes(notes_st):

	return_scales = []
	# for each note, assume its the root
	for j in range(len(notes_st)):
		root_note = notes_st[j]

		all_scales = SCALES.keys()
		for scale in all_scales:
			scale_notes = set(notes_in_scale(root_note, scale))
			if set(notes_st).issubset(set(scale_notes)):
				return_scales.append((scale, note_from_semitone(root_note)))

	return return_scales


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("-mode", "--mode", default="chords", help="If chords, returns all valid chords in the given"
	                                                              "scale/key. If scale, then the program will find all"
	                                                              "valid scales for the given set of notes")
	parser.add_argument('-scale', '--scale', help="Scale to use")
	parser.add_argument('-key', '--key', help="Root key of the scale")
	parser.add_argument("-notes", "--notes", help="The notes to match to scales")

	args = parser.parse_args()

	if args.mode == "chords":
		notes = notes_in_scale(notes_to_semitones([args.key])[0], args.scale)
		print([note_from_semitone(n) for n in notes])
		all_chords = available_chords_from_notes(notes)
		for key, chords in all_chords.items():
			print(f"\n\n{DEFUALT_NOTE_NAMES[key]} chords that can be played in {args.scale} {args.key}:")
			print(chords)

	if args.mode == "scale":
		notes = args.notes.split(" ")
		print(notes)
		scales = available_scales_from_notes(notes_to_semitones(notes))
		print(scales)




