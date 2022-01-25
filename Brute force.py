import csv
import time

"""A brute force method to determine the lowest number of guesses to solve Absurdle. This is not intended to be 
used with Absurdle and will diminish the experience of the game."""


# Functions

def Guess(gues, dictionary, func):
    """Determines which letters need to be in the correct position, wrong position or not in th word at all to
    give the maximum amount of words remaining in the dictionary, for a given guess"""

    decider = {}
    for i0 in range(3):  # Try each letter in the correct position, the wrong position and not in the word
        for i1 in range(3):
            for i2 in range(3):
                for i3 in range(3):
                    for i4 in range(3):
                        dictionaryTemp = dictionary.copy()
                        dictionaryTemp = func[i0](0, gues[0], dictionaryTemp)
                        dictionaryTemp = func[i1](1, gues[1], dictionaryTemp)
                        dictionaryTemp = func[i2](2, gues[2], dictionaryTemp)
                        dictionaryTemp = func[i3](3, gues[3], dictionaryTemp)
                        dictionaryTemp = func[i4](4, gues[4], dictionaryTemp)
                        decider[str(i0) + str(i1) + str(i2) + str(i3) + str(i4)] = len(dictionaryTemp)
    maxKey = max(decider, key=decider.get)  # Find the result that leaves the most words in the dictionary
    return maxKey


def Right(no, let, dic):
    """Adds words to dictionary if the letter 'let' appears in the word in position 'no'."""

    diccopy = []  # temporary dictionary
    for wor in dic:
        if wor[no] == let:
            diccopy.append(wor)
    return diccopy


def Place(no, let, dic):
    """Adds words to dictionary if the letter 'let' appears in the word in position OTHER THAN 'no'."""

    diccopy = []  # temporary dictionary
    for wor in dic:
        if (let in wor) and (wor[no] != let):
            diccopy.append(wor)
    return diccopy


def Wrong(no, let, dic):
    """Adds words to dictionary if the letter 'let' does not appear in the word."""

    diccopy = []  # temporary dictionary
    for wor in dic:
        if let not in wor:
            diccopy.append(wor)
    return diccopy


def count_letters(dic, alpha):
    """Counts how many of each letter remain in dictionary."""

    record = [[alpha[i], 0] for i in range(26)]  # list of letters and a tally.
    for i in range(26):
        for wor in dic:
            if alpha[i] in wor:
                record[i][1] += 1
    print(record)


def first_words(dictionary, fun, max):
    """First guesses that give the smallest remaining dictionary"""

    results = []
    dic = [i for i in dictionary]
    for word in dic:
        print(word)
        maxKey1 = Guess(word, dic, fun)
        for i in range(5):
            dic = fun[int(maxKey1[i])](i, word[i], dic)
        if len(dic) <= max:
            results.append([word, len(dic), maxKey1])
        dic = [i for i in dictionary]
    return results


def second_words(dictionary, fun, max, list):
    """Second guesses, based on the list of first guesses, that give the smallest remaining dictionary"""

    dic = [i for i in dictionary]
    results = []
    for line in list:
        [word, first, maxKey1] = line
        print(word)
        for j in range(5):
            dic = fun[int(maxKey1[j])](j, word[j], dic)

        dic2 = [i2 for i2 in dic]
        for word2 in dic2:
            maxKey2 = Guess(word2, dic2, fun)
            for j2 in range(5):
                dic2 = fun[int(maxKey2[j2])](j2, word2[j2], dic2)
            if len(dic2) <= max:
                results.append([word, str(first), maxKey1, word2, str(len(dic2)), maxKey2])
            dic2 = [i2 for i2 in dic]
        dic = [i for i in dictionary]
    return results


def third_words(dictionary, fun, max, list):
    """Third guesses, based on the list of second guesses, that give the smallest remaining dictionary"""

    dic = [i for i in dictionary]
    results = []
    for line in list:
        [word, first, maxKey1, word2, second, maxKey2] = line
        print(word, word2)
        for i in range(5):
            dic = fun[int(maxKey1[i])](i, word[i], dic)
        for j2 in range(5):
            dic = fun[int(maxKey2[j2])](j2, word2[j2], dic)

        dic3 = [i3 for i3 in dic]
        for word3 in dic3:
            maxKey3 = Guess(word3, dic3, fun)
            for j3 in range(5):
                dic3 = fun[int(maxKey3[j3])](j3, word3[j3], dic3)
            if len(dic3) <= max:
                results.append([word, str(first), word2, str(second), word3, str(len(dic3)), dic3[1]])
            dic3 = [i3 for i3 in dic]
        dic = [i for i in dictionary]
    return results


# Import English 5 letter words as a list and alphabet

