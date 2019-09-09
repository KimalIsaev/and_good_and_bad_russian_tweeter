import operator
emoji_dictionary = {')':'😀',
                    '(':'🙁',
                    'XD':'🤣',
                    'xD':'🤣',
                    'ХД':'🤣',
                    ':-|':'😑',
                    ':|':'😐',
                    '._.':'😐',
                    '-_-':'😑',
                    ':D':'😁',
                    ':-D':'😃',
                    '*_*':'😍',
                    '**':'😍',
                    ':-C':'😩',
                    ':C':'😩',
                    ':-/':'😕',
                    ':-\\':'😕',
                    ':O':'😮',
                    'O:':'😮',
                    ':O':'😮',
                    'O:':'😮',
                    'o_O':'😮',
                    'oO':'😮',
                    'o.O':'😮',
                    'owO':'😮',
                    'о_О':'😮',
                    'оО':'😮',
                    'о.О':'😮',
                    ':-p':'😜',
                    ':-P':'😜',
                    ':-Ъ':'😜',
                    ':-Р':'😜',
                    ':-р':'😜',
                    ':p':'😜',
                    ':P':'😜',
                    ':Ъ':'😜',
                    ':Р':'😜',
                    ':р':'😜'}
                    
                    
def just_emojis(string):
    count_emoji = {} 
    for ascii_emo in emoji_dictionary.keys():
        temp_count = string.count(ascii_emo)
        if temp_count>0:
            count_emoji[emoji_dictionary[ascii_emo]] = temp_count
    output = []
    for emo in sorted(count_emoji.items(), key=operator.itemgetter(1)):
        output += [emo[0]]*emo[1]
    return output
