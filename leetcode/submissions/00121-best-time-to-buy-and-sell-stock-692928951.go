// Submission title: for Best Time to Buy and Sell Stock
// Submission url  : https://leetcode.com/submissions/detail/692928951/
// Submission json : {"id": 692928951, "status_display": "Accepted", "lang": "golang", "question_id": 121, "title_slug": "best-time-to-buy-and-sell-stock", "code": "\nfunc maxProfit(prices []int) int {\n\tprofit, index_buy := 0, 0\n\tfor index, price := range prices {\n\t\tif prices[index_buy] > price {\n\t\t\tindex_buy = index\n\t\t}\n\t\tnew_profit := price - prices[index_buy]\n\t\tif new_profit > profit {\n\t\t\tprofit = new_profit\n\t\t}\n\t}\n\treturn profit\n}", "title": "Best Time to Buy and Sell Stock", "url": "/submissions/detail/692928951/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651659233, "status": 10, "runtime": "174 ms", "is_pending": "Not Pending", "memory": "8.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

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
