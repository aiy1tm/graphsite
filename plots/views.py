from django.shortcuts import render, render_to_response

from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from bokeh.models import Range1d
from bokeh.embed import components

from .forms import NumberForm


def monthly_pmt(price,int_r_pct=4.5,tax_pct=1.2, down_pct=20,hoa=0,years=30,pmts=12,):
	loan_amount = price*(100-down_pct)/100
	tax_monthly = loan_amount*(tax_pct)/(100-down_pct)/12
	
	monthly_eff = int_r_pct/(pmts*100)
	denom = 1-pow(1/(1+monthly_eff),pmts*years)
	pi_pay = loan_amount*monthly_eff/denom
	

	return pi_pay+tax_monthly+hoa #80$ monthly insurance guesstimate
	

def make_bokeh_plot(int_r_pct=4.5,tax_pct=1.2, down_pct=20,hoa=0,years=30,pmts=12):
		# create some data
	range_x = range(50,1250,10)
	x_vals = [x for x in range_x]
	test_nohoa = [monthly_pmt(1000*x,int_r_pct,tax_pct,down_pct,hoa,years,pmts)
	 for x in range_x]
	#test =[monthly_pmt(1000*x) for x in range_x]
	
	# select the tools we want
	TOOLS="pan,wheel_zoom,box_zoom,reset,save"
	TOOLTIPS = [
    ("(Prch. Price, Monthly Pmt)", "($x, $y)"),
    ]


	# the red and blue graphs will share this data range
	xr1 = Range1d(start=200, end=700)
	yr1 = Range1d(start=500, end=3200)

	
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
	p1.line(x_vals, test_nohoa, line_width=3, color="red", alpha=0.5)
	#p1.line(x_vals, test_nohoa, line_width=2, color="blue", alpha=0.5)



	# plots can be a single Bokeh Model, a list/tuple, or even a dictionary
	plots = p1

	return components(plots)


def index(request):

	
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = NumberForm(request.POST)
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
			script, div = make_bokeh_plot(ir,tax,dp,hoa,yrs)
			return render(request,'plots/index.html',{'script' : script , 'div' : div, 'form': form})

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NumberForm()
		script, div = make_bokeh_plot()

	form = NumberForm()
	script, div = make_bokeh_plot()
	#Feed them to the Django template.
	return render(request,'plots/index.html',{'script' : script , 'div' : div, 'form': form})


