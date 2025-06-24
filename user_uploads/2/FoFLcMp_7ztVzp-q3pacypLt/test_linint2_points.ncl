begin
        n1 = 7
        ;n1 = 13
        n2 = 4
	xi = todouble(fspan(0,n1,n2))
	yi = todouble(fspan(0,n1,n2))
	xo = todouble(fspan(0,n1,n1))
	yo = todouble(fspan(0,n1,n1))

	fi = random_uniform(0, 1, (/3, 2, n2, n2/))

	;print(dimsizes(fi))
	
	print(xi)
	print(yi)
	print(xo)
	print(yo)		
	print(fi)
	
	fo = linint2_points(xi, yi, fi, False, xo, yo, 0)

	;print(dimsizes(fo))
	print(fo)
end
