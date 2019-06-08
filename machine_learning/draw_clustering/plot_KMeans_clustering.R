
args <- commandArgs(TRUE)

#making matrix of Petal.length, Petal.Width from iris data
#data_matrix = iris[,3:4]

#Checkout how the data_matrix looks like. (col = colored by labels, cex = size of data point, pch = plot symbols)
#plot(data_matrix, cex=1 ,pch=20)
#plot(data_matrix, col=iris[,5], cex=1 ,pch=20)


data_file <- args[1]
number_of_clustering <- args[2]
output_file <- args[3]


dataframe <- read.table(data_file, header=TRUE, sep="\t")
jpeg(output_file)

#shuffle dataframe for test purpose
#
shuffled_dataframe <- dataframe[sample(nrow(dataframe)),]
model_dataframe <- shuffled_dataframe[0:145,1:2]
test_dataframe <- shuffled_dataframe[145:150,1:2]
#
#
#
#-----------------------



#Run K-means clustering. 
kc <- kmeans(model_dataframe, number_of_clustering)
kc

plot(model_dataframe, col=kc$cluster, cex=1, pch=20) 
points(kc$centers[,c("Sepal.Length", "Sepal.Width")], col=1:3, pch=23, cex=2) 
points(model_dataframe, col=iris[,5], pch=21, cex=1.4) 

dev.off()
