library(tm)
library(wordcloud)
tabulate <- read.delim(file.choose(), sep=",", stringsAsFactors=FALSE,
                          header=TRUE, na.strings="")
View(tabulate)
head(tabulate, 10)

#Frequent no of words occuring in titles for the gifs
barplot(tabulate[1:10,]$Freq, las = 2, names.arg = tabulate[1:10,]$Word,
        col ="lightblue", main ="Most frequent words",
        ylab = "Word frequencies")

# Wordcloud
set.seed(1234)
wordcloud(words = tabulate$Word, freq = tabulate$Freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))
