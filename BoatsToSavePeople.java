class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int numberOfBoats,leftPointer,rightPointer,sumOfCurrentWeights;
        numberOfBoats = 0;
        leftPointer = 0;
        rightPointer = people.length-1;
        Arrays.sort(people);
        while(leftPointer <= rightPointer){
            sumOfCurrentWeights = people[leftPointer] + people[rightPointer];
            if(sumOfCurrentWeights > limit){
                numberOfBoats++;
                rightPointer--;
            }
            else {
                numberOfBoats++;
                leftPointer++;
                rightPointer--;
            }
        }
        return numberOfBoats;
    }
}
