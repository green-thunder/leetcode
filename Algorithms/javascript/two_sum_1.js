function twoSum(nums, target) {
    const numMap = new Map(); 
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (numMap.has(complement)) {
            return [numMap.get(complement), i];
        }
        numMap.set(nums[i], i); 
    }
    return [];
}

const nums = [1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 41];
const target = 51;

const result = twoSum(nums, target);
console.log(result);
