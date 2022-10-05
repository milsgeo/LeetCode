class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_dict={}
        words=s.split()
        if len(pattern)!=len(words):
            return False
        
        for i in range(len(pattern)):
            ch=pattern[i]
            w=words[i]
            
            char_key = 'char_{}'.format(ch)
            char_word = 'word_{}'.format(w)
            
            
            if char_key not in map_dict:
                map_dict[char_key]=i
            if char_word not in map_dict:
                map_dict[char_word]=i
            if map_dict[char_key]!=map_dict[char_word]:
                return False
        return True