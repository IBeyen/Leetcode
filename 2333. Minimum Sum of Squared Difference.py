class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        if len(nums1) == 0:
            return 0
        
        K = k1 + k2

        l = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        if K == 0:
            L = [l[i]**2 for i in range(len(l))]
            return sum(L)

        l.sort()

        if K >= sum(l):
            return 0

        for i in reversed(range(1, len(l))):
            diff = (l[i]-l[i-1])
            if len(l)-i > K:
                break
            if not (len(l)-i)*diff <= K:
                break
            l[i] = l[i-1]
            K -= (len(l)-i)*diff
        
        if l[i] == l[i-1]:
            i -= 1

        S = sum([l[j]**2 for j in range(i)])
    
        print(l)
        print(l[i])


        diff = K//(len(l)-i)

        l[i] -= diff

        K -= diff*(len(l)-i)

        S += (l[i]**2)*(len(l)-i-K) + ((l[i]-1)**2)*K

        return S
        