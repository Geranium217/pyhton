#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int>& A) {
    int n = A.size();
    int maxMoves = 0;
    
    // Sort the array in ascending order
    sort(A.begin(), A.end());
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            // Calculate the sum of the two elements at indices i and j
            int sum = A[i] + A[j];
            
            // Find the number of elements equal to 'sum' in the sorted array
            int count = upper_bound(A.begin(), A.end(), sum) - lower_bound(A.begin(), A.end(), sum);
            
            // Update the maximum moves if the current sum can be obtained more than once
            maxMoves = max(maxMoves, count);
        }
    }
    
    return maxMoves;
}

int main() {
    vector<int> A = {4,1,4,3,3,2,5,2};
    int result = solution(A);
    cout << "Maximum number of moves: " << result << endl;
    return 0;
}
