// Some js practice

// Function to check if word is a palindrome
function isPalindrome(word) {
    const cleanedWord = word.replace(/[^A-Za-z0-9]/g, '').toLowerCase();
    const reversedWord = cleanedWord.split('').reverse().join('');
    return cleanedWord === reversedWord;
}
// Example usage
console.log(isPalindrome("A man, a plan, a canal: Panama")); // true
console.log(isPalindrome("hello")); // false
// Function to find the largest number in an array
function findLargestNumber(arr) {
    if (arr.length === 0) return null;
    return Math.max(...arr);
}
// Example usage
console.log(findLargestNumber([1, 2, 3, 4, 5])); // 5
console.log(findLargestNumber([-1, -2, -3, -4, -5])); // -1