class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, ans = len(nums), []
        for i in range(n):
            if i and nums[i] == nums[i-1]: continue
            target = -nums[i]
            s, e = i + 1, n - 1
            while s < e:
                if nums[s] + nums[e] < target:
                    s += 1
                elif nums[s] + nums[e] > target:
                    e -= 1
                else:
                    ans.append((nums[i], nums[s], nums[e]))
                    s += 1
                    e -= 1
        return set(ans)