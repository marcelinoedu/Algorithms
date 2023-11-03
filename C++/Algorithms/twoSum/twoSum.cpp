#include <iostream>
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> numToIndex;
        std::vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (numToIndex.find(complement) != numToIndex.end()) {
                result.push_back(numToIndex[complement]);
                result.push_back(i);
                return result;
            }
            numToIndex[nums[i]] = i;
        }
        
        return result;
    }
};

int main() {
    Solution solution;

    std::vector<int> nums1;
    nums1.push_back(2);
    nums1.push_back(7);
    nums1.push_back(11);
    nums1.push_back(15);

    std::vector<int> result1 = solution.twoSum(nums1, 9);
    for (int num : result1) {
        std::cout << num << " ";
    }

    std::vector<int> nums2;
    nums2.push_back(3);
    nums2.push_back(2);
    nums2.push_back(4);

    std::vector<int> result2 = solution.twoSum(nums2, 6);
    for (int num : result2) {
        std::cout << num << " ";
    }

    std::vector<int> nums3;
    nums3.push_back(3);
    nums3.push_back(3);

    std::vector<int> result3 = solution.twoSum(nums3, 6);
    for (int num : result3) {
        std::cout << num << " ";
    }

    return 0;
}
