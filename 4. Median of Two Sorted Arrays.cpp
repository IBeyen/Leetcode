class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        vector<int> arr3(nums1.size() + nums2.size());
        merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(),
              arr3.begin());
        if (arr3.size() % 2 == 0)
        {
            return (float(arr3[arr3.size() / 2 - 1] + arr3[arr3.size() / 2]) /
                    2);
        }
        return arr3[arr3.size() / 2];
    }
};