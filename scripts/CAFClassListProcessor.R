library(XML)
readHTMLTable("http://www.actor-framework.org/doc/annotated.html") -> rslt
classes = as.character(rslt[[2]][,1])
classes = gsub("▼", "", classes)
blankChar = substr(classes[1], 1,1)
classes = gsub(blankChar, "", classes)
classes2 = as.character(sapply(classes, function(x){as.character(substr(x, 2, nchar(x)))}))
write.csv(matrix(classes2, nrow = 1), file = "CAF_classes.csv", quote = FALSE)
