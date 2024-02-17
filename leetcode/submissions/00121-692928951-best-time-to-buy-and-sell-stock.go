// Submission title: Best Time to Buy and Sell Stock
// Submission url  : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/"
// Submission url  : https://leetcode.com/submissions/detail/692928951/"
package submissions

func maxProfit(prices []int) int {
	profit, index_buy := 0, 0
	for index, price := range prices {
		if prices[index_buy] > price {
			index_buy = index
		}
		new_profit := price - prices[index_buy]
		if new_profit > profit {
			profit = new_profit
		}
	}
	return profit
}
