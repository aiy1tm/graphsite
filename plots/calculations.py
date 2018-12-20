#calculations.py -- things to web serve up

def monthly_pmt(price,int_r_pct=4.5,tax_pct=1.2, down_pct=20,hoa=0,years=30,pmts=12,):
	loan_amount = price*(100-down_pct)/100
	tax_monthly = loan_amount*(tax_pct)/(100-down_pct)/12
	
	monthly_eff = int_r_pct/(pmts*100)
	denom = 1-pow(1/(1+monthly_eff),pmts*years)
	pi_pay = loan_amount*monthly_eff/denom
	

	return pi_pay+tax_monthly+hoa #80$ monthly insurance guesstimate

def mortgage_payment_for_plot(int_r_pct=4.5,tax_pct=1.2, down_pct=20,hoa=0,years=30,pmts=12,):
	#returns xvals , yvals for bokeh plot
	start_cost = 50
	max_cost = 3000
	cost_step = 25
	range_x = range(start_cost,max_cost,cost_step)
	x_vals = [x for x in range_x]
	y_vals = [monthly_pmt(1000*x,int_r_pct,tax_pct,down_pct,hoa,years,pmts)
	 for x in range_x]
	return x_vals, y_vals

def savings_vs_year_for_plot(cagr = 5.5,egg = 5500,spend = 33000, investment = 5500, swr = 4):
	total = egg
	x_vals = [0]
	y_vals = [egg/1000]
	while swr*total/100 < 1.5*spend:
		x_vals.append(x_vals[-1]+1)
		total = total*(1+cagr/100)
		total+= investment
		y_vals.append(total/1000)
	return x_vals, y_vals

