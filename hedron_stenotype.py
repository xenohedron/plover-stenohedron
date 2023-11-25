from plover.system.english_stenotype import ORTHOGRAPHY_RULES, ORTHOGRAPHY_RULES_ALIASES, ORTHOGRAPHY_WORDLIST

KEYS = (
  '#', '%',
  '@-', '^-', '+-', 'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-', '~',
  'A-', 'O-', '-E', '-U',
  '*', '-L', '-R', '-P', '-S', '-T', '-K', '-G', '-Z', '-Y', '-D',
)

# Hedron Theory intended to use #^+STKPWHRAOEU*LRPSTKGZYD
# For custom extensibility, @~% are provided
# Depending on hardware, #^+ may need to be relocated
# Expected keymap as follows:
#   ####   %%%% 
#  @+TPH~ *LPTGY
#  ^SKWR~ *RSKZD
#      AO EU    

IMPLICIT_HYPHEN_KEYS = ('~', 'A-', 'O-', '-E', '-U', '*')

# TODO: Support folding of prefixes and strokes with more than one key?
# Or handle it entirely from programmatically generated dictionary?
SUFFIX_KEYS = ('-Z', '-D', '-G')

NUMBER_KEY = None
NUMBERS = {}
FERAL_NUMBER_KEY = False

# TODO: Should this really be hardcoded?
UNDO_STROKE_STENO = '*'

# TODO: Only Gemini PR has been fully implemented.
# Right bank keys have been renamed for all.
# Keyboard has split +S and ~*, but not the others.
KEYMAPS = {
    'Gemini PR': {
        '#'         : ('#1', '#2', '#3', '#4', '#5'),
        '%'         : ('#6', '#7', '#8', '#9', '#A'),
        '@-'        : '#B',
        '^-'        : '#C',
        '+-'        : 'S1-',
        'S-'        : 'S2-',
        'T-'        : 'T-',
        'K-'        : 'K-',
        'P-'        : 'P-',
        'W-'        : 'W-',
        'H-'        : 'H-',
        'R-'        : 'R-',
        '~'         : ('*1', '*2'),
        'A-'        : 'A-',
        'O-'        : 'O-',
        '-E'        : '-E',
        '-U'        : '-U',
        '*'         : ('*3', '*4'),
        '-L'        : '-F',
        '-R'        : '-R',
        '-P'        : '-P',
        '-S'        : '-B',
        '-T'        : '-L',
        '-K'        : '-G',
        '-G'        : '-T',
        '-Z'        : '-S',
        '-Y'        : '-D',
        '-D'        : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        '+-'        : 'q',
        'S-'        : 'a',
        'T-'        : 'w',
        'K-'        : 's',
        'P-'        : 'e',
        'W-'        : 'd',
        'H-'        : 'r',
        'R-'        : 'f',
        '~'         : ('t', 'g'),
        'A-'        : 'c',
        'O-'        : 'v',
        '-E'        : 'n',
        '-U'        : 'm',
        '*'         : ('y', 'h'),
        '-L'        : 'u',
        '-R'        : 'j',
        '-P'        : 'i',
        '-S'        : 'k',
        '-T'        : 'o',
        '-K'        : 'l',
        '-G'        : 'p',
        '-Z'        : ';',
        '-Y'        : '[',
        '-D'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
    'Passport': {
        '#'    : '#',
        'S-'   : ('S', 'C'),
        'T-'   : 'T',
        'K-'   : 'K',
        'P-'   : 'P',
        'W-'   : 'W',
        'H-'   : 'H',
        'R-'   : 'R',
        'A-'   : 'A',
        'O-'   : 'O',
        '*'    : ('~', '*'),
        '-E'   : 'E',
        '-U'   : 'U',
        '-L'   : 'F',
        '-R'   : 'Q',
        '-P'   : 'N',
        '-S'   : 'B',
        '-T'   : 'L',
        '-K'   : 'G',
        '-G'   : 'Y',
        '-Z'   : 'X',
        '-Y'   : 'D',
        '-D'   : 'Z',
        'no-op': ('!', '^', '+'),
    },
    'Stentura': {
        '#'    : '#',
        'S-'   : 'S-',
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'W-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-U'   : '-U',
        '-L'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-S'   : '-B',
        '-T'   : '-L',
        '-K'   : '-G',
        '-G'   : '-T',
        '-Z'   : '-S',
        '-Y'   : '-D',
        '-D'   : '-Z',
        'no-op': '^',
    },
    'TX Bolt': {
        '#'    : '#',
        'S-'   : 'S-',
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'W-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-U'   : '-U',
        '-L'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-S'   : '-B',
        '-T'   : '-L',
        '-K'   : '-G',
        '-G'   : '-T',
        '-Z'   : '-S',
        '-Y'   : '-D',
        '-D'   : '-Z',
    },
    'Treal': {
        '#'    : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B'),
        'S-'   : ('S1-', 'S2-'),
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'W-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : ('*1', '*2'),
        '-E'   : '-E',
        '-U'   : '-U',
        '-L'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-S'   : '-B',
        '-T'   : '-L',
        '-K'   : '-G',
        '-G'   : '-T',
        '-Z'   : '-S',
        '-Y'   : '-D',
        '-D'   : '-Z',
        'no-op': ('X1-', 'X2-', 'X3'),
    },
}

# TODO: include hedron default dictionaries instead
DICTIONARIES_ROOT = 'asset:plover:assets'
DEFAULT_DICTIONARIES = ()
