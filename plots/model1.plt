set style data lines
set xrange [0:5]
set yrange [0:1.0]
set xlabel "epoch"
set ylabel "percentage"
plot 'porownanie modeli.txt' using 1:2 title "loss1",\
'porownanie modeli.txt' using 1:3 title "accuracy1",\
'porownanie modeli.txt' using 1:4 title "val loss1",\
'porownanie modeli.txt' using 1:5 title "val accuracy1",\