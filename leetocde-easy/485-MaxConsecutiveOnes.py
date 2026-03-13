def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    count = 0
    streak_count = 0

    for i in nums:
        if i == 1:
            count += 1
            streak_count =max(count,streak_count)
        else:
            count = 0

    return streak_count