def main():
	USD_vs_RMB = 6.77
	currency_str_value = input('请输入带单位的货币：')
	unit = currency_str_value[-3:]
	
	if unit == 'USD':
		exchange_rate = USD_vs_RMB
	elif unit == 'CNY':
		exchange_rate = 1 / USD_vs_RMB
	else:
		exchange_rate = -1

	if exchange_rate != -1:
		in_money = eval(currency_str_value[:-3])
		convert_currency = lambda x: x * exchange_rate

		out_money = convert_currency(in_money)

		print('兑换后的金额为：', out_money)


	else:
		print('暂不支持该种货币')


if __name__ =='__main__':
	main()
