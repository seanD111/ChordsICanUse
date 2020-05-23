import argparse

INTERVAL_TO_SEMITONES = {
	"W": 2,
	"H": 1
}

# ascending order
# IONIAN = "WWHWWWH"
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

	# other scales
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
SCALES["natural_minor"] = SCALES["aeolian"]

BASE_NOTES = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#Bb", "B"]

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


def notes_in_scale(key, scale):
	notes_return = []
	if scale in SCALES:
		root_offset = -1

		for i in range(len(BASE_NOTES)):
			is_key_puretone = not ("#" in key or "b" in key)
			is_note_puretone = not ("#" in BASE_NOTES[i] or "b" in BASE_NOTES[i])

			if (is_note_puretone == is_key_puretone) and (key in BASE_NOTES[i]):
				root_offset = i

		if root_offset >= 0:
			note_i = root_offset

			notes_return.append(BASE_NOTES[note_i])
			for distance in SCALES[scale]:
				note_i = (note_i + distance) % len(BASE_NOTES)
				notes_return.append(BASE_NOTES[note_i])

		else:
			print(f"{key} is not a valid key")

	else:
		print(f"Entered scale {scale} not supported")

	return notes_return


def available_chords_from_notes(notes):
	for i in range(len(notes)):
		# find the index in BASE_NOTES of the note at the root of the chord
		root_note_i = BASE_NOTES.index(notes[i])


		semitone_differences = set()
		for note in notes:
			ind_diff = BASE_NOTES.index(note) - root_note_i
			if ind_diff < 0:
				ind_diff += 12
			semitone_differences.add(ind_diff)

		semitone_intervals = set()
		for diff in semitone_differences:
			semitone_intervals.update(SEMITONE_TO_INTERVAL[diff])

		print(f"\n\n{BASE_NOTES[root_note_i]} chords that can be played in the scale:")
		for k, v in CHORD_SETS.items():
			if v.issubset(semitone_intervals):
				print(k)





	return semitone_intervals



if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument('Scale', help="Scale to use")
	parser.add_argument('Key', help="Root key of the scale")

	args = parser.parse_args()

	notes = notes_in_scale(args.Key, args.Scale)
	print(notes)
	print(available_chords_from_notes(notes))


