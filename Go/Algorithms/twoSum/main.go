package main

import "fmt"

func twoSum(nums []int, target int) []int {
	numToIndex := make(map[int]int)
	result := []int{}

	for i, num := range nums {
		complement := target - num
		if idx, found := numToIndex[complement]; found {
			result = append(result, idx, i)
			return result
		}
		numToIndex[num] = i
	}

	return result
}

func main() {
	nums1 := []int{2, 7, 11, 15}
	target1 := 9
	result1 := twoSum(nums1, target1)
	fmt.Println(result1)

	nums2 := []int{3, 2, 4}
	target2 := 6
	result2 := twoSum(nums2, target2)
	fmt.Println(result2)

	nums3 := []int{3, 3}
	target3 := 6
	result3 := twoSum(nums3, target3)
	fmt.Println(result3)
}
