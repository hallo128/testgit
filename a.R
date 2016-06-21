data=read.csv('score3.csv',header=T)
data2=read.table('ws.txt',header=T)
data3=read.table('cp.txt',header=T)

EDA=function(x)
{
  par(mfrow=c(2,2))				#同时做4个图
  hist(x);								#直方图
  plot(x);							#点图
  boxplot(x,horizontal=T);			#箱型图
  qqnorm(x);qqline(x);				#QQ图
  par(mfrow=c(1,1))
}
