library(xlsx)
getwd()
setwd("C:\\Users\\HUAWEI\\Desktop")
library(readxl)
city_data=read_xls("2013Orig.xls")
rownames(city_data)
city_data<-as.data.frame(city_data)
head(city_data)
rownames(city_data) <- city_data$`城    市`
rownames(city_data)
city_data<-city_data[,-1]#去掉非数值列，将行名变成城市

df<-scale(city_data)#标准化数据并计算欧式距离

city_dist <- dist(df , method = "euclidean")
#去掉空值
city_dist[is.na(city_dist)] <- min(city_dist,na.rm = T)*0.01
#设置种子，保证不变
set.seed()
km <- kmeans(df , 4)
id=km$cluster
list(df[(id==1),1],df[(id==2),2],df[(id==3),3],df[(id==4),4])

#由于分类划分具有不确定性
'''
因为kmeans每次都是随机的把样品分为K个分类，然后计算距离，然后重新分类，
所以每次的运行结果不太一样。对类别及k的数值选择不同，分类结果的好坏也不尽相同。
选择一个正确的聚类数目对于划分数据是很重要的。
R语言中使用Gap统计值来确定k的个数，
他是通过对数据进行bootstrap抽样来比较内差异性。
这里使用cluster软件包里面的clusGap函数计算。
'''

library(cluster)
#计算gap值
city_best <- clusGap(city_data , FUNcluster = pam , K.max = 10)
#提取计算后的Gap结果并转换成数据框
city_gapDF <- as.data.frame(city_best$Tab)
#查看结果
city_gapDF
#导入ggplot2软件包可视化结果
library(ggplot2)
ggplot(city_gapDF , aes(x = 1:nrow(city_gapDF)))+
  geom_line(aes(y = gap) , color = "red") + 
  geom_point(aes(y = gap) , color = "red") +
  geom_errorbar(aes(ymin = gap-SE.sim , ymax = gap + SE.sim) , color = "red") +
  labs(x = "分类数" , y = "Gap")




#聚类方法
city_clust1<- hclust(city_dist , method = "ward.D2") 
#画出聚类图
plot(city_clust2 , hang=-1 , main = "离差平方和" , sub = NULL, xlab = "城市")
#画出分为5类的矩形框下同
rect.hclust(city_clust , k = 4)

city_clust2 <- hclust(city_dist , method = "complete") #最长距离法
#画出聚类图
plot(city_clust2 , hang=-1 , main = "最长距离" , sub = NULL, xlab = "城市")
#画出分为5类的矩形框下同
rect.hclust(city_clust2 , k = 4)

city_clust3<- hclust(city_dist , method = "median") #中间值距离法
#画出聚类图
plot(city_clust3 , hang=-1 , main = "median" , sub = NULL, xlab = "城市")
#画出分为5类的矩形框下同
rect.hclust(city_clust3 , k = 4)

city_clust4 <- hclust(city_dist , method = "average") #类平均法
#画出聚类图
plot(city_clust4 , hang=-1 , main = "类平均法" , sub = NULL, xlab = "城市")
#画出分为5类的矩形框下同
rect.hclust(city_clust4 , k = 4)

city_clust5 <- hclust(city_dist , method = "centroid") #重心法
#画出聚类图
plot(city_clust5 , hang=-1 , main = "重心法" , sub = NULL, xlab = "城市")
#画出分为5类的矩形框下同
rect.hclust(city_clust5 , k = 4)






















