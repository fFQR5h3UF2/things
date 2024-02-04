// Submission for Eliminate Maximum Number of Monsters
// Submission url: https://leetcode.com/submissions/detail/1093719534/

package submissions

func eliminateMaximum(dist []int, speed []int) int {
    arrival := []int{}
    length := len(dist)
    for i := 0; i < length; i++ {
        arrival = append(arrival, dist[i] / speed[i])
    }
    slices.Sort(arrival)
    ans := 0
    for i := 0; i < length; i++ {
        if arrival[i] <= i {
            break
        }
        ans += 1
    }
    return ans
}
