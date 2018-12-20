from django.shortcuts import render, render_to_response

from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from bokeh.models import Range1d
from bokeh.embed import components

from .forms import MortgageNumberForm, RetirementNumberForm
from .calculations import mortgage_payment_for_plot, savings_vs_year_for_plot



	

def make_mortgage_plot(int_r_pct=4.5,tax_pct=1.2, down_pct=20,hoa=0,years=30,pmts=12):
		# create some data
	x_vals , y_vals = mortgage_payment_for_plot(int_r_pct,tax_pct,down_pct,hoa,years,pmts)

	
	# select the tools we want
	TOOLS="pan,wheel_zoom,box_zoom,reset,save"
	TOOLTIPS = [
    			("(Prch. Price, Monthly Pmt)", "($x, $y)"),
    			]

	# the red and blue graphs will share this data range
	xr1 = Range1d(start=150, end=750)
	yr1 = Range1d(start=y_vals[10], end=y_vals[25])

	# build our figures
	p1 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_height=400,
	 sizing_mode = 'scale_width',tooltips = TOOLTIPS,
		x_axis_label='Purchase Price [k$]', y_axis_label='Monthly Outlay [$]',
		title="Monthly Payment vs Purchase Price")

	p1.title.text_font_size = '20pt'
	p1.xaxis.axis_label_text_font_size = '20pt'
	p1.yaxis.axis_label_text_font_size = '20pt'
	p1.xaxis.major_label_text_font_size = "20pt"
	p1.yaxis.major_label_text_font_size = "20pt"
	p1.line(x_vals, y_vals, line_width=3, color="red", alpha=0.5)




	# plots can be a single Bokeh Model, a list/tuple, or even a dictionary
	plots = p1

	return components(plots)

def make_retirement_plot(cagr = 5.5,egg = 5500,spend = 33000, investment = 5500, swr = 4):
		# create some data
	x_vals , y_vals = savings_vs_year_for_plot(cagr,egg,spend,investment,swr)

	
	# select the tools we want
	TOOLS="pan,wheel_zoom,box_zoom,reset,save"
	TOOLTIPS = [
    			("(Year, Investments)", "($x, $y)"),
    			]

	# the red and blue graphs will share this data range
	xr1 = Range1d(start=0, end=x_vals[-1])
	yr1 = Range1d(start=y_vals[1], end=y_vals[-1])

	# build our figures
	p1 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_height=400,
	 sizing_mode = 'scale_width',tooltips = TOOLTIPS,
		x_axis_label='Year', y_axis_label='Retirement Total [k$]',
		title="Retirement Investment TImeline")

	p1.title.text_font_size = '20pt'
	p1.xaxis.axis_label_text_font_size = '20pt'
	p1.yaxis.axis_label_text_font_size = '20pt'
	p1.xaxis.major_label_text_font_size = "20pt"
	p1.yaxis.major_label_text_font_size = "20pt"
	p1.line(x_vals, y_vals, line_width=3, color="blue", alpha=0.5)
	p1.line(x_vals,[0.1*spend/swr]*len(x_vals),line_width=3, color="green", alpha=0.5)




	# plots can be a single Bokeh Model, a list/tuple, or even a dictionary
	plots = p1

	return components(plots)


def index(request):

	context_dict = {'heading': 'Mortgage Payment Calculator','form_route' : 'mortgage'}
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = MortgageNumberForm(request.POST)
	# check whether it's valid:
		if form.is_valid():
	# process the data in form.cleaned_data as required
	# ...
	# redirect to a new URL:
			ir  = float(form['interest_rate'].value())
			dp  = float(form['down_pct'].value())
			yrs = float(form['loan_term'].value())
			hoa = float(form['hoa_monthly'].value())
			tax = float(form['property_tax'].value())
			script, div = make_mortgage_plot(ir,tax,dp,hoa,yrs)
			context_dict.update({'script': script, 'div': div,'form':form})
			return render(request,'plots/index.html',context_dict)



	form = MortgageNumberForm()
	script, div = make_mortgage_plot()
	context_dict.update({'script': script, 'div': div,'form':form})
	#Feed them to the Django template.
	return render(request,'plots/index.html',context_dict)

def retirement(request):
	context_dict = {'heading': 'Retirement Calculator','form_route' : 'retirement'}
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = RetirementNumberForm(request.POST)
	# check whether it's valid:
		if form.is_valid():
	# process the data in form.cleaned_data as required
			cagr = float(form['expected_cagr'].value())
			egg = float(form['current_nest'].value())
			spend  = float(form['expected_spend'].value())
			save = float(form['annual_savings'].value())
			swr = float(form['withdrawal_rate'].value())
			script, div = make_retirement_plot(cagr,egg,spend,save,swr)
			context_dict.update({'script': script, 'div': div,'form':form})
			return render(request,'plots/index.html',context_dict)



	form = RetirementNumberForm()
	script, div = make_retirement_plot()
	context_dict.update({'script': script, 'div': div,'form':form})
	#Feed them to the Django template.
	return render(request,'plots/index.html',context_dict)


def allocation(request):
	context_dict = {'heading': 'Investment / Allocation Calculator : WIP','form_route' : 'allocation'}

	return render(request,'plots/index.html',context_dict)
