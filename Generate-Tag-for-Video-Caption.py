class Solution:
    def generateTag(self, caption: str) -> str:
        subs = caption.split()
        # print(subs)
        if not subs:
            return '#'
        cap = '#' + subs[0].lower() + ''.join(sub.capitalize() for sub in subs[1:])
        # print(cap)
        return cap[:100]