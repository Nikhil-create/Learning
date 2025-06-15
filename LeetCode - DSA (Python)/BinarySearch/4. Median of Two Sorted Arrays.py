from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        i=j=m1=m2=0

        for _ in range((n1+n2)//2 + 1):
            m2=m1
            if i < n1 and j<n2:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j+=1
                else:
                    m1 = nums1[i]
                    i+=1 
            elif i < n1:
                m1 = nums1[i]
                i+=1
            else:
                m1 = nums2[j]
                j+=1


        if (n1+n2)%2 == 1:
            return float(m1)
        else:
            return (float(m1) + float(m2))/2.0
        