dictionary = ['ABACK', 'ABASE', 'ABATE', 'ABBEY', 'ABBOT', 'ABHOR', 'ABIDE', 'ABLED', 'ABODE', 'ABORT', 'ABOUT',
              'ABOVE', 'ABUSE', 'ABYSS', 'ACORN', 'ACRID', 'ACTOR', 'ACUTE', 'ADAGE', 'ADAPT', 'ADEPT', 'ADMIN',
              'ADMIT', 'ADOBE', 'ADOPT', 'ADORE', 'ADORN', 'ADULT', 'AFFIX', 'AFIRE', 'AFOOT', 'AFOUL', 'AFTER',
              'AGAIN', 'AGAPE', 'AGATE', 'AGENT', 'AGILE', 'AGING', 'AGLOW', 'AGONY', 'AGORA', 'AGREE', 'AHEAD',
              'AIDER', 'AISLE', 'ALARM', 'ALBUM', 'ALERT', 'ALGAE', 'ALIBI', 'ALIEN', 'ALIGN', 'ALIKE', 'ALIVE',
              'ALLAY', 'ALLEY', 'ALLOT', 'ALLOW', 'ALLOY', 'ALOFT', 'ALONE', 'ALONG', 'ALOOF', 'ALOUD', 'ALPHA',
              'ALTAR', 'ALTER', 'AMASS', 'AMAZE', 'AMBER', 'AMBLE', 'AMEND', 'AMISS', 'AMITY', 'AMONG', 'AMPLE',
              'AMPLY', 'AMUSE', 'ANGEL', 'ANGER', 'ANGLE', 'ANGRY', 'ANGST', 'ANIME', 'ANKLE', 'ANNEX', 'ANNOY',
              'ANNUL', 'ANODE', 'ANTIC', 'ANVIL', 'AORTA', 'APART', 'APHID', 'APING', 'APNEA', 'APPLE', 'APPLY',
              'APRON', 'APTLY', 'ARBOR', 'ARDOR', 'ARENA', 'ARGUE', 'ARISE', 'ARMOR', 'AROMA', 'AROSE', 'ARRAY',
              'ARROW', 'ARSON', 'ARTSY', 'ASCOT', 'ASHEN', 'ASIDE', 'ASKEW', 'ASSAY', 'ASSET', 'ATOLL', 'ATONE',
              'ATTIC', 'AUDIO', 'AUDIT', 'AUGUR', 'AUNTY', 'AVAIL', 'AVERT', 'AVIAN', 'AVOID', 'AWAIT', 'AWAKE',
              'AWARD', 'AWARE', 'AWASH', 'AWFUL', 'AWOKE', 'AXIAL', 'AXIOM', 'AXION', 'AZURE', 'BACON', 'BADGE',
              'BADLY', 'BAGEL', 'BAGGY', 'BAKER', 'BALER', 'BALMY', 'BANAL', 'BANJO', 'BARGE', 'BARON', 'BASAL',
              'BASIC', 'BASIL', 'BASIN', 'BASIS', 'BASTE', 'BATCH', 'BATHE', 'BATON', 'BATTY', 'BAWDY', 'BAYOU',
              'BEACH', 'BEADY', 'BEARD', 'BEAST', 'BEECH', 'BEEFY', 'BEFIT', 'BEGAN', 'BEGAT', 'BEGET', 'BEGIN',
              'BEGUN', 'BEING', 'BELCH', 'BELIE', 'BELLE', 'BELLY', 'BELOW', 'BENCH', 'BERET', 'BERRY', 'BERTH',
              'BESET', 'BETEL', 'BEVEL', 'BEZEL', 'BIBLE', 'BICEP', 'BIDDY', 'BIGOT', 'BILGE', 'BILLY', 'BINGE',
              'BINGO', 'BIOME', 'BIRCH', 'BIRTH', 'BISON', 'BITTY', 'BLACK', 'BLADE', 'BLAME', 'BLAND', 'BLANK',
              'BLARE', 'BLAST', 'BLAZE', 'BLEAK', 'BLEAT', 'BLEED', 'BLEEP', 'BLEND', 'BLESS', 'BLIMP', 'BLIND',
              'BLINK', 'BLISS', 'BLITZ', 'BLOAT', 'BLOCK', 'BLOKE', 'BLOND', 'BLOOD', 'BLOOM', 'BLOWN', 'BLUER',
              'BLUFF', 'BLUNT', 'BLURB', 'BLURT', 'BLUSH', 'BOARD', 'BOAST', 'BOBBY', 'BONEY', 'BONGO', 'BONUS',
              'BOOBY', 'BOOST', 'BOOTH', 'BOOTY', 'BOOZE', 'BOOZY', 'BORAX', 'BORNE', 'BOSOM', 'BOSSY', 'BOTCH',
              'BOUGH', 'BOULE', 'BOUND', 'BOWEL', 'BOXER', 'BRACE', 'BRAID', 'BRAIN', 'BRAKE', 'BRAND', 'BRASH',
              'BRASS', 'BRAVE', 'BRAVO', 'BRAWL', 'BRAWN', 'BREAD', 'BREAK', 'BREED', 'BRIAR', 'BRIBE', 'BRICK',
              'BRIDE', 'BRIEF', 'BRINE', 'BRING', 'BRINK', 'BRINY', 'BRISK', 'BROAD', 'BROIL', 'BROKE', 'BROOD',
              'BROOK', 'BROOM', 'BROTH', 'BROWN', 'BRUNT', 'BRUSH', 'BRUTE', 'BUDDY', 'BUDGE', 'BUGGY', 'BUGLE',
              'BUILD', 'BUILT', 'BULGE', 'BULKY', 'BULLY', 'BUNCH', 'BUNNY', 'BURLY', 'BURNT', 'BURST', 'BUSED',
              'BUSHY', 'BUTCH', 'BUTTE', 'BUXOM', 'BUYER', 'BYLAW', 'CABAL', 'CABBY', 'CABIN', 'CABLE', 'CACAO',
              'CACHE', 'CACTI', 'CADDY', 'CADET', 'CAGEY', 'CAIRN', 'CAMEL', 'CAMEO', 'CANAL', 'CANDY', 'CANNY',
              'CANOE', 'CANON', 'CAPER', 'CAPUT', 'CARAT', 'CARGO', 'CAROL', 'CARRY', 'CARVE', 'CASTE', 'CATCH',
              'CATER', 'CATTY', 'CAULK', 'CAUSE', 'CAVIL', 'CEASE', 'CEDAR', 'CELLO', 'CHAFE', 'CHAFF', 'CHAIN',
              'CHAIR', 'CHALK', 'CHAMP', 'CHANT', 'CHAOS', 'CHARD', 'CHARM', 'CHART', 'CHASE', 'CHASM', 'CHEAP',
              'CHEAT', 'CHECK', 'CHEEK', 'CHEER', 'CHESS', 'CHEST', 'CHICK', 'CHIDE', 'CHIEF', 'CHILD', 'CHILI',
              'CHILL', 'CHIME', 'CHINA', 'CHIRP', 'CHOCK', 'CHOIR', 'CHOKE', 'CHORD', 'CHORE', 'CHOSE', 'CHUCK',
              'CHUMP', 'CHUNK', 'CHURN', 'CHUTE', 'CIDER', 'CIGAR', 'CINCH', 'CIRCA', 'CIVIC', 'CIVIL', 'CLACK',
              'CLAIM', 'CLAMP', 'CLANG', 'CLANK', 'CLASH', 'CLASP', 'CLASS', 'CLEAN', 'CLEAR', 'CLEAT', 'CLEFT',
              'CLERK', 'CLICK', 'CLIFF', 'CLIMB', 'CLING', 'CLINK', 'CLOAK', 'CLOCK', 'CLONE', 'CLOSE', 'CLOTH',
              'CLOUD', 'CLOUT', 'CLOVE', 'CLOWN', 'CLUCK', 'CLUED', 'CLUMP', 'CLUNG', 'COACH', 'COAST', 'COBRA',
              'COCOA', 'COLON', 'COLOR', 'COMET', 'COMFY', 'COMIC', 'COMMA', 'CONCH', 'CONDO', 'CONIC', 'COPSE',
              'CORAL', 'CORER', 'CORNY', 'COUCH', 'COUGH', 'COULD', 'COUNT', 'COUPE', 'COURT', 'COVEN', 'COVER',
              'COVET', 'COVEY', 'COWER', 'COYLY', 'CRACK', 'CRAFT', 'CRAMP', 'CRANE', 'CRANK', 'CRASH', 'CRASS',
              'CRATE', 'CRAVE', 'CRAWL', 'CRAZE', 'CRAZY', 'CREAK', 'CREAM', 'CREDO', 'CREED', 'CREEK', 'CREEP',
              'CREME', 'CREPE', 'CREPT', 'CRESS', 'CREST', 'CRICK', 'CRIED', 'CRIER', 'CRIME', 'CRIMP', 'CRISP',
              'CROAK', 'CROCK', 'CRONE', 'CRONY', 'CROOK', 'CROSS', 'CROUP', 'CROWD', 'CROWN', 'CRUDE', 'CRUEL',
              'CRUMB', 'CRUMP', 'CRUSH', 'CRUST', 'CRYPT', 'CUBIC', 'CUMIN', 'CURIO', 'CURLY', 'CURRY', 'CURSE',
              'CURVE', 'CURVY', 'CUTIE', 'CYBER', 'CYCLE', 'CYNIC', 'DADDY', 'DAILY', 'DAIRY', 'DAISY', 'DALLY',
              'DANCE', 'DANDY', 'DATUM', 'DAUNT', 'DEALT', 'DEATH', 'DEBAR', 'DEBIT', 'DEBUG', 'DEBUT', 'DECAL',
              'DECAY', 'DECOR', 'DECOY', 'DECRY', 'DEFER', 'DEIGN', 'DEITY', 'DELAY', 'DELTA', 'DELVE', 'DEMON',
              'DEMUR', 'DENIM', 'DENSE', 'DEPOT', 'DEPTH', 'DERBY', 'DETER', 'DETOX', 'DEUCE', 'DEVIL', 'DIARY',
              'DICEY', 'DIGIT', 'DILLY', 'DIMLY', 'DINER', 'DINGO', 'DINGY', 'DIODE', 'DIRGE', 'DIRTY', 'DISCO',
              'DITCH', 'DITTO', 'DITTY', 'DIVER', 'DIZZY', 'DODGE', 'DODGY', 'DOGMA', 'DOING', 'DOLLY', 'DONOR',
              'DONUT', 'DOPEY', 'DOUBT', 'DOUGH', 'DOWDY', 'DOWEL', 'DOWNY', 'DOWRY', 'DOZEN', 'DRAFT', 'DRAIN',
              'DRAKE', 'DRAMA', 'DRANK', 'DRAPE', 'DRAWL', 'DRAWN', 'DREAD', 'DREAM', 'DRESS', 'DRIED', 'DRIER',
              'DRIFT', 'DRILL', 'DRINK', 'DRIVE', 'DROIT', 'DROLL', 'DRONE', 'DROOL', 'DROOP', 'DROSS', 'DROVE',
              'DROWN', 'DRUID', 'DRUNK', 'DRYER', 'DRYLY', 'DUCHY', 'DULLY', 'DUMMY', 'DUMPY', 'DUNCE', 'DUSKY',
              'DUSTY', 'DUTCH', 'DUVET', 'DWARF', 'DWELL', 'DWELT', 'DYING', 'EAGER', 'EAGLE', 'EARLY', 'EARTH',
              'EASEL', 'EATEN', 'EATER', 'EBONY', 'ECLAT', 'EDICT', 'EDIFY', 'EERIE', 'EGRET', 'EIGHT', 'EJECT',
              'EKING', 'ELATE', 'ELBOW', 'ELDER', 'ELECT', 'ELEGY', 'ELFIN', 'ELIDE', 'ELITE', 'ELOPE', 'ELUDE',
              'EMAIL', 'EMBED', 'EMBER', 'EMCEE', 'EMPTY', 'ENACT', 'ENDOW', 'ENEMA', 'ENEMY', 'ENJOY', 'ENNUI',
              'ENSUE', 'ENTER', 'ENTRY', 'ENVOY', 'EPOCH', 'EPOXY', 'EQUAL', 'EQUIP', 'ERASE', 'ERECT', 'ERODE',
              'ERROR', 'ERUPT', 'ESSAY', 'ESTER', 'ETHER', 'ETHIC', 'ETHOS', 'ETUDE', 'EVADE', 'EVENT', 'EVERY',
              'EVICT', 'EVOKE', 'EXACT', 'EXALT', 'EXCEL', 'EXERT', 'EXILE', 'EXIST', 'EXPEL', 'EXTOL', 'EXTRA',
              'EXULT', 'EYING', 'FABLE', 'FACET', 'FAINT', 'FAIRY', 'FAITH', 'FALSE', 'FANCY', 'FANNY', 'FARCE',
              'FATAL', 'FATTY', 'FAULT', 'FAUNA', 'FAVOR', 'FEAST', 'FECAL', 'FEIGN', 'FELLA', 'FELON', 'FEMME',
              'FEMUR', 'FENCE', 'FERAL', 'FERRY', 'FETAL', 'FETCH', 'FETID', 'FETUS', 'FEVER', 'FEWER', 'FIBER',
              'FIBRE', 'FICUS', 'FIELD', 'FIEND', 'FIERY', 'FIFTH', 'FIFTY', 'FIGHT', 'FILER', 'FILET', 'FILLY',
              'FILMY', 'FILTH', 'FINAL', 'FINCH', 'FINER', 'FIRST', 'FISHY', 'FIXER', 'FIZZY', 'FJORD', 'FLACK',
              'FLAIL', 'FLAIR', 'FLAKE', 'FLAKY', 'FLAME', 'FLANK', 'FLARE', 'FLASH', 'FLASK', 'FLECK', 'FLEET',
              'FLESH', 'FLICK', 'FLIER', 'FLING', 'FLINT', 'FLIRT', 'FLOAT', 'FLOCK', 'FLOOD', 'FLOOR', 'FLORA',
              'FLOSS', 'FLOUR', 'FLOUT', 'FLOWN', 'FLUFF', 'FLUID', 'FLUKE', 'FLUME', 'FLUNG', 'FLUNK', 'FLUSH',
              'FLUTE', 'FLYER', 'FOAMY', 'FOCAL', 'FOCUS', 'FOGGY', 'FOIST', 'FOLIO', 'FOLLY', 'FORAY', 'FORCE',
              'FORGE', 'FORGO', 'FORTE', 'FORTH', 'FORTY', 'FORUM', 'FOUND', 'FOYER', 'FRAIL', 'FRAME', 'FRANK',
              'FRAUD', 'FREAK', 'FREED', 'FREER', 'FRESH', 'FRIAR', 'FRIED', 'FRILL', 'FRISK', 'FRITZ', 'FROCK',
              'FROND', 'FRONT', 'FROST', 'FROTH', 'FROWN', 'FROZE', 'FRUIT', 'FUDGE', 'FUGUE', 'FULLY', 'FUNGI',
              'FUNKY', 'FUNNY', 'FUROR', 'FURRY', 'FUSSY', 'FUZZY', 'GAFFE', 'GAILY', 'GAMER', 'GAMMA', 'GAMUT',
              'GASSY', 'GAUDY', 'GAUGE', 'GAUNT', 'GAUZE', 'GAVEL', 'GAWKY', 'GAYER', 'GAYLY', 'GAZER', 'GECKO',
              'GEEKY', 'GEESE', 'GENIE', 'GENRE', 'GHOST', 'GHOUL', 'GIANT', 'GIDDY', 'GIPSY', 'GIRLY', 'GIRTH',
              'GIVEN', 'GIVER', 'GLADE', 'GLAND', 'GLARE', 'GLASS', 'GLAZE', 'GLEAM', 'GLEAN', 'GLIDE', 'GLINT',
              'GLOAT', 'GLOBE', 'GLOOM', 'GLORY', 'GLOSS', 'GLOVE', 'GLYPH', 'GNASH', 'GNOME', 'GODLY', 'GOING',
              'GOLEM', 'GOLLY', 'GONAD', 'GONER', 'GOODY', 'GOOEY', 'GOOFY', 'GOOSE', 'GORGE', 'GOUGE', 'GOURD',
              'GRACE', 'GRADE', 'GRAFT', 'GRAIL', 'GRAIN', 'GRAND', 'GRANT', 'GRAPE', 'GRAPH', 'GRASP', 'GRASS',
              'GRATE', 'GRAVE', 'GRAVY', 'GRAZE', 'GREAT', 'GREED', 'GREEN', 'GREET', 'GRIEF', 'GRILL', 'GRIME',
              'GRIMY', 'GRIND', 'GRIPE', 'GROAN', 'GROIN', 'GROOM', 'GROPE', 'GROSS', 'GROUP', 'GROUT', 'GROVE',
              'GROWL', 'GROWN', 'GRUEL', 'GRUFF', 'GRUNT', 'GUARD', 'GUAVA', 'GUESS', 'GUEST', 'GUIDE', 'GUILD',
              'GUILE', 'GUILT', 'GUISE', 'GULCH', 'GULLY', 'GUMBO', 'GUMMY', 'GUPPY', 'GUSTO', 'GUSTY', 'GYPSY',
              'HABIT', 'HAIRY', 'HALVE', 'HANDY', 'HAPPY', 'HARDY', 'HAREM', 'HARPY', 'HARRY', 'HARSH', 'HASTE',
              'HASTY', 'HATCH', 'HATER', 'HAUNT', 'HAUTE', 'HAVEN', 'HAVOC', 'HAZEL', 'HEADY', 'HEARD', 'HEART',
              'HEATH', 'HEAVE', 'HEAVY', 'HEDGE', 'HEFTY', 'HEIST', 'HELIX', 'HELLO', 'HENCE', 'HERON', 'HILLY',
              'HINGE', 'HIPPO', 'HIPPY', 'HITCH', 'HOARD', 'HOBBY', 'HOIST', 'HOLLY', 'HOMER', 'HONEY', 'HONOR',
              'HORDE', 'HORNY', 'HORSE', 'HOTEL', 'HOTLY', 'HOUND', 'HOUSE', 'HOVEL', 'HOVER', 'HOWDY', 'HUMAN',
              'HUMID', 'HUMOR', 'HUMPH', 'HUMUS', 'HUNCH', 'HUNKY', 'HURRY', 'HUSKY', 'HUSSY', 'HUTCH', 'HYDRO',
              'HYENA', 'HYMEN', 'HYPER', 'ICILY', 'ICING', 'IDEAL', 'IDIOM', 'IDIOT', 'IDLER', 'IDYLL', 'IGLOO',
              'ILIAC', 'IMAGE', 'IMBUE', 'IMPEL', 'IMPLY', 'INANE', 'INBOX', 'INCUR', 'INDEX', 'INEPT', 'INERT',
              'INFER', 'INGOT', 'INLAY', 'INLET', 'INNER', 'INPUT', 'INTER', 'INTRO', 'IONIC', 'IRATE', 'IRONY',
              'ISLET', 'ISSUE', 'ITCHY', 'IVORY', 'JAUNT', 'JAZZY', 'JELLY', 'JERKY', 'JETTY', 'JEWEL', 'JIFFY',
              'JOINT', 'JOIST', 'JOKER', 'JOLLY', 'JOUST', 'JUDGE', 'JUICE', 'JUICY', 'JUMBO', 'JUMPY', 'JUNTA',
              'JUNTO', 'JUROR', 'KAPPA', 'KARMA', 'KAYAK', 'KEBAB', 'KHAKI', 'KINKY', 'KIOSK', 'KITTY', 'KNACK',
              'KNAVE', 'KNEAD', 'KNEED', 'KNEEL', 'KNELT', 'KNIFE', 'KNOCK', 'KNOLL', 'KNOWN', 'KOALA', 'KRILL',
              'LABEL', 'LABOR', 'LADEN', 'LADLE', 'LAGER', 'LANCE', 'LANKY', 'LAPEL', 'LAPSE', 'LARGE', 'LARVA',
              'LASSO', 'LATCH', 'LATER', 'LATHE', 'LATTE', 'LAUGH', 'LAYER', 'LEACH', 'LEAFY', 'LEAKY', 'LEANT',
              'LEAPT', 'LEARN', 'LEASE', 'LEASH', 'LEAST', 'LEAVE', 'LEDGE', 'LEECH', 'LEERY', 'LEFTY', 'LEGAL',
              'LEGGY', 'LEMON', 'LEMUR', 'LEPER', 'LEVEL', 'LEVER', 'LIBEL', 'LIEGE', 'LIGHT', 'LIKEN', 'LILAC',
              'LIMBO', 'LIMIT', 'LINEN', 'LINER', 'LINGO', 'LIPID', 'LITHE', 'LIVER', 'LIVID', 'LLAMA', 'LOAMY',
              'LOATH', 'LOBBY', 'LOCAL', 'LOCUS', 'LODGE', 'LOFTY', 'LOGIC', 'LOGIN', 'LOOPY', 'LOOSE', 'LORRY',
              'LOSER', 'LOUSE', 'LOUSY', 'LOVER', 'LOWER', 'LOWLY', 'LOYAL', 'LUCID', 'LUCKY', 'LUMEN', 'LUMPY',
              'LUNAR', 'LUNCH', 'LUNGE', 'LUPUS', 'LURCH', 'LURID', 'LUSTY', 'LYING', 'LYMPH', 'LYNCH', 'LYRIC',
              'MACAW', 'MACHO', 'MACRO', 'MADAM', 'MADLY', 'MAFIA', 'MAGIC', 'MAGMA', 'MAIZE', 'MAJOR', 'MAKER',
              'MAMBO', 'MAMMA', 'MANGA', 'MANGE', 'MANGO', 'MANGY', 'MANIA', 'MANIC', 'MANLY', 'MANOR', 'MAPLE',
              'MARCH', 'MARRY', 'MARSH', 'MASON', 'MASSE', 'MATCH', 'MATEY', 'MAUVE', 'MAXIM', 'MAYBE', 'MAYOR',
              'MEALY', 'MEANT', 'MEATY', 'MECCA', 'MEDAL', 'MEDIA', 'MEDIC', 'MELEE', 'MELON', 'MERCY', 'MERGE',
              'MERIT', 'MERRY', 'METAL', 'METER', 'METRO', 'MICRO', 'MIDGE', 'MIDST', 'MIGHT', 'MILKY', 'MIMIC',
              'MINCE', 'MINER', 'MINIM', 'MINOR', 'MINTY', 'MINUS', 'MIRTH', 'MISER', 'MISSY', 'MOCHA', 'MODAL',
              'MODEL', 'MODEM', 'MOGUL', 'MOIST', 'MOLAR', 'MOLDY', 'MONEY', 'MONTH', 'MOODY', 'MOOSE', 'MORAL',
              'MORON', 'MORPH', 'MOSSY', 'MOTEL', 'MOTIF', 'MOTOR', 'MOTTO', 'MOULT', 'MOUND', 'MOUNT', 'MOURN',
              'MOUSE', 'MOUTH', 'MOVER', 'MOVIE', 'MOWER', 'MUCKY', 'MUCUS', 'MUDDY', 'MULCH', 'MUMMY', 'MUNCH',
              'MURAL', 'MURKY', 'MUSHY', 'MUSIC', 'MUSKY', 'MUSTY', 'MYRRH', 'NADIR', 'NAIVE', 'NANNY', 'NASAL',
              'NASTY', 'NATAL', 'NAVAL', 'NAVEL', 'NEEDY', 'NEIGH', 'NERDY', 'NERVE', 'NEVER', 'NEWER', 'NEWLY',
              'NICER', 'NICHE', 'NIECE', 'NIGHT', 'NINJA', 'NINNY', 'NINTH', 'NOBLE', 'NOBLY', 'NOISE', 'NOISY',
              'NOMAD', 'NOOSE', 'NORTH', 'NOSEY', 'NOTCH', 'NOVEL', 'NUDGE', 'NURSE', 'NUTTY', 'NYLON', 'NYMPH',
              'OAKEN', 'OBESE', 'OCCUR', 'OCEAN', 'OCTAL', 'OCTET', 'ODDER', 'ODDLY', 'OFFAL', 'OFFER', 'OFTEN',
              'OLDEN', 'OLDER', 'OLIVE', 'OMBRE', 'OMEGA', 'ONION', 'ONSET', 'OPERA', 'OPINE', 'OPIUM', 'OPTIC',
              'ORBIT', 'ORDER', 'ORGAN', 'OTHER', 'OTTER', 'OUGHT', 'OUNCE', 'OUTDO', 'OUTER', 'OUTGO', 'OVARY',
              'OVATE', 'OVERT', 'OVINE', 'OVOID', 'OWING', 'OWNER', 'OXIDE', 'OZONE', 'PADDY', 'PAGAN', 'PAINT',
              'PALER', 'PALSY', 'PANEL', 'PANIC', 'PANSY', 'PAPAL', 'PAPER', 'PARER', 'PARKA', 'PARRY', 'PARSE',
              'PARTY', 'PASTA', 'PASTE', 'PASTY', 'PATCH', 'PATIO', 'PATSY', 'PATTY', 'PAUSE', 'PAYEE', 'PAYER',
              'PEACE', 'PEACH', 'PEARL', 'PECAN', 'PEDAL', 'PENAL', 'PENCE', 'PENNE', 'PENNY', 'PERCH', 'PERIL',
              'PERKY', 'PESKY', 'PESTO', 'PETAL', 'PETTY', 'PHASE', 'PHONE', 'PHONY', 'PHOTO', 'PIANO', 'PICKY',
              'PIECE', 'PIETY', 'PIGGY', 'PILOT', 'PINCH', 'PINEY', 'PINKY', 'PINTO', 'PIPER', 'PIQUE', 'PITCH',
              'PITHY', 'PIVOT', 'PIXEL', 'PIXIE', 'PIZZA', 'PLACE', 'PLAID', 'PLAIN', 'PLAIT', 'PLANE', 'PLANK',
              'PLANT', 'PLATE', 'PLAZA', 'PLEAD', 'PLEAT', 'PLIED', 'PLIER', 'PLUCK', 'PLUMB', 'PLUME', 'PLUMP',
              'PLUNK', 'PLUSH', 'POESY', 'POINT', 'POISE', 'POKER', 'POLAR', 'POLKA', 'POLYP', 'POOCH', 'POPPY',
              'PORCH', 'POSER', 'POSIT', 'POSSE', 'POUCH', 'POUND', 'POUTY', 'POWER', 'PRANK', 'PRAWN', 'PREEN',
              'PRESS', 'PRICE', 'PRICK', 'PRIDE', 'PRIED', 'PRIME', 'PRIMO', 'PRINT', 'PRIOR', 'PRISM', 'PRIVY',
              'PRIZE', 'PROBE', 'PRONE', 'PRONG', 'PROOF', 'PROSE', 'PROUD', 'PROVE', 'PROWL', 'PROXY', 'PRUDE',
              'PRUNE', 'PSALM', 'PUBIC', 'PUDGY', 'PUFFY', 'PULPY', 'PULSE', 'PUNCH', 'PUPAL', 'PUPIL', 'PUPPY',
              'PUREE', 'PURER', 'PURGE', 'PURSE', 'PUSHY', 'PUTTY', 'PYGMY', 'QUACK', 'QUAIL', 'QUAKE', 'QUALM',
              'QUARK', 'QUART', 'QUASH', 'QUASI', 'QUEEN', 'QUEER', 'QUELL', 'QUERY', 'QUEST', 'QUEUE', 'QUICK',
              'QUIET', 'QUILL', 'QUILT', 'QUIRK', 'QUITE', 'QUOTA', 'QUOTE', 'QUOTH', 'RABBI', 'RABID', 'RACER',
              'RADAR', 'RADII', 'RADIO', 'RAINY', 'RAISE', 'RAJAH', 'RALLY', 'RALPH', 'RAMEN', 'RANCH', 'RANDY',
              'RANGE', 'RAPID', 'RARER', 'RASPY', 'RATIO', 'RATTY', 'RAVEN', 'RAYON', 'RAZOR', 'REACH', 'REACT',
              'READY', 'REALM', 'REARM', 'REBAR', 'REBEL', 'REBUS', 'REBUT', 'RECAP', 'RECUR', 'RECUT', 'REEDY',
              'REFER', 'REFIT', 'REGAL', 'REHAB', 'REIGN', 'RELAX', 'RELAY', 'RELIC', 'REMIT', 'RENAL', 'RENEW',
              'REPAY', 'REPEL', 'REPLY', 'RERUN', 'RESET', 'RESIN', 'RETCH', 'RETRO', 'RETRY', 'REUSE', 'REVEL',
              'REVUE', 'RHINO', 'RHYME', 'RIDER', 'RIDGE', 'RIFLE', 'RIGHT', 'RIGID', 'RIGOR', 'RINSE', 'RIPEN',
              'RIPER', 'RISEN', 'RISER', 'RISKY', 'RIVAL', 'RIVER', 'RIVET', 'ROACH', 'ROAST', 'ROBIN', 'ROBOT',
              'ROCKY', 'RODEO', 'ROGER', 'ROGUE', 'ROOMY', 'ROOST', 'ROTOR', 'ROUGE', 'ROUGH', 'ROUND', 'ROUSE',
              'ROUTE', 'ROVER', 'ROWDY', 'ROWER', 'ROYAL', 'RUDDY', 'RUDER', 'RUGBY', 'RULER', 'RUMBA', 'RUMOR',
              'RUPEE', 'RURAL', 'RUSTY', 'SADLY', 'SAFER', 'SAINT', 'SALAD', 'SALLY', 'SALON', 'SALSA', 'SALTY',
              'SALVE', 'SALVO', 'SANDY', 'SANER', 'SAPPY', 'SASSY', 'SATIN', 'SATYR', 'SAUCE', 'SAUCY', 'SAUNA',
              'SAUTE', 'SAVOR', 'SAVOY', 'SAVVY', 'SCALD', 'SCALE', 'SCALP', 'SCALY', 'SCAMP', 'SCANT', 'SCARE',
              'SCARF', 'SCARY', 'SCENE', 'SCENT', 'SCION', 'SCOFF', 'SCOLD', 'SCONE', 'SCOOP', 'SCOPE', 'SCORE',
              'SCORN', 'SCOUR', 'SCOUT', 'SCOWL', 'SCRAM', 'SCRAP', 'SCREE', 'SCREW', 'SCRUB', 'SCRUM', 'SCUBA',
              'SEDAN', 'SEEDY', 'SEGUE', 'SEIZE', 'SEMEN', 'SENSE', 'SEPIA', 'SERIF', 'SERUM', 'SERVE', 'SETUP',
              'SEVEN', 'SEVER', 'SEWER', 'SHACK', 'SHADE', 'SHADY', 'SHAFT', 'SHAKE', 'SHAKY', 'SHALE', 'SHALL',
              'SHALT', 'SHAME', 'SHANK', 'SHAPE', 'SHARD', 'SHARE', 'SHARK', 'SHARP', 'SHAVE', 'SHAWL', 'SHEAR',
              'SHEEN', 'SHEEP', 'SHEER', 'SHEET', 'SHEIK', 'SHELF', 'SHELL', 'SHIED', 'SHIFT', 'SHINE', 'SHINY',
              'SHIRE', 'SHIRK', 'SHIRT', 'SHOAL', 'SHOCK', 'SHONE', 'SHOOK', 'SHOOT', 'SHORE', 'SHORN', 'SHORT',
              'SHOUT', 'SHOVE', 'SHOWN', 'SHOWY', 'SHREW', 'SHRUB', 'SHRUG', 'SHUCK', 'SHUNT', 'SHUSH', 'SHYLY',
              'SIEGE', 'SIEVE', 'SIGHT', 'SIGMA', 'SILKY', 'SILLY', 'SINCE', 'SINEW', 'SINGE', 'SIREN', 'SISSY',
              'SIXTH', 'SIXTY', 'SKATE', 'SKIER', 'SKIFF', 'SKILL', 'SKIMP', 'SKIRT', 'SKULK', 'SKULL', 'SKUNK',
              'SLACK', 'SLAIN', 'SLANG', 'SLANT', 'SLASH', 'SLATE', 'SLAVE', 'SLEEK', 'SLEEP', 'SLEET', 'SLEPT',
              'SLICE', 'SLICK', 'SLIDE', 'SLIME', 'SLIMY', 'SLING', 'SLINK', 'SLOOP', 'SLOPE', 'SLOSH', 'SLOTH',
              'SLUMP', 'SLUNG', 'SLUNK', 'SLURP', 'SLUSH', 'SLYLY', 'SMACK', 'SMALL', 'SMART', 'SMASH', 'SMEAR',
              'SMELL', 'SMELT', 'SMILE', 'SMIRK', 'SMITE', 'SMITH', 'SMOCK', 'SMOKE', 'SMOKY', 'SMOTE', 'SNACK',
              'SNAIL', 'SNAKE', 'SNAKY', 'SNARE', 'SNARL', 'SNEAK', 'SNEER', 'SNIDE', 'SNIFF', 'SNIPE', 'SNOOP',
              'SNORE', 'SNORT', 'SNOUT', 'SNOWY', 'SNUCK', 'SNUFF', 'SOAPY', 'SOBER', 'SOGGY', 'SOLAR', 'SOLID',
              'SOLVE', 'SONAR', 'SONIC', 'SOOTH', 'SOOTY', 'SORRY', 'SOUND', 'SOUTH', 'SOWER', 'SPACE', 'SPADE',
              'SPANK', 'SPARE', 'SPARK', 'SPASM', 'SPAWN', 'SPEAK', 'SPEAR', 'SPECK', 'SPEED', 'SPELL', 'SPELT',
              'SPEND', 'SPENT', 'SPERM', 'SPICE', 'SPICY', 'SPIED', 'SPIEL', 'SPIKE', 'SPIKY', 'SPILL', 'SPILT',
              'SPINE', 'SPINY', 'SPIRE', 'SPITE', 'SPLAT', 'SPLIT', 'SPOIL', 'SPOKE', 'SPOOF', 'SPOOK', 'SPOOL',
              'SPOON', 'SPORE', 'SPORT', 'SPOUT', 'SPRAY', 'SPREE', 'SPRIG', 'SPUNK', 'SPURN', 'SPURT', 'SQUAD',
              'SQUAT', 'SQUIB', 'STACK', 'STAFF', 'STAGE', 'STAID', 'STAIN', 'STAIR', 'STAKE', 'STALE', 'STALK',
              'STALL', 'STAMP', 'STAND', 'STANK', 'STARE', 'STARK', 'START', 'STASH', 'STATE', 'STAVE', 'STEAD',
              'STEAK', 'STEAL', 'STEAM', 'STEED', 'STEEL', 'STEEP', 'STEER', 'STEIN', 'STERN', 'STICK', 'STIFF',
              'STILL', 'STILT', 'STING', 'STINK', 'STINT', 'STOCK', 'STOIC', 'STOKE', 'STOLE', 'STOMP', 'STONE',
              'STONY', 'STOOD', 'STOOL', 'STOOP', 'STORE', 'STORK', 'STORM', 'STORY', 'STOUT', 'STOVE', 'STRAP',
              'STRAW', 'STRAY', 'STRIP', 'STRUT', 'STUCK', 'STUDY', 'STUFF', 'STUMP', 'STUNG', 'STUNK', 'STUNT',
              'STYLE', 'SUAVE', 'SUGAR', 'SUING', 'SUITE', 'SULKY', 'SULLY', 'SUMAC', 'SUNNY', 'SUPER', 'SURER',
              'SURGE', 'SURLY', 'SUSHI', 'SWAMI', 'SWAMP', 'SWARM', 'SWASH', 'SWATH', 'SWEAR', 'SWEAT', 'SWEEP',
              'SWEET', 'SWELL', 'SWEPT', 'SWIFT', 'SWILL', 'SWINE', 'SWING', 'SWIRL', 'SWISH', 'SWOON', 'SWOOP',
              'SWORD', 'SWORE', 'SWORN', 'SWUNG', 'SYNOD', 'SYRUP', 'TABBY', 'TABLE', 'TABOO', 'TACIT', 'TACKY',
              'TAFFY', 'TAINT', 'TAKEN', 'TAKER', 'TALLY', 'TALON', 'TAMER', 'TANGO', 'TANGY', 'TAPER', 'TAPIR',
              'TARDY', 'TAROT', 'TASTE', 'TASTY', 'TATTY', 'TAUNT', 'TAWNY', 'TEACH', 'TEARY', 'TEASE', 'TEDDY',
              'TEETH', 'TEMPO', 'TENET', 'TENOR', 'TENSE', 'TENTH', 'TEPEE', 'TEPID', 'TERRA', 'TERSE', 'TESTY',
              'THANK', 'THEFT', 'THEIR', 'THEME', 'THERE', 'THESE', 'THETA', 'THICK', 'THIEF', 'THIGH', 'THING',
              'THINK', 'THIRD', 'THONG', 'THORN', 'THOSE', 'THREE', 'THREW', 'THROB', 'THROW', 'THRUM', 'THUMB',
              'THUMP', 'THYME', 'TIARA', 'TIBIA', 'TIDAL', 'TIGER', 'TIGHT', 'TILDE', 'TIMER', 'TIMID', 'TIPSY',
              'TITAN', 'TITHE', 'TITLE', 'TOAST', 'TODAY', 'TODDY', 'TOKEN', 'TONAL', 'TONGA', 'TONIC', 'TOOTH',
              'TOPAZ', 'TOPIC', 'TORCH', 'TORSO', 'TORUS', 'TOTAL', 'TOTEM', 'TOUCH', 'TOUGH', 'TOWEL', 'TOWER',
              'TOXIC', 'TOXIN', 'TRACE', 'TRACK', 'TRACT', 'TRADE', 'TRAIL', 'TRAIN', 'TRAIT', 'TRAMP', 'TRASH',
              'TRAWL', 'TREAD', 'TREAT', 'TREND', 'TRIAD', 'TRIAL', 'TRIBE', 'TRICE', 'TRICK', 'TRIED', 'TRIPE',
              'TRITE', 'TROLL', 'TROOP', 'TROPE', 'TROUT', 'TROVE', 'TRUCE', 'TRUCK', 'TRUER', 'TRULY', 'TRUMP',
              'TRUNK', 'TRUSS', 'TRUST', 'TRUTH', 'TRYST', 'TUBAL', 'TUBER', 'TULIP', 'TULLE', 'TUMOR', 'TUNIC',
              'TURBO', 'TUTOR', 'TWANG', 'TWEAK', 'TWEED', 'TWEET', 'TWICE', 'TWINE', 'TWIRL', 'TWIST', 'TWIXT',
              'TYING', 'UDDER', 'ULCER', 'ULTRA', 'UMBRA', 'UNCLE', 'UNCUT', 'UNDER', 'UNDID', 'UNDUE', 'UNFED',
              'UNFIT', 'UNIFY', 'UNION', 'UNITE', 'UNITY', 'UNLIT', 'UNMET', 'UNSET', 'UNTIE', 'UNTIL', 'UNWED',
              'UNZIP', 'UPPER', 'UPSET', 'URBAN', 'URINE', 'USAGE', 'USHER', 'USING', 'USUAL', 'USURP', 'UTILE',
              'UTTER', 'VAGUE', 'VALET', 'VALID', 'VALOR', 'VALUE', 'VALVE', 'VAPID', 'VAPOR', 'VAULT', 'VAUNT',
              'VEGAN', 'VENOM', 'VENUE', 'VERGE', 'VERSE', 'VERSO', 'VERVE', 'VICAR', 'VIDEO', 'VIGIL', 'VIGOR',
              'VILLA', 'VINYL', 'VIOLA', 'VIPER', 'VIRAL', 'VIRUS', 'VISIT', 'VISOR', 'VISTA', 'VITAL', 'VIVID',
              'VIXEN', 'VOCAL', 'VODKA', 'VOGUE', 'VOICE', 'VOILA', 'VOMIT', 'VOTER', 'VOUCH', 'VOWEL', 'VYING',
              'WACKY', 'WAFER', 'WAGER', 'WAGON', 'WAIST', 'WAIVE', 'WALTZ', 'WARTY', 'WASTE', 'WATCH', 'WATER',
              'WAVER', 'WAXEN', 'WEARY', 'WEAVE', 'WEDGE', 'WEEDY', 'WEIGH', 'WEIRD', 'WELCH', 'WELSH', 'WENCH',
              'WHACK', 'WHALE', 'WHARF', 'WHEAT', 'WHEEL', 'WHELP', 'WHERE', 'WHICH', 'WHIFF', 'WHILE', 'WHINE',
              'WHINY', 'WHIRL', 'WHISK', 'WHITE', 'WHOLE', 'WHOOP', 'WHOSE', 'WIDEN', 'WIDER', 'WIDOW', 'WIDTH',
              'WIELD', 'WIGHT', 'WILLY', 'WIMPY', 'WINCE', 'WINCH', 'WINDY', 'WISER', 'WISPY', 'WITCH', 'WITTY',
              'WOKEN', 'WOMAN', 'WOMEN', 'WOODY', 'WOOER', 'WOOLY', 'WOOZY', 'WORDY', 'WORLD', 'WORRY', 'WORSE',
              'WORST', 'WORTH', 'WOULD', 'WOUND', 'WOVEN', 'WRACK', 'WRATH', 'WREAK', 'WRECK', 'WREST', 'WRING',
              'WRIST', 'WRITE', 'WRONG', 'WROTE', 'WRUNG', 'WRYLY', 'YACHT', 'YEARN', 'YEAST', 'YIELD', 'YOUNG',
              'YOUTH', 'ZEBRA', 'ZESTY', 'ZONAL']

# Create alphabet and import dictionary. Use dictionary above if .txt is not available.

# f = open("dictionary.txt", "r")
# dictionary = f.read().splitlines()
# print(dictionary)
# f.close()

##########################################################################################

start_time = time.time()

fun = (Wrong, Place, Right)  # Function choice
maxFirst, maxSecond, maxThird = 400, 30, 1  # Number of words left in dictionary after each guess, 300, 25, 3 is a good start

print("starting first")  # Finding first guess words that fit the above
first = first_words(dictionary, fun, maxFirst)
print(first)

print("starting second")  # Finding second guess words that fit the above, based on first
second = second_words(dictionary, fun, maxSecond, first)
print(second)

print("starting third")  # Finding second guess words that fit the above, based on second
third = third_words(dictionary, fun, maxThird, second)
print(third)

# print to CSV

f = open("AbsurdleWords.csv", "w", newline="")
writer = csv.writer(f)
writer.writerows(third)
f.close()

print("--- %s seconds ---" % (time.time() - start_time))