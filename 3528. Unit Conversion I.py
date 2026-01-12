class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        zero_equiv = {0: 1}
        i = 0
        conversions.sort(key=lambda x: x[0])
        while i < len(conversions):
            source = conversions[i][0]
            target = conversions[i][1]
            factor = conversions[i][2]
            if zero_equiv.get(source, -1) == -1:
                conversions.append(conversions.pop(i))
                continue
            factor *= (zero_equiv[source] % (10**9+7))
            factor %= 10**9+7
            zero_equiv[target] = factor
            i += 1
        
        final_conversions = []
        keys = list(zero_equiv.keys())
        keys.sort()
        for key in keys:
            final_conversions.append(zero_equiv[key])

        return final_conversions

        