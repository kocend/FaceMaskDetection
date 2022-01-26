set style data lines
set xrange [0:7]
set yrange [0:1.0]
set xlabel "epoch"
set ylabel "percentage"
plot 'model3.txt' using 1:2 title "loss3",\
'model3.txt' using 1:3 title "accuracy3",\
'model3.txt' using 1:4 title "val loss3",\
'model3.txt' using 1:5 title "val accuracy3"