class Solution(object):
    def twoSum(self, nums, target):
        func = lambda n: n-(float(target)/2)
        vals = list(map(func, nums))
        inds = [i for i in range(len(nums))]
        rdy = sorted(list(zip(vals, inds)))

        left = 0
        right = len(rdy) - 1

        while left < right:
            cur = rdy[left][0] + rdy[right][0]
            if cur == 0:
                break
            elif cur > 0:
                right -= 1
            else:
                left += 1
        return [rdy[left][1], rdy[right][1]]
      